#***************************************************************************
#*                                                                         *
#*   Copyright (c) 2012                                                    * 
#*   Yorik van Havre <yorik@uncreated.net>                                 * 
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************

# This is the start page template

import os,ED,EDGui,tempfile,time,zipfile,urllib,re,cStringIO
from PySide import QtGui
from xml.etree.ElementTree import parse

EDGui.addLanguagePath(":/translations")
EDGui.updateLocale()

def translate(context,text):
    "convenience function for the Qt translator"
    # return str(QtGui.QApplication.translate(context, text, None, QtGui.QApplication.UnicodeUTF8).toUtf8())
    u = QtGui.QApplication.translate(context, text, None,
                                     QtGui.QApplication.UnicodeUTF8).encode("utf8")
    s = cStringIO.StringIO()
    for i in u:
        if ord(i) == 39:
            s.write("\\'")
        else:
            s.write(i)
    t = s.getvalue()
    s.close()
    return t

# texts to be translated

text01 = translate("StartPage","FreeCAD Start Center")
text02 = translate("StartPage","Start a new project")
text03 = translate("StartPage","Recent Files")
text04 = translate("StartPage","Latest commits")
text05 = translate("StartPage","On the web")
text06 = translate("StartPage","Example projects")
text07 = translate("StartPage","Getting started")
text08 = translate("StartPage","The FreeCAD interface is divided in workbenches, which are sets of tools suited for a specific task. You can start with one of the workbenches in this list, or with the complete workbench, which presents you with some of the most used tools gathered from other workbenches. Click to read more about workbenches on the FreeCAD website.")
text09 = translate("StartPage","http://edisondesigner.tistory.com/category/Manuals")
text10 = translate("StartPage","Example workflow")
text11 = translate("StartPage","Designing parts")
text12 = translate("StartPage","The <b>Part Design</b> workbench is designed to create complex pieces based on constrained 2D sketches. Use it to draw 2D shapes, constrain some of their elements and extrude them to form 3D pieces.")
text13 = translate("StartPage","Part Design")
text14 = translate("StartPage","Working with Meshes")
text15 = translate("StartPage","The <b>Mesh Workbench</b> is used to work with Mesh objects. Meshes are simpler 3D objects than Part objects, but they are often easier to import and export to/from other applications.")
text16 = translate("StartPage","FreeCAD offers you several tools to convert between Mesh and Part objects.")
text17 = translate("StartPage","Work with Meshes")
text18 = translate("StartPage","This is the FreeCAD Homepage. Here you will be able to find a lot of information about FreeCAD, including tutorials, examples and user documentation.")
text19 = translate("StartPage","FreeCAD Homepage")
text20 = translate("StartPage","This is the official user manual of FreeCAD, built, maintained and translated by the FreeCAD community.")
text21 = translate("StartPage","http://www.freecadweb.org/wiki/index.php?title=Online_Help_Toc")
text22 = translate("StartPage","User manual")
text23 = translate("StartPage","The tutorials section on the FreeCAD website")
text24 = translate("StartPage","http://edisondesigner.tistory.com/category/Tutorials")
text25 = translate("StartPage","Tutorials")
text26 = translate("StartPage","The section of the FreeCAD website dedicated to python scripting, with examples, explanations, and API commands.")
text27 = translate("StartPage","http://www.freecadweb.org/wiki/index.php?title=Power_users_hub")
text28 = translate("StartPage","Python resources")
text29 = translate("StartPage","A blog dedicated to teaching FreeCAD, maintained by members of the FreeCAD community")
text30 = translate("StartPage","The FreeCAD-tutorial blog")
text31 = translate("StartPage","<b>Development versions</b> are made available by community members from time to time and usually contain the latest changes, but are more likely to contain bugs.")
text32 = translate("StartPage","Obtain a development version")
text33 = translate("StartPage","Schenkel STEP file")
text34 = translate("StartPage","Load a PartDesign example")
text35 = translate("StartPage","Load a connecting rod example")




text40 = translate("StartPage","file size:")
text41 = translate("StartPage","creation time:")
text42 = translate("StartPage","last modified:")
text43 = translate("StartPage","location:")
text44 = translate("StartPage","File not found")
text45 = translate("StartPage","Your version of FreeCAD is up to date.")
text46 = translate("StartPage","There is a new release of FreeCAD available.")
text47 = translate("StartPage","See all commits")

