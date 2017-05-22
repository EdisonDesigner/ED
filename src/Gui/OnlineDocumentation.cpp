/***************************************************************************
 *   Copyright (c) 2007 Werner Mayer <wmayer[at]users.sourceforge.net>     *
 *                                                                         *
 *   This file is part of the FreeCAD CAx development system.              *
 *                                                                         *
 *   This library is free software; you can redistribute it and/or         *
 *   modify it under the terms of the GNU Library General Public           *
 *   License as published by the Free Software Foundation; either          *
 *   version 2 of the License, or (at your option) any later version.      *
 *                                                                         *
 *   This library  is distributed in the hope that it will be useful,      *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU Library General Public License for more details.                  *
 *                                                                         *
 *   You should have received a copy of the GNU Library General Public     *
 *   License along with this library; see the file COPYING.LIB. If not,    *
 *   write to the Free Software Foundation, Inc., 59 Temple Place,         *
 *   Suite 330, Boston, MA  02111-1307, USA                                *
 *                                                                         *
 ***************************************************************************/


#include "PreCompiled.h"

#ifndef _PreComp_
# include <QBuffer>
# include <QHttpResponseHeader>
# include <QMessageBox>
# include <QTcpSocket>
#endif

#include <sstream>
#include <CXX/Objects.hxx>
#include <zipios++/zipfile.h>

#include <Base/Interpreter.h>
#include <Base/Stream.h>

#include <App/Application.h>

#include "MainWindow.h"
#include "BitmapFactory.h"
#include "OnlineDocumentation.h"

using namespace Gui;

// the favicon
static const unsigned int navicon_data_len = 318;
static const unsigned char navicon_data[] = {
    0x00,0x00,0x01,0x00,0x01,0x00,0x10,0x10,0x10,0x00,0x01,0x00,0x04,0x00,
    0x28,0x01,0x00,0x00,0x16,0x00,0x00,0x00,0x28,0x00,0x00,0x00,0x10,0x00,
    0x00,0x00,0x20,0x00,0x00,0x00,0x01,0x00,0x04,0x00,0x00,0x00,0x00,0x00,
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xff,0x00,
    0x84,0x82,0x84,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x11,0x11,0x00,
    0x00,0x00,0x00,0x00,0x01,0x10,0x01,0x10,0x00,0x00,0x00,0x00,0x11,0x00,
    0x00,0x10,0x00,0x00,0x00,0x00,0x11,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
    0x11,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x11,0x00,0x00,0x00,0x00,0x00,
    0x00,0x00,0x11,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x11,0x00,0x00,0x10,
    0x00,0x00,0x00,0x00,0x01,0x10,0x01,0x10,0x00,0x20,0x00,0x00,0x00,0x11,
    0x11,0x00,0x00,0x20,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x20,0x00,0x00,
    0x00,0x00,0x00,0x00,0x00,0x20,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x20,
    0x00,0x00,0x00,0x00,0x02,0x22,0x22,0x20,0x00,0x00,0x00,0x00,0x00,0x00,
    0x00,0x00,0xff,0xff,0x00,0x00,0xfc,0x3f,0x00,0x00,0xf9,0x9f,0x00,0x00,
    0x93,0xdf,0x00,0x00,0x93,0xff,0x00,0x00,0x93,0xff,0x00,0x00,0x93,0xff,
    0x00,0x00,0x93,0xfd,0x00,0x00,0x81,0xd8,0x00,0x00,0x99,0x9d,0x00,0x00,
    0x9c,0x3d,0x00,0x00,0x9f,0xfd,0x00,0x00,0x80,0xfd,0x00,0x00,0xff,0x7d,
    0x00,0x00,0xfe,0x01,0x00,0x00,0xff,0x7f,0x00,0x00};

OnlineDocumentation::OnlineDocumentation()
{
    // store the listed files in a stringlist
    std::string path = App::GetApplication().getHomePath();
    path += "/doc/docs.zip";
    zipios::ZipFile zip(path);
    if (zip.isValid()) {
        zipios::ConstEntries entries = zip.entries();
        for (zipios::ConstEntries::iterator it = entries.begin(); it != entries.end(); ++it) {
            this->files.push_back(QString::fromLatin1((*it)->getFileName().c_str()));
        }
    }
}

