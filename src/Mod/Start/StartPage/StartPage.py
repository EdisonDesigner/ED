# -*- coding: utf-8 -*- 
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
    #"convenience function for the Qt translator"
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

mainTitle = translate("StartPage","EdisonDesigner")
mainTitle2 = translate("StartPage", "Start center")

#************************************************************************************************************************

subTitle01 = translate("StartPage", "새 프로젝트 생성")
# Contents in the Start a new project board
getStart = translate("StartPage", "EdisonDesigner 소개")
getStartInfo = translate("StartPage", "<p><b>EdisonDesigner</b>는 고유의 기능을 가지고 있는 워크벤치(Workbench)로 나뉘어져 있습니다.</p>"
                                      "<p>사용자는 <b>새 프로젝트 생성</b>항목에 있는 워크벤치 선택하여 모델링을 시작할 수 있습니다.</p>"
                                      "<p>각 워크벤치에 대한 자세한 설명은 EdisonDesigner 블로그를 통하여 알 수 있습니다.</p>")
getStartLink = translate("StartPage","http://edisondesigner.tistory.com/category/Manuals")

sketcher = translate("StartPage", "Sketcher")
sketcherTitle = translate("StartPage", "2D 스케치 생성")
sketcherInfo = translate("StartPage", "<p><b>Sketcher</b>는 오직 2D 스케치를 생성하기 위한 워크벤치입니다.</p>"
                                      "<p>사용자는 Sketcher 워크벤치를 이용하여 점, 선, 호, 원과 같은 단순한 스케치뿐만 아니라 "
                                      "연속선(Polyline), 다각형(Polygon), 타원을 손쉽게 그릴 수 있습니다.</p>"
                                      "<p>또한, 논리(Logical)/치수(Dimensional) 구속조건을 통해 스케치가 변경되지 않도록 정의할 수 있습니다.</p>")
sketcherFlow = translate("StartPage", "Sketcher 사용 예:")

partDesign = translate("StartPage", "Part Design")
partDesignTitle = translate("StartPage", "피처 기반(Feature-based) 3D 솔리드 모델 생성")
partDesignInfo = translate("StartPage", "<p><b>Part Design</b>은 2D 스케치를 이용하여 복잡한 3D 솔리드 모델을 생성할 수 있는 워크벤치입니다.</p>"
                                        "<p>3D 솔리드 모델을 생성하는 Pad, pocket, revolve, groove 피처와 생성된 3D 솔리드 모델을 수정하는 "
                                        "fillet, chamfer, mirror, pattern을 사용할 수 있습니다.</p>")
partDesignFlow = translate("StartPage", "Part Design 사용 예:")

part = translate("StartPage", "Part")
partTitle = translate("StartPage", "CSG 기반 3D 솔리드 모델과 3D surface 모델 생성")
partInfo = translate("StartPage", "<p><b>Part</b>는 두가지 모델링 방법을 제공합니다.</p>"
                                  "<ol><li>CSG 모델링</li><li>Surface 모델링</li></ol>"
                                  "<p>CSG 모델링은 육면체, 원뿔, 구와 같은 미리 정의된 기본 모양 요소(Primitives)를 이용하여 3D 솔리드 모델을 생성하고"
                                  "불린(Boolean)연산을 통해 새로운 3D 솔리드 모델을 만드는 방법입니다. 이때, 기본 모양 요소와 불린연산은 트리 구조로 기록합니다.</p>"
                                  "<p>Surface 모델링은 3차원 공간에서 점과 선을 이용하여 surface를 생성할 수 있습니다.</p>")
partFlow = translate("StartPage", "Part 사용 예:")

mesh = translate("StartPage", "Mesh Design")
meshTitle = translate("StartPage", "Mesh 모델 불러오기(Import)/내보내기(Export)")
meshInfo = translate("StartPage", "<p><b>Mesh Workbench</b>는 mesh 객체를 다루기 위한 워크벤치입니다.</p>"
                                  "<p>Mesh 모델은 Part Design과 Part에서 생성된 모델보다는 단순하지만 다른 프로그램에서 생성된 모델을"
                                  "불러오거나 내보내는 것이 상대적으로 편리합니다.<br />현재 Mesh Design 워크벤치는 두가지 기능을 제공합니다.</p>"
                                  "<ol><li>Mesh import</li><li>Mesh export</li></ol>")
meshFlow = translate("StartPage", "Mesh 사용 예:")

# ************************************************************************************************************************