# get ED version

v = ED.Version()
vmajor = v[0]
vminor = v[1]
vbuild = v[2].split(" ")[0]

# here is the html page skeleton

page = """
<html>
  <head>
    <title>EdisonDesigner - Start page</title>

    <script language="javascript">

        var linkDescriptions = [];

        function JSONscriptRequest(fullUrl) {
            // REST request path
            this.fullUrl = fullUrl; 
            // Get the DOM location to put the script tag
            this.headLoc = document.getElementsByTagName("head").item(0);
            // Generate a unique script tag id
            this.scriptId = 'JscriptId' + JSONscriptRequest.scriptCounter++;
        }

        // Static script ID counter
        JSONscriptRequest.scriptCounter = 1;

        JSONscriptRequest.prototype.buildScriptTag = function () {
            // Create the script tag
            this.scriptObj = document.createElement("script");
            // Add script object attributes
            this.scriptObj.setAttribute("type", "text/javascript");
            this.scriptObj.setAttribute("charset", "utf-8");
            this.scriptObj.setAttribute("src", this.fullUrl);
            this.scriptObj.setAttribute("id", this.scriptId);
        }
 
        JSONscriptRequest.prototype.removeScriptTag = function () {
            // Destroy the script tag
            this.headLoc.removeChild(this.scriptObj);  
        }

        JSONscriptRequest.prototype.addScriptTag = function () {
            // Create the script tag
            this.headLoc.appendChild(this.scriptObj);
        }

        function show(theText) {
            ddiv = document.getElementById("description");
            if (theText == "") theText = "&nbsp;";
            ddiv.innerHTML = theText;
        }
        
        function checkVersion(data) {
            vdiv = document.getElementById("versionbox");
            var cmajor = """ + vmajor + """;
            var cminor = """ + vminor + """;
            var cbuild = """ + vbuild + """;
            var amajor = data[0]['major'];
            var aminor = data[0]['minor'];
            var abuild = data[0]['build'];
            if (cmajor >= amajor && cminor >= aminor && cbuild >= abuild) {
                vdiv.innerHTML=" """ + text45 + """: """ + vmajor + """.""" + vminor + """.""" + vbuild + """";
            } else {
                vdiv.innerHTML="<a href=exthttp://github.com/FreeCAD/FreeCAD/releases/latest> """ + text46 + """:"+amajor+"."+aminor+"."+abuild+"</a>";
            }
        }

        function load() {
            // load latest news
            ddiv = document.getElementById("news");
            ddiv.innerHTML = "Connecting...";
            var tobj=new JSONscriptRequest('https://api.github.com/repos/FreeCAD/FreeCAD/commits?callback=showTweets');
            tobj.buildScriptTag(); // Build the script tag
            tobj.addScriptTag(); // Execute (add) the script tag
            ddiv.innerHTML = "Downloading latest news...";
            
            // load version
            var script = document.createElement('script');
            script.src = 'http://www.freecadweb.org/version.php?callback=checkVersion';
            document.body.appendChild(script);
        }

        function stripTags(text) {
            // from http://www.pagecolumn.com/tool/all_about_html_tags.htm /<\s*\/?\s*span\s*.*?>/g
            stripped = text.replace("<table", "<div");
            stripped = stripped.replace("</table", "</div");
            stripped = stripped.replace("<tr", "<tr");
            stripped = stripped.replace("</tr", "</tr");
            stripped = stripped.replace("<td", "<td");
            stripped = stripped.replace("</td", "</td");
            stripped = stripped.replace("555px", "auto");
            stripped = stripped.replace("border:1px", "border:0px");
            stripped = stripped.replace("color:#000000;","");
            return stripped;
        }

        function showTweets(data) {
            ddiv = document.getElementById('news');
            ddiv.innerHTML = "Received";
            var html = ['<ul>'];
            for (var i = 0; i < 15; i++) {
                html.push('<li><img src="web.png">&nbsp;<a href="ext', data.data[i].commit.url, '" onMouseOver="showDescr(', i+1, ')" onMouseOut="showDescr()">', data.data[i].commit.message, '</a></li>');
                if ("message" in data.data[i].commit) {
                    linkDescriptions.push(stripTags(data.data[i].commit.message)+'<br/>'+data.data[i].commit.author.name+'<br/>'+data.data[i].commit.author.date);
                } else {
                    linkDescriptions.push("");
                }
                
            }
            html.push('</ul>');
            html.push('<a href="exthttps://github.com/EdisonDesigner/ED/commits/master">""" + text47 + """<a/>');
            ddiv.innerHTML = html.join('');
        }

        function showDescr(d) {
            if (d) {
                show(linkDescriptions[d-1]);
            } else {
                show("");
            }
        }

        function scroller() {
            desc = document.getElementById("description");
            base = document.getElementById("column").offsetTop;
            scro = window.scrollY;
            if (scro > base) {
                desc.className = "stick";
            } else {
                desc.className = "";
            }
        }

        document.onmousemove=scroller;

    </script>

    <style type="text/css">

        body {
            background: #basecolor;
            color: #textcolor;
            font-family: Arial, Helvetica, Sans;
            font-size: 11px;
        }

        a {
            color: #linkcolor;
            font-weight: bold;
            text-decoration: none;
            padding: 2px;
        }

        a:hover {
            color: white;
            background: #linkcolor;
            border-radius: 5px;
        }

        p {
			font-size: 1.2em;
			line-height: 1.5em;
            text-align: justify;
        }

        .left {
            text-align: left;
        }

        h1 {
            font-size: 3em;
            letter-spacing: 2px;
            padding: 20px 0 0 80px;
            align: bottom;
            color: #000000;
        }

        h2 {
            font-size: 1.5em;
        }
		
		h3 {
			font-size: 1.2em;
			line-height: 1.5em;
		}

        ul {
			list-style-type: none;
            padding: 0;
        }
		
		li {
			font-size: 1.3em;
			line-height: 1.7em;
		}

        #column {
            margin: 0 350px 0 10px;
        }

        #column img {
            max-width: 14px;
        }

        .block {
            background: #windowcolor;
            border-radius: 5px;
            padding: 8px;
            margin-bottom: 10px;
            color: #windowtextcolor;
            width: auto;
			position: relative:
        }

        .options {
            clear: both;
        }

        .from {
            font-size: 0.7em;
            font-weight: normal;
        }
        
        #versionbox {
            float: right;
            text-align: right;
            font-size: 0.33em;
            font-weight: normal;
            padding-right: 20px;
            letter-spacing: 0;
            color: #000000;
        }

        #description {
            background: #windowcolor;
            border-radius: 5px;
            padding: 8px;
            color: #windowtextcolor;
			float: right;
            width: 316px;
            right: 10px;
            height: 100%;
            position: relative;
        }

        #description img {
            max-width: 300px;
            clear: both;
        }

        pre {
            width: 300px !important;
            white-space: pre-wrap;
        }

        .stick {
            position: fixed !important;
            top: 0px;
            right: 18px !important;
        }

    </style>

  </head>

  <body onload="load()">

    <h1><img src="EdisonDesigner.png">&nbsp;""" + text01 + """<div id=versionbox>&nbsp</div></h1>

    <div id="description">
      &nbsp;
    </div>

    <div id="column">

      <div class="block">
        <h2>""" + text02 + """</h2>
          defaultworkbenches
      </div>

      <div class="block">
        <h2>""" + text03 + """</h2>
          recentfiles
      </div>

      <div class="block">
        <h2>""" + text04 + """</h2>
        <div id="news">news feed</div>
      </div>

      <div class="block">
        <h2>""" + text05 + """</h2>
            defaultlinks
      </div>

      <div class="block">
        <h2>""" + text06 + """</h2>
            defaultexamples
      </div>

      customblocks

    </div>
  </body>
</html>
"""