OnlineDocumentation::~OnlineDocumentation()
{
}

QByteArray OnlineDocumentation::loadResource(const QString& filename) const
{
    QString fn = filename;
    fn = filename.mid(1);
    QByteArray res;

    if (fn == QLatin1String("favicon.ico")) {
        // Return an resource icon in ico format
        res.reserve(navicon_data_len);
        for (int i=0; i<(int)navicon_data_len;i++) {
            res[i] = navicon_data[i];
        }
    }
    else if (filename == QLatin1String("/")) {
        // load the startpage
        QString header = QString::fromLatin1(
            "<!doctype html PUBLIC \"-//W3C//DTD HTML 4.0 Transitional//EN\">"
            "<link rel=\"shortcut icon\" href=\"favicon.ico\" type=\"image/x-icon\">"
            "<html><head><title>Python: Index of Modules</title>"
            "</head><body bgcolor=\"#f0f0f8\">"
            ""
            "<table width=\"100%\" cellspacing=0 cellpadding=2 border=0 summary=\"heading\">"
            "<tr bgcolor=\"#7799ee\">"
            "<td valign=bottom>&nbsp;<br>"
            "<font color=\"#ffffff\" face=\"helvetica, arial\">&nbsp;<br><big><big><strong>Python: Index of Modules</strong></big></big></font></td>"
            "<td align=right valign=bottom>"
            "<font color=\"#ffffff\" face=\"helvetica, arial\">&nbsp;</font></td></tr></table>"
            "<p><p>"
            "<table width=\"100%\" cellspacing=0 cellpadding=2 border=0 summary=\"section\">"
            "<tr bgcolor=\"#ee77aa\">"
            "<td colspan=3 valign=bottom>&nbsp;<br>"
            "<font color=\"#ffffff\" face=\"helvetica, arial\"><big><strong>ED Modules</strong></big></font></td></tr>"
            ""
            "<tr><td bgcolor=\"#ee77aa\"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>"
            "<td width=\"100%\"><table width=\"100%\" summary=\"list\"><tr><td width=\"25%\" valign=top>");
        int ct=0;
        for (QStringList::ConstIterator it = this->files.begin(); it != this->files.end(); ++it) {
            QString file = *it;
            if (file.endsWith(QLatin1String(".html"))) {
                file.chop(5);
                if ((++ct)%15 == 0)
                    header += QString::fromLatin1("</td><td width=\"25%\" valign=top>");
                header += QString::fromLatin1("<a href=\"%1.html\">%2</a><br>").arg(file).arg(file);
            }
        }

        header += QString::fromLatin1(
        "</td></tr></table></td></tr></table> <p>"
        //"<p align=right>"
        //"<font color=\"#909090\" face=\"helvetica, arial\"><strong>"
        //"pydoc</strong> by Ka-Ping Yee &lt;ping@lfw.org&gt;</font>"
        "</body></html>");
        res.append(header);
    }
    else if (this->files.contains(fn)) {
        // load the requested page from zip 
        std::string path = App::GetApplication().getHomePath();
        path += "/doc/docs.zip";
        zipios::ZipFile zip(path);
        zipios::ConstEntryPointer entry = zip.getEntry((const char*)fn.toLatin1());
        std::istream* str = zip.getInputStream(entry);

        // set size of the array so that no re-allocation is needed when reading from the stream
        res.reserve(entry->getSize());
        QBuffer buffer(&res);
        buffer.open(QIODevice::WriteOnly);
        Base::IODeviceOStreambuf buf(&buffer);
        (*str) >> &buf;
    }
    else {
        // load the error page
        QHttpResponseHeader header(404, QString::fromLatin1("File not found"));
        header.setContentType(QString::fromLatin1("text/html\r\n"
            "\r\n"
            "<html><head><title>Error</title></head>"
            "<body bgcolor=\"#f0f0f8\">"
            "<table width=\"100%\" cellspacing=0 cellpadding=2 border=0 summary=\"heading\">"
            "<tr bgcolor=\"#7799ee\">"
            "<td valign=bottom>&nbsp;<br>"
            "<font color=\"#ffffff\" face=\"helvetica, arial\">&nbsp;<br><big><big><strong>ED Documentation</strong></big></big></font></td>"
            "<td align=right valign=bottom>"
            "<font color=\"#ffffff\" face=\"helvetica, arial\">&nbsp;</font></td></tr></table>"
            "<p><p>"
            "<h1>404 - File not found</h1>"
            "<div><p><strong>The requested URL was not found on this server."
            "</strong></p>"
            "</div></body>"
            "</html>"
            "\r\n"));
        res.append(header.toString());
    }

    return res;
}

