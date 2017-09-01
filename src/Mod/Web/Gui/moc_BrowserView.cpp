/****************************************************************************
** Meta object code from reading C++ file 'BrowserView.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "BrowserView.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'BrowserView.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_WebGui__WebView[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       3,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       2,       // signalCount

 // signals: signature, parameters, type, tag, flags
      21,   17,   16,   16, 0x05,
      53,   16,   16,   16, 0x05,

 // slots: signature, parameters, type, tag, flags
      79,   16,   16,   16, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_WebGui__WebView[] = {
    "WebGui::WebView\0\0url\0"
    "openLinkInExternalBrowser(QUrl)\0"
    "openLinkInNewWindow(QUrl)\0"
    "triggerContextMenuAction(int)\0"
};

void WebGui::WebView::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        WebView *_t = static_cast<WebView *>(_o);
        switch (_id) {
        case 0: _t->openLinkInExternalBrowser((*reinterpret_cast< const QUrl(*)>(_a[1]))); break;
        case 1: _t->openLinkInNewWindow((*reinterpret_cast< const QUrl(*)>(_a[1]))); break;
        case 2: _t->triggerContextMenuAction((*reinterpret_cast< int(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData WebGui::WebView::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject WebGui::WebView::staticMetaObject = {
    { &QWebView::staticMetaObject, qt_meta_stringdata_WebGui__WebView,
      qt_meta_data_WebGui__WebView, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &WebGui::WebView::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *WebGui::WebView::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *WebGui::WebView::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_WebGui__WebView))
        return static_cast<void*>(const_cast< WebView*>(this));
    return QWebView::qt_metacast(_clname);
}

int WebGui::WebView::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWebView::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 3)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    }
    return _id;
}

// SIGNAL 0
void WebGui::WebView::openLinkInExternalBrowser(const QUrl & _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void WebGui::WebView::openLinkInNewWindow(const QUrl & _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}
static const uint qt_meta_data_WebGui__BrowserView[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       9,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      21,   20,   20,   20, 0x09,
      37,   20,   20,   20, 0x09,
      57,   20,   20,   20, 0x09,
      82,   78,   20,   20, 0x09,
     112,  107,  102,   20, 0x09,
     145,  137,   20,   20, 0x09,
     188,  182,   20,   20, 0x09,
     225,   78,   20,   20, 0x09,
     259,   20,   20,   20, 0x09,

       0        // eod
};

static const char qt_meta_stringdata_WebGui__BrowserView[] = {
    "WebGui::BrowserView\0\0onLoadStarted()\0"
    "onLoadProgress(int)\0onLoadFinished(bool)\0"
    "url\0onLinkClicked(QUrl)\0bool\0host\0"
    "chckHostAllowed(QString)\0request\0"
    "onDownloadRequested(QNetworkRequest)\0"
    "reply\0onUnsupportedContent(QNetworkReply*)\0"
    "onOpenLinkInExternalBrowser(QUrl)\0"
    "onOpenLinkInNewWindow(QUrl)\0"
};

void WebGui::BrowserView::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        BrowserView *_t = static_cast<BrowserView *>(_o);
        switch (_id) {
        case 0: _t->onLoadStarted(); break;
        case 1: _t->onLoadProgress((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 2: _t->onLoadFinished((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 3: _t->onLinkClicked((*reinterpret_cast< const QUrl(*)>(_a[1]))); break;
        case 4: { bool _r = _t->chckHostAllowed((*reinterpret_cast< const QString(*)>(_a[1])));
            if (_a[0]) *reinterpret_cast< bool*>(_a[0]) = _r; }  break;
        case 5: _t->onDownloadRequested((*reinterpret_cast< const QNetworkRequest(*)>(_a[1]))); break;
        case 6: _t->onUnsupportedContent((*reinterpret_cast< QNetworkReply*(*)>(_a[1]))); break;
        case 7: _t->onOpenLinkInExternalBrowser((*reinterpret_cast< const QUrl(*)>(_a[1]))); break;
        case 8: _t->onOpenLinkInNewWindow((*reinterpret_cast< const QUrl(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData WebGui::BrowserView::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject WebGui::BrowserView::staticMetaObject = {
    { &Gui::MDIView::staticMetaObject, qt_meta_stringdata_WebGui__BrowserView,
      qt_meta_data_WebGui__BrowserView, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &WebGui::BrowserView::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *WebGui::BrowserView::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *WebGui::BrowserView::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_WebGui__BrowserView))
        return static_cast<void*>(const_cast< BrowserView*>(this));
    if (!strcmp(_clname, "Gui::WindowParameter"))
        return static_cast< Gui::WindowParameter*>(const_cast< BrowserView*>(this));
    typedef Gui::MDIView QMocSuperClass;
    return QMocSuperClass::qt_metacast(_clname);
}

int WebGui::BrowserView::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    typedef Gui::MDIView QMocSuperClass;
    _id = QMocSuperClass::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 9)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 9;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