def getWorkbenches():
    return """
    <ul>
        <li><img src="EdisonDesigner.png">&nbsp;
            <a onMouseover="show('<h3>""" + text07 + """</h3> \
            <p>""" + text08 + """</p>')" 
            onMouseout="show('')" 
            href=""" + text09 + """>""" + text07 + """</a>
        </li>
        <li><img src="PartDesign.png">&nbsp;
            <a onMouseover="show('<h3>""" + text11 + """</h3> \
            <p>""" + text12 + """</p><p>""" + text10 + """ \
            :</small></p><img src=PartDesignExample.png>')" 
            onMouseout="show('')" 
            href="PartDesign.py">""" + text13 + """</a>
        </li>
        <li><img src="Mesh.png">&nbsp;
            <a onMouseover="show('<h3>""" + text14 + """</h3> \
            <p>""" + text15 + """</p><p>""" + text16 + """</p>')" 
            onMouseout="show('')" 
            href="Mesh.py">""" + text17 + """</a>
        </li>
    </ul>"""

def getLinks():
    return """
    <ul>
        <li><img src="web.png">&nbsp;
            <a onMouseover="show('<p>""" + text18 + """</p>')" 
                onMouseout="show('')"
                href="exthttp://edisondesigner.tistory.com/">""" + text19 + """</a></li>
        <li><img src="web.png">&nbsp;
            <a onMouseover="show('<p>""" + text20 + """</p>')" 
                onMouseout="show('')"
                href=ext""" + text21 + """>""" + text22 + """</a></li>
        <li><img src="web.png">&nbsp;
            <a onMouseover="show('<p>""" + text23 + """</p>')" 
                onMouseout="show('')"
                href=ext""" + text24 + """>""" + text25 + """</a></li>
        <li><img src="web.png">&nbsp;
            <a onMouseover="show('<p>""" + text26 + """</p>')" 
                onMouseout="show('')"
                href=ext""" + text27 + """>""" + text28 + """</a></li>
        <li><img src="web.png">&nbsp;
            <a onMouseover="show('<p>""" + text29 + """</p>')" 
                onMouseout="show('')"
                href="exthttp://freecad-tutorial.blogspot.com/">""" + text30 + """</a></li>
        <li><img src="web.png">&nbsp;
            <a href="exthttp://github.com/FreeCAD/FreeCAD/releases" 
               onMouseOver="show('<p>""" + text31 + """</p>')" 
               onMouseOut="show('')">""" + text32 + """</a></li>

    </ul>"""
      