PythonOnlineHelp::PythonOnlineHelp()
{
}

PythonOnlineHelp::~PythonOnlineHelp()
{
}

QByteArray PythonOnlineHelp::loadResource(const QString& filename) const
{
    QString fn = filename;
    fn = filename.mid(1);
    QByteArray res;

    if (fn == QLatin1String("favicon.ico")) {
        // Return an resource icon in ico format
        res.reserve(navicon_data_len);
        for (int i=0; i<(int)navicon_data_len;i++) {
            res[i] = navicon_data[i];
        }
    }
    else if (filename == QLatin1String("/")) {
        // get the global interpreter lock otherwise the app may crash with the error
        // 'PyThreadState_Get: no current thread' (see pystate.c)
        Base::PyGILStateLocker lock;
        PyObject* main = PyImport_AddModule("__main__");
        PyObject* dict = PyModule_GetDict(main);
        dict = PyDict_Copy(dict);

        QByteArray cmd =
            "import string, os, sys, pydoc, pkgutil\n"
            "\n"
            "class EDDoc(pydoc.HTMLDoc):\n"
            "    def index(self, dir, shadowed=None):\n"
            "        \"\"\"Generate an HTML index for a directory of modules.\"\"\"\n"
            "        modpkgs = []\n"
            "        if shadowed is None: shadowed = {}\n"
            "        for importer, name, ispkg in pkgutil.iter_modules([dir]):\n"
            "            if name == 'Init': continue\n"
            "            if name == 'InitGui': continue\n"
            "            if name[-2:] == '_d': continue\n"
            "            modpkgs.append((name, '', ispkg, name in shadowed))\n"
            "            shadowed[name] = 1\n"
            "\n"
            "        if len(modpkgs) == 0: return None\n"
            "        modpkgs.sort()\n"
            "        contents = self.multicolumn(modpkgs, self.modpkglink)\n"
            "        return self.bigsection(dir, '#ffffff', '#ee77aa', contents)\n"
            "\n"
            "pydoc.html=EDDoc()\n"
            "title='ED Python Modules Index'\n"
            "\n"
            "heading = pydoc.html.heading("
            "'<big><big><strong>Python: Index of Modules</strong></big></big>',"
            "'#ffffff', '#7799ee')\n"
            "def bltinlink(name):\n"
            "    return '<a href=\"%s.html\">%s</a>' % (name, name)\n"
            "names = filter(lambda x: x != '__main__',\n"
            "               sys.builtin_module_names)\n"
            "contents = pydoc.html.multicolumn(names, bltinlink)\n"
            "indices = ['<p>' + pydoc.html.bigsection(\n"
            "    'Built-in Modules', '#ffffff', '#ee77aa', contents)]\n"
            "\n"
            "names = ['ED', 'EDGui']\n"
            "contents = pydoc.html.multicolumn(names, bltinlink)\n"
            "indices.append('<p>' + pydoc.html.bigsection(\n"
            "    'Built-in ED Modules', '#ffffff', '#ee77aa', contents))\n"
            "\n"
            "seen = {}\n"
            "for dir in sys.path:\n"
            "    dir = os.path.realpath(dir)\n"
            "    ret = pydoc.html.index(dir, seen)\n"
            "    if ret != None:\n"
            "        indices.append(ret)\n"
            "contents = heading + string.join(indices) + '''<p align=right>\n"
            "<font color=\"#909090\" face=\"helvetica, arial\"><strong>\n"
            "pydoc</strong> by Ka-Ping Yee &lt;ping@lfw.org&gt;</font>'''\n"
            "htmldocument=pydoc.html.page(title,contents)\n";

        PyObject* result = PyRun_String(cmd.constData(), Py_file_input, dict, dict);
        if (result) {
            Py_DECREF(result);
            result = PyDict_GetItemString(dict, "htmldocument");
            const char* contents = PyString_AsString(result);
            res.append("HTTP/1.0 200 OK\n");
            res.append("Content-type: text/html\n");
            res.append(contents);
            return res;
        }
        else {
            // load the error page
            PyErr_Clear();
            res = fileNotFound();
        }

        Py_DECREF(dict);
    }
    else {
        // get the global interpreter lock otherwise the app may crash with the error
        // 'PyThreadState_Get: no current thread' (see pystate.c)
        Base::PyGILStateLocker lock;
        QString name = fn.left(fn.length()-5);
        PyObject* main = PyImport_AddModule("__main__");
        PyObject* dict = PyModule_GetDict(main);
        dict = PyDict_Copy(dict);
        QByteArray cmd = 
            "import pydoc\n"
            "object, name = pydoc.resolve(\"";
        cmd += name.toUtf8();
        cmd += "\")\npage = pydoc.html.page(pydoc.describe(object), pydoc.html.document(object, name))\n";
        PyObject* result = PyRun_String(cmd.constData(), Py_file_input, dict, dict);
        if (result) {
            Py_DECREF(result);
            result = PyDict_GetItemString(dict, "page");
            const char* page = PyString_AsString(result);
            res.append("HTTP/1.0 200 OK\n");
            res.append("Content-type: text/html\n");
            res.append(page);
        }
        else {
            // get information about the error
            Base::PyException e;
            Base::Console().Warning("PythonOnlineHelp::loadResource: %s\n", e.what());
            // load the error page
            res = fileNotFound();
        }

        Py_DECREF(dict);
    }

    return res;
}