subTitle02 = translate("StartPage", "최근 사용 문서")

# ************************************************************************************************************************

subTitle03 = translate("StartPage", "EDISON center 공지사항")
readAllCommits = translate("StartPage","See all commits")

# ************************************************************************************************************************

subTitle04 = translate("StartPage", "관련 웹 사이트")
# Contents in the on the web board
homepage = translate("StartPage", "EDISON과제 홈페이지")
homepageInfo = translate("StartPage", "<p>EDISON과제의 주관기관인 KISTI 홈페이지입니다.</p>"
                                      "<p>홈페이지를 통해 EDISON 소식, EdisonDesigner, 사용자 메뉴얼과 EDISON과제의 다른 전문센터에서 "
                                      "제공하는 다양한 프로그램을 이용할 수 있습니다.</p>")

manual = translate("StartPage", "사용자 메뉴얼(국문)")
manualInfo = translate("StartPage", "<p>KAIST iCAD 연구실에서 작성한 EdisonDesigner의 사용자 메뉴얼입니다.</p>")
manualLink = translate("StartPage", "https://www.edison.re.kr/documents/23849/439421/ED014%ED%95%9C%EA%B8%80.pdf/695a7613-6059-478f-9f53-930d0569e58f")

tutorial = translate("StartPage", "튜토리얼")
tutorialInfo = translate("StartPage", "<p>EdisonDesigner의 사용법에 대한 튜토리얼을 제공합니다.</p>"
                                      "<p>주어진 예제 <b>도면</b>을 이용하여 모델링을 하는 방법과 <b>동영상</b>을 제공하고 있습니다.</p>")

tutorialBlog = translate("StartPage", "EdisonDesigner 블로그")
tutorialBlogInfo = translate("StartPage", "<p>EdisonDesigner의 공식 블로그입니다.</p>"
                                          "<p>EdisonDesigner의 업데이트 소식, 변경사항, 메뉴얼 등 많은 정보를 제공하는 사이트입니다.</p>")

pythonRes = translate("StartPage", "매크로와 API를 위한 파이썬(영문)")
pythonResInfo = translate("StartPage", "<p>EdisonDesigner는 오픈 소스 CAD 프로그램인 <b>FreeCAD</b>를 활용하여 개발되었습니다.</p>"
                                       "<p>현재 FreeCAD에서 제공하는 매크로와 API를 사용하고 있습니다. 이 링크는 FreeCAD에서 제공하는"
                                       "매크로 활용법과 API문서를 안내하는 페이지입니다.</p>")


# ************************************************************************************************************************

subTitle05 = translate("StartPage", "예제 파일")
# Contents in the example board
ex01 = translate("StartPage", "Schenkel STEP file")
ex01Info = translate("StartPage", "STEP 파일 불러오기 예제(FreeCAD에서 제공)")

ex02 = translate("StartPage", "Load a PartDesign example")
ex02Info = translate("StartPage", "파트모델 만들기 예제(FreeCAD에서 제공)")

ex03 = translate("StartPage", "셀카봉 설계 예제")
ex03Info = translate("StartPage", "Part Design과 Part워크벤치를 이용한 셀카봉 설계 예제")

# ************************************************************************************************************************

versionCheck_update = translate("StartPage","최신 버전의 EdisonDesigner를 사용하고 있습니다.")
versionCheck_needUpdate = translate("StartPage","새로운 버전의 EdisonDesigner가 있습니다.")

#************************************************************************************************************************

message01 = translate("StartPage","Close this window after opening or creating a file")
message02 = translate("StartPage","Don't show me this window again next time")

text33 = translate("StartPage","file size:")
text34 = translate("StartPage","creation time:")
text35 = translate("StartPage","last modified:")
text36 = translate("StartPage","location:")
text37 = translate("StartPage","File not found")

# get ED version

v = ED.Version()
vmajor = v[0]
vminor = v[1]
vbuild = v[2].split(" ")[0]


# here is the html page skeleton