def getExamples():
    return """
    <ul>
        <li>
			<img src="EdisonDesigner.png" style="width: 16px">&nbsp;
			<a href="LoadSchenkel.py"
				onMouseover="show('<img src=SchenkelExample.png>')"
				onMouseOut="show('')">""" + text33 + """
			</a>
		</li>
		
        <li><img src="EdisonDesigner.png" style="width: 16px">&nbsp;<a href="LoadPartDesignExample.py">""" + text34 + """</a></li>
		
		<li>
			<img src="EdisonDesigner.png" style="width: 16px">&nbsp;
			<a href="LoadConnectingRodExample.py"
				onMouseover="show('<img src=ConnectingRod.png>')"
				onMouseout="show('')">""" + text35 + """
			</a>
		</li>
    </ul>"""
      




def getInfo(filename):
    "returns available file information"

    def getLocalTime(timestamp):
        "returns a local time from a timestamp"       
        return time.strftime("%m/%d/%Y %H:%M:%S",time.localtime(timestamp))

    def getSize(size):
        "returns a human-readable size" 
        if size > 1024*1024:
            hsize = str(size/(1024*1024)) + "Mb"
        elif size > 1024:
            hsize = str(size/1024) + "Kb"
        else:
            hsize = str(size) + "b"
        return hsize
        
    html = '<h3>'+os.path.basename(filename)+'</h3>'
    
    if os.path.exists(filename):
        # get normal file info
        s = os.stat(filename)
        html += "<p>" + text40 + " " + getSize(s.st_size) + "<br/>"
        html += text41 + " " + getLocalTime(s.st_ctime) + "<br/>"
        html += text42 + " " + getLocalTime(s.st_mtime) + "<br/>"
        html += text43 + " " + filename + "</p>"
        # get additional info from fcstd files
        if os.path.splitext(filename)[1].upper() in [".FCSTD"]:
            zfile=zipfile.ZipFile(filename)
            files=zfile.namelist()
            # check for meta-file if it's really a EdisonDesigner document
            if files[0] == "Document.xml":
                html += "<p>EdisonDesigner Standard File</p>"
                image="thumbnails/Thumbnail.png"
                if image in files:
                    image=zfile.read(image)
                    thumbfile = tempfile.mkstemp(suffix='.png')[1]
                    thumb = open(thumbfile,"wb")
                    thumb.write(image)
                    thumb.close()
                    html += '<img src=file://'

                    html += thumbfile + '><br/>'
    else:
        html += "<p>" + text44 + "</p>"
            
    return html