QByteArray PythonOnlineHelp::fileNotFound() const
{
    QByteArray res;
    QHttpResponseHeader header(404, QString::fromLatin1("File not found"));
    header.setContentType(QString::fromLatin1("text/html\r\n"
        "\r\n"
        "<html><head><title>Error</title></head>"
        "<body bgcolor=\"#f0f0f8\">"
        "<table width=\"100%\" cellspacing=0 cellpadding=2 border=0 summary=\"heading\">"
        "<tr bgcolor=\"#7799ee\">"
        "<td valign=bottom>&nbsp;<br>"
        "<font color=\"#ffffff\" face=\"helvetica, arial\">&nbsp;<br><big><big><strong>ED Documentation</strong></big></big></font></td>"
        "<td align=right valign=bottom>"
        "<font color=\"#ffffff\" face=\"helvetica, arial\">&nbsp;</font></td></tr></table>"
        "<p><p>"
        "<h1>404 - File not found</h1>"
        "<div><p><strong>The requested URL was not found on this server."
        "</strong></p>"
        "</div></body>"
        "</html>"
        "\r\n"));
    res.append(header.toString());
    return res;
}

HttpServer::HttpServer(QObject* parent)
  : QTcpServer(parent), disabled(false)
{
}

void HttpServer::incomingConnection(int socket)
{
    if (disabled)
        return;

    // When a new client connects the server constructs a QTcpSocket and all
    // communication with the client is done over this QTcpSocket. QTcpSocket
    // works asynchronously, this means that all the communication is done
    // in the two slots readClient() and discardClient().
    QTcpSocket* s = new QTcpSocket(this);
    connect(s, SIGNAL(readyRead()), this, SLOT(readClient()));
    connect(s, SIGNAL(disconnected()), this, SLOT(discardClient()));
    s->setSocketDescriptor(socket);
}

void HttpServer::pause()
{
    disabled = true;
}

void HttpServer::resume()
{
    disabled = false;
}