page = """
<!DOCTYPE html>
<html>
<head>
    <title>EdisonDesigner - Start page</title>
    <meta charset="UTF-8">
    
    <style>
        body {
            background: url(background.jpg);
            font-family: "Consolas", "Courier New", "monospace";
            font-size: 12px;
        }

        a {
            color: #2E9AFE;
            font-weight: bold;
            font-size: 1.3em;
            text-decoration: none;
            vertical-align: middle;
        }

        a:hover {
            color: white;
            background: #2E9AFE;
            border-radius: 5px;
        }

        p {
            text-align: justify;
            font-size: larger;
        }

        h1 {
            font-size: 2.5em;
            letter-spacing: 1px;
            padding: 10px 0 0 50px;
            color: #000000;
        }

        h1 img {
            width: 32px;
            height: 32px;
            vertical-align: top;
        }

        h2 {
            font-size: 1.2em;
        }

        ul {
            list-style-type: none;
            padding: 0;
        }

        #column {
            margin: 0 600px 0 10px;
        }

        #column img {
            max-width: 16px;
            vertical-align: middle;
        }

        .block {
            background: #E6E6E6;
            border-radius: 5px;
            padding: 8px;
            margin-bottom: 10px;
            color: #000000;
            width: auto;
        }

        #description {
            background: #E6E6E6;
            border-radius: 5px;
            padding: 8px;
            color: #000000;
            float: right;
            width: 566px;
            right: 10px;
            height: auto;
            position: relative;
        }

        #description img {
            max-width: 500px;
            display: block;
            margin-left: auto;
            margin-right: auto;
            clear: both;
        }

        #versionbox {
            float: right;
            text-align: right;
            font-size: 0.33em;
            font-weight: normal;
            padding-right: 20px;
            letter-spacing: 0;
            color: #ffffff;
        }

        pre {
        width: 300px !important;
        white-space: pre-wrap;
        }

    </style>
</head>

<body>
    <h1>
        <img src="ED.png" style="width: 32px">&nbsp""" + mainTitle + """&nbsp""" + vmajor + """&#46;""" + vminor + """&nbsp""" + mainTitle2 + """
        <div id="versionbox">&nbsp</div>
    </h1>

    <div id="description"></div>

    <div id="column">

      <div class="block">
        <h2>""" + subTitle01 + """</h2>
          defaultworkbenches
      </div>

      <div class="block">
        <h2>""" + subTitle02 + """</h2>
          recentfiles
      </div>

      <div class="block">
        <h2>""" + subTitle03 + """</h2>
        <div id="news">news feed</div>
      </div>

      <div class="block">
        <h2>""" + subTitle04 + """</h2>
            defaultlinks
      </div>

      <div class="block">
        <h2>""" + subTitle05 + """</h2>
            defaultexamples
      </div>
    </div>
  </body>
</html>
"""

def getWorkbenches():
    return """
    <ul>
        <li>
            <img src="blank.png">&nbsp;
            <a onMouseover="show('<h3>""" + getStart + """</h3> \
            <p>""" + getStartInfo + """</p>')"
            onMouseout="show('')"
            href=ext""" + getStartLink + """>""" + getStart + """</a>
        </li>
        <li>
            <img src="Sketcher.png">&nbsp;
            <a onMouseover="show('<h3>""" + sketcherTitle + """</h3> \
            <p>""" + sketcherInfo + """</p><p>""" + sketcherFlow + """ :</p>\
            <img src=SketcherFlow.png>')"
            onMouseout="show('')"
            href="Sketcher.py">""" + sketcher + """</a>
        </li>
        <li>
            <img src="PartDesign.png">&nbsp;
            <a onMouseover="show('<h3>""" + partDesignTitle + """</h3> \
            <p>""" + partDesignInfo + """</p><p>""" + partDesignFlow + """ :</p>\
            <img src=PartDesignFlow.png>')"
            onMouseout="show('')"
            href="PartDesign.py">""" + partDesign + """</a>
        </li>
        <li>
            <img src="Part.png">&nbsp;
            <a onMouseover="show('<h3>""" + partTitle + """</h3> \
            <p>""" + partInfo + """</p><p>""" + partFlow + """ :</p>\
            <img src=PartFlow.png>')"
            onMouseout="show('')"
            href="Part.py">""" + part + """</a>
        </li>
        <li>
            <img src="Mesh.png">&nbsp;
            <a onMouseover="show('<h3>""" + meshTitle + """</h3> \
            <p>""" + meshInfo + """</p><p>""" + meshFlow + """ :</p>\
            <img src=MeshFlow.png>')"
            onMouseout="show('')"
            href="Mesh.py">""" + mesh + """</a>
        </li>
    </ul>"""


def getRecentFiles():
    # returns a list of 3 latest recent files

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
                    html += '<img src="ED.png" style="width: 16px">&nbsp;'
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