def getRecentFiles():
    "returns a list of 3 latest recent files"
    rf = ED.ParamGet("User parameter:BaseApp/Preferences/RecentFiles")
    ct = rf.GetInt("RecentFiles")
    html = '<ul>'
    for i in range(3):
        if i < ct:
            mr = rf.GetString("MRU%d" % (i))
            if os.path.exists(mr):
                fn = os.path.basename(mr)
                html += '<li>'
                if mr[-5:].upper() == "FCSTD":
                    html += '<img src="ED-doc.png" style="width: 16px">&nbsp;'
                else:
                    html += '<img src="blank.png" style="width: 16px">&nbsp;'
                html += '<a '
                html += 'onMouseover="show(\''+getInfo(mr)+'\')" '
                html += 'onMouseout="show(\'\')" '
                html += 'href="LoadMRU'+str(i)+'.py">'
                html += fn
                html += '</a></li>'
    html += '</ul>'
    return html

def getFeed(url,numitems=3):
    "returns a html list with links from the given RSS feed url"
    xml = parse(urllib.urlopen(url)).getroot()
    items = []
    channel = xml.find('channel')
    for element in channel.findall('item'):
        items.append({'title': element.find('title').text,
                      'description': element.find('description').text,
                      'link': element.find('link').text})
    if len(items) > numitems:
        items = items[:numitems]
    resp = '<ul>'
    for item in items:
        descr = re.compile("style=\".*?\"").sub('',item['description'])
        descr = re.compile("alt=\".*?\"").sub('',descr)
        descr = re.compile("\"").sub('',descr)
        d1 = re.findall("<img.*?>",descr)[0]
        d2 = re.findall("<span>.*?</span>",descr)[0]
        descr = "<h3>" + item['title'] + "</h3>"
        descr += d1 + "<br/>"
        descr += d2
        resp += '<li><a onMouseover="show(\''
        resp += descr
        resp += '\')" onMouseout="show(\'\')" href="'
        resp += item['link']
        resp += '">'
        resp += item['title']
        resp += '</a></li>'
    resp += '</ul>'
    print resp
    return resp

def getCustomBlocks():
    "fetches custom html files in ED user dir"
    output = ""
    return output

def setColors(html):
    "gets theme colors from the system, and sets appropriate styles"
    defaults = {"#basecolor":"#191B26",
                "#linkcolor":"#0092E8",
                "#textcolor":"#FFFFFF",
                "#windowcolor":"#FFFFFF",
                "#windowtextcolor":"#000000"}
    try:
        palette = QtGui.qApp.palette()
    except:
        pass
    else:
        #defaults["#basecolor"] = palette.base().color().name()
        defaults["#basecolor"] = "#171A2B url(Background.jpg)"
        #defaults["#linkcolor"] = palette.link().color().name() # UGLY!!
        defaults["#textcolor"] = palette.text().color().name()
        defaults["#windowcolor"] = palette.window().color().name()
        defaults["#windowtextcolor"] = palette.windowText().color().name()
    for k,v in defaults.iteritems():
        html = html.replace(k,str(v))
    return html

def handle():
    "returns the complete html startpage"
    
    # add recent files
    recentfiles = getRecentFiles()
    html = page.replace("recentfiles",recentfiles)

    # add default workbenches
    html = html.replace("defaultworkbenches",getWorkbenches())

    # add default web links
    html = html.replace("defaultlinks",getLinks())

    # add default examples
    html = html.replace("defaultexamples",getExamples())

    # add web examples
    #html = html.replace("webexamples",getWebExamples())

    # add custom blocks
    html = html.replace("customblocks",getCustomBlocks())

    # fetches system colors
    html = setColors(html)
    
    return html

def exportTestFile():
    f = open(os.path.expanduser("~")+os.sep+"freecad-startpage.html","wb")
    f.write(handle())
    f.close()