void HttpServer::readClient()
{
    if (disabled)
        return;

    // This slot is called when the client sent data to the server. The
    // server looks if it was a GET request and  sends back the 
    // corresponding HTML document from the ZIP file.
    QTcpSocket* socket = (QTcpSocket*)sender();
    if (socket->canReadLine()) {
        QString request = QString::fromLatin1(socket->readLine());
        QHttpRequestHeader header(request);
        if (header.method() == QLatin1String("GET")) {
            socket->write(help.loadResource(header.path()));
            socket->close();
            if (socket->state() == QTcpSocket::UnconnectedState) {
                //mark the socket for deletion but do not destroy immediately
                socket->deleteLater();
            }
        }
    }
}

void HttpServer::discardClient()
{
    QTcpSocket* socket = (QTcpSocket*)sender();
    socket->deleteLater();
}

// --------------------------------------------------------------------

/* TRANSLATOR Gui::StdCmdPythonHelp */

StdCmdPythonHelp::StdCmdPythonHelp()
  : Command("Std_PythonHelp"), server(0)
{
    sGroup        = QT_TR_NOOP("Tools");
    sMenuText     = QT_TR_NOOP("Automatic python modules documentation");
    sToolTipText  = QT_TR_NOOP("Opens a browser to show the Python modules documentation");
    sWhatsThis    = QT_TR_NOOP("Opens a browser to show the Python modules documentation");
    sStatusTip    = QT_TR_NOOP("Opens a browser to show the Python modules documentation");
    sPixmap       = "applications-python";
}

StdCmdPythonHelp::~StdCmdPythonHelp()
{
    if (server) {
        server->close();
        delete server;
    }
}

void StdCmdPythonHelp::activated(int iMsg)
{
    // try to open a connection over this port
    qint16 port = 7465;
    if (!this->server)
        this->server = new HttpServer();

    // if server is not yet running try to open one
    if (this->server->isListening() || 
        this->server->listen(QHostAddress(QHostAddress::LocalHost), port)) {
        // okay the server is running, now we try to open the system internet browser
        bool failed = true;

        // The webbrowser Python module allows to start the system browser in an 
        // OS-independent way
        Base::PyGILStateLocker lock;
        PyObject* module = PyImport_ImportModule("webbrowser");
        if (module) {
            // get the methods dictionary and search for the 'open' method
            PyObject* dict = PyModule_GetDict(module);
            PyObject* func = PyDict_GetItemString(dict, "open");
            if (func) {
                char szBuf[201];
                snprintf(szBuf, 200, "http://localhost:%d", port);
                PyObject* args = Py_BuildValue("(s)", szBuf);
                PyObject* result = PyEval_CallObject(func,args);
                if (result)
                    failed = false;
        
                // decrement the args and module reference
                Py_XDECREF(result);
                Py_DECREF(args);
                Py_DECREF(module);
            }
        }

        // print error message on failure
        if (failed) {
            QMessageBox::critical(Gui::getMainWindow(), QObject::tr("No Browser"), 
                QObject::tr("Unable to open your browser.\n\n"
                "Please open a browser window and type in: http://localhost:%1.").arg(port));
        }
    }
    else {
        QMessageBox::critical(Gui::getMainWindow(), QObject::tr("No Server"), 
            QObject::tr("Unable to start the server to port %1: %2.").arg(port).arg(server->errorString()));
    }
}

bool Gui::OpenURLInBrowser(const char * URL)
{
    // The webbrowser Python module allows to start the system browser in an OS-independent way
    bool failed = true;
    Base::PyGILStateLocker lock;
    PyObject* module = PyImport_ImportModule("webbrowser");
    if (module) {
        // get the methods dictionary and search for the 'open' method
        PyObject* dict = PyModule_GetDict(module);
        PyObject* func = PyDict_GetItemString(dict, "open");
        if (func) {
            PyObject* args = Py_BuildValue("(s)", URL);
            PyObject* result = PyEval_CallObject(func,args);
            if (result)
                failed = false;
        
            // decrement the args and module reference
            Py_XDECREF(result);
            Py_DECREF(args);
            Py_DECREF(module);
        }
    } 

    // print error message on failure
    if (failed) {
        QMessageBox::critical(Gui::getMainWindow(), QObject::tr("No Browser"), 
            QObject::tr("Unable to open your system browser."));
        return false;
    }
  
    return true;
}


#include "moc_OnlineDocumentation.cpp"