def getInfo(filename):
    # returns available file information

    def getLocalTime(timestamp):
        "returns a local time from a timestamp"
        return time.strftime("%m/%d/%Y %H:%M:%S", time.localtime(timestamp))

    def getSize(size):
        "returns a human-readable size"
        if size > 1024 * 1024:
            hsize = str(size / (1024 * 1024)) + "Mb"
        elif size > 1024:
            hsize = str(size / 1024) + "Kb"
        else:
            hsize = str(size) + "b"
        return hsize

    html = '<h3>' + os.path.basename(filename) + '</h3>'

    if os.path.exists(filename):
        # get normal file info
        s = os.stat(filename)
        html += "<p>" + text33 + " " + getSize(s.st_size) + "<br/>"
        html += text34 + " " + getLocalTime(s.st_ctime) + "<br/>"
        html += text35 + " " + getLocalTime(s.st_mtime) + "<br/>"
        html += "<span>" + text36 + " " + filename + "</span></p>"
        # get additional info from fcstd files
        if os.path.splitext(filename)[1].upper() in [".FCSTD"]:
            zfile = zipfile.ZipFile(filename)
            files = zfile.namelist()
            # check for meta-file if it's really a ED document
            if files[0] == "Document.xml":
                html += "<p>EdisonDesigner Standard File</p>"
                image = "thumbnails/Thumbnail.png"
                if image in files:
                    image = zfile.read(image)
                    thumbfile = tempfile.mkstemp(suffix='.png')[1]
                    thumb = open(thumbfile, "wb")
                    thumb.write(image)
                    thumb.close()
                    html += '<img src=file://'

                    html += thumbfile + '><br/>'
    else:
        html += "<p>" + text37 + "</p>"

    return html


def getLinks():
    return """
    <ul>
        <li>
            <img src="web.png">&nbsp;
            <a onMouseover="show('<p>""" + homepageInfo + """</p>')"
                onMouseout="show('')"
                href="exthttp://design.edison.re.kr">""" + homepage + """</a></li>
        <li><img src="web.png">&nbsp;
            <a onMouseover="show('<p>""" + manualInfo + """</p>')"
                onMouseout="show('')"
                href=ext""" + manualLink + """>""" + manual + """</a></li>
        <li><img src="web.png">&nbsp;
            <a onMouseover="show('<p>""" + tutorialInfo + """</p>')"
                onMouseout="show('')"
                href="exthttp://edisondesigner.tistory.com/category/Tutorials">""" + tutorial + """</a></li>
        <li><img src="web.png">&nbsp;
            <a onMouseover="show('<p>""" + tutorialBlogInfo + """</p>')"
                onMouseout="show('')"
                href="exthttp://edisondesigner.tistory.com">""" + tutorialBlog + """</a></li>
        <li><img src="web.png">&nbsp;
            <a onMouseover="show('<p>""" + pythonResInfo + """</p>')"
                onMouseout="show('')"
                href="exthttps://www.freecadweb.org/wiki/Category:API">""" + pythonRes + """</a></li>
    </ul>"""



def getExamples():
    return """
    <ul>
        <li>
            <img src="ED.png" style="width: 16px">&nbsp;
            <a href="LoadSchenkel.py"
                onMouseover="show('<p>""" + ex01Info + """</p> \
                                   <img src=SchenkelEx.png>')"
                onMouseout="show('')">""" + ex01 + """
            </a>
        </li>
        
        <li>
            <img src="ED.png" style="width: 16px">&nbsp;
            <a href="LoadPartDesignExample.py"
                onMouseover="show('<p>""" + ex02Info + """</p> \
                                   <img src=PartDesignEx.png>')"
                onMouseout="show('')">""" + ex02 + """
            </a>
        </li>
        <li>
            <img src="ED.png" style="width: 16px">&nbsp;
            <a href="LoadSelfieStickExample.py"
                onMouseover="show('<p>""" + ex03Info + """</p> \
                                   <img src=SelfiestickEx.png>')"
                onMouseout="show('')">""" + ex03 + """
            </a>
        </li>
    </ul>
"""



def handle():
    # returns the complete html startpage
    
    # add recent files
    recentfiles = getRecentFiles()
    html = page.replace("recentfiles",recentfiles)

    # add default workbenches
    html = html.replace("defaultworkbenches",getWorkbenches())

    # add default web links
    html = html.replace("defaultlinks",getLinks())

    # add default examples
    html = html.replace("defaultexamples",getExamples())

    
    return html

def exportTestFile():
    f = open(os.path.expanduser("~")+os.sep+"EdisonDesigner-startpage.html","wb")
    f.write(handle())
    f.close()
