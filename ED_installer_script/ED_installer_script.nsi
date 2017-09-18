# Include Mordern UI header
!include "MUI2.nsh"
!include "LogicLib.nsh"

# 프로그램 버전 정보를 포함
!include Version.nsi

# 프로그램 명칭 설정
!define APPNAME				"EdisonDesigner"
!define EXEName				"ED"
!define PUPNAME				"KAIST iCAD laboratory"
!define DESCRIPTION			"A freeware CAD system for education"
!define HELPURL				"http://edisondesigner.tistory.com"
!define ABOUTURL			"http://edisondesigner.tistory.com"
!define UPDATEURL			"http://edisondesigner.tistory.com"


!define FULLNAME "${APPNAME} ${VERSIONMAJOR}.${VERSIONMINOR}"

# 프로그램 실행 권한 설정
RequestExecutionLevel admin

# 프로그램 설치 경로 설정
InstallDir "$PROGRAMFILES\${FULLNAME}"

# 인스톨러와 언인스톨러의 이름 설정
Name "${FULLNAME}"

# 최종 인스톨러 파일 이름
OutFile "${FULLNAME}_x86_setup.exe"

!define MUI_ABORTWARNING
!define MUI_ICON	"Install_icon.ico"
!define MUI_UNICON	"Install_icon.ico"

# -------------------------------------------------------
# 인스톨러 실행 권한이 admin인지 확인
Function checkAdmin
	UserInfo::GetAccountType
	pop $0

	${If} $0 != "admin"
		MessageBox MB_ICONSTOP \
			"관리자권한이 필요합니다. 프로그램을 우클릭하여 관리자권한으로 실행해주시기 바랍니다."
		QUIT
	${EndIf}
FunctionEnd

# -------------------------------------------------------

Function .onInit
	# 인스톨러 시작 시, 화면에 나타나는 splash 이미지 설정
	File /oname=splash.bmp "splash.bmp"
    splash::show 1000 splash

	Call checkAdmin
FunctionEnd

# -------------------------------------------------------
# Pages
# 인스톨러 시작화면 문구
;!define			MUI_WELCOMEFINISHPAGE_BITMAP "${NSISDIR}\Contrib\Graphics\Wizard\orange.bmp"
!define 		WELCOME_TITLE "${FULLNAME} 설치를 시작합니다."
!define 		MUI_WELCOMEPAGE_TITLE '${WELCOME_TITLE}'
!insertmacro 	MUI_PAGE_WELCOME

!insertmacro 	MUI_PAGE_LICENSE "License.rtf"					 # 저작권 페이지
!insertmacro 	MUI_PAGE_COMPONENTS								 # 컴포넌트 페이지
!insertmacro 	MUI_PAGE_DIRECTORY								 # 설치 경로 페이지
!insertmacro 	MUI_PAGE_INSTFILES								 # 설치 상황 페이지

!define			MUI_FINISHPAGE_RUN "$INSTDIR\bin\${APPNAME}.exe" # 설치 종료 후, 프로그램 실행
!insertmacro    MUI_PAGE_FINISH                             	 # 설치 종료 후, 마지막 안내 페이지

!insertmacro    MUI_UNPAGE_WELCOME                  			 # 언인스톨 시작 문구
!insertmacro 	MUI_UNPAGE_CONFIRM								 # 언인스톨??
!insertmacro 	MUI_UNPAGE_INSTFILES							 # 언인스톨 진행 상황


# -------------------------------------------------------
# Languages

!insertmacro 	MUI_LANGUAGE "Korean"				# 언어 설정

# -------------------------------------------------------
# 설치파일 버전 정보

VIProductVersion "${APP_VI_PRODUCT_VER}"
VIAddVersionKey /LANG=${LANG_KOREAN} "FileDescription" "${APPNAME} 설치파일"
VIAddVersionKey /LANG=${LANG_KOREAN} "ProductName"     "${APPNAME}"
VIAddVersionKey /LANG=${LANG_KOREAN} "ProductVersion"  "${VERSIONMAJOR}.${VERSIONMINOR}.${VERSIONBUILD}"
VIAddVersionKey /LANG=${LANG_KOREAN} "CompanyName"     "${PUPNAME}"
VIAddVersionKey /LANG=${LANG_KOREAN} "LegalCopyright"  "Copyright 2014-2016. iCAD Lab. all rights reserved"
VIAddVersionKey /LANG=${LANG_KOREAN} "FileVersion"     "${APP_VI_PRODUCT_VER}"

# -------------------------------------------------------
# 설치 및 삭제 내용 자세히 보기 여부(hide|show|nevershow)
ShowInstDetails     show
ShowUninstDetails   show

# -------------------------------------------------------

Section "EdisonDesigner(Required)" EdisonDesigner

	# VS 2013 재배포패키지 설치 유/무 확인
	Call checkVCRedist

	# bin, data, Mod, Addons 폴더 설치
	# 1. bin folder
	SetOutPath $INSTDIR
	SetCompress auto
    DetailPrint "Extracting bin package..."
	SetDetailsPrint listOnly

	File bin.7z
	SetDetailsPrint both
	Nsis7z::ExtractWithDetails "bin.7z" "Installing bin package %s..."

	Delete "$OUTDIR\bin.7z"

	# --------------------------------------------------------------------
	# 2. Data folder
  	SetOutPath $INSTDIR
	SetCompress auto
	DetailPrint "Extracting Data package..."
	SetDetailsPrint listonly

	File Data.7z
	SetDetailsPrint both
	Nsis7z::ExtractWithDetails "Data.7z" "Installing Data package %s..."

	Delete "$OUTDIR\Data.7z"

	# --------------------------------------------------------------------
	# 3. Mod folder
	SetOutPath $INSTDIR
	SetCompress auto
	DetailPrint "Extracting Mod package..."
	SetDetailsPrint listonly

	File Mod.7z
	SetDetailsPrint both
	Nsis7z::ExtractWithDetails "Mod.7z" "Installing Mod package %s..."

	Delete "$OUTDIR\Mod.7z"

	# --------------------------------------------------------------------
	# 4. Addons folder
	SetOutPath $INSTDIR
	SetCompress auto
	DetailPrint "Extracting Addons package..."
	SetDetailsPrint listonly

	File Addons.7z
	SetDetailsPrint both
	Nsis7z::ExtractWithDetails "Addons.7z" "Installing Addons package %s..."

	Delete "$OUTDIR\Addons.7z"

	# --------------------------------------------------------------------

	
	# 설치 폴더에 EdisonDesigner 바로가기 생성
	CreateShortcut "$INSTDIR\${APPNAME}.lnk" "$INSTDIR\bin\ED.exe" "" ""

	# 프로그램 추가/제거를 위한 레지스트리 등록
	Call setReg

	# Create uninstaller
	WriteUninstaller "$INSTDIR\Uninstall.exe"

SectionEnd

# -------------------------------------------------------
# 시작메뉴 및 바로가기 생성 section

Section "Add to start menu" AddStartMenu

	createDirectory	"$SMPROGRAMS\${FULLNAME}"
	createShortCut	"$SMPROGRAMS\${FULLNAME}\${APPNAME}.lnk" "$INSTDIR\bin\ED.exe" "" ""

SectionEnd

# -------------------------------------------------------
# 바탕화면 바로가기 생성 section

Section "Add to desktop icon" AddDesktop

	CreateShortCut  "$DESKTOP\${APPNAME}.lnk" "$INSTDIR\bin\ED.exe" "" ""

SectionEnd

# -------------------------------------------------------
# 각 section에 대한 설명

	#Language strings
	LangString EdisonDesigner ${LANG_KOREAN} \
		"EdisonDesigner에 가장 필수요소입니다."

	LangString AddStartMenu ${LANG_KOREAN} \
		"시작메뉴에 프로그램 그룹을 생성합니다."

	LangString AddDesktop ${LANG_KOREAN} \
		"바탕화면에 바로가기를 생성합니다."

	#Assign language strings to sections
	!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
		!insertmacro MUI_DESCRIPTION_TEXT ${EdisonDesigner} $(EdisonDesigner)
		!insertmacro MUI_DESCRIPTION_TEXT ${AddStartMenu}	$(AddStartMenu)
		!insertmacro MUI_DESCRIPTION_TEXT ${AddDesktop}		$(AddDesktop)
	!insertmacro MUI_FUNCTION_DESCRIPTION_END

# -------------------------------------------------------
# Uninstaller section

# Uninstaller를 시작할 때 뜨는 경고문
Function un.onInit
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "${FULLNAME}을(를) 제거하시겠습니까?" IDYES +2
  Abort
FunctionEnd

# Uninstaller가 끝나고 나서 뜨는 안내문
Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "${FULLNAME}는(은) 완전히 제거되었습니다."
FunctionEnd

Section "Uninstall"

	# 시작메뉴의 lnk 파일 삭제
	Delete "$SMPROGRAMS\${FULLNAME}\${APPNAME}.lnk"

	# 시작메뉴의 폴더 삭제
	RMDir "$SMPROGRAMS\${FULLNAME}"

	# 바탕화면의 실행파일 삭제
	Delete "$DESKTOP\${APPNAME}.lnk"

	# 설치폴더의 바로가기 삭제
	Delete "$INSTDIR\${APPNAME}.lnk"

	# EdisonDesigner에 있는 폴더 삭제
	RMDir /r "$INSTDIR\bin"
	RMDir /r "$INSTDIR\Data"
	RMDir /r "$INSTDIR\Mod"
	RMDir /r "$INSTDIR\Addons"

    Delete "$INSTDIR\vcredist_x86_vs2013.exe"
    Delete "$INSTDIR\vcredist_x64_vs2013.exe"

	Delete "$INSTDIR\Uninstall.exe"

	RMDir "$INSTDIR"

	# 레지스트리 삭제
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${FULLNAME}"

SectionEnd

# -------------------------------------------------------
# Functions
Var GetInstalledSize.total

Function checkVCRedist

	# 사용자 컴퓨터의 Windows OS bit를 확인하여
	# bit에 맞는 VS2013 재배포 패키지를 설치
	System::Call "kernel32::GetCurrentProcess() i .s"
	System::Call "kernel32::IsWow64Process(i s, *i .r0)"

	# Windows 32bit인 경우,
	${if} $0 == '0'
		ReadRegDword $R1 HKLM "SOFTWARE\Wow6432Node\Microsoft\VisualStudio\12.0\VC\Runtimes\x86" "Installed"

		# Visual studio 2013 재배포패치키 설치됨
		${if} $R1 == '1'
			DetailPrint "이미 Visual studio 2013 32bit 용 재배포패키지가 설치되어 있습니다."

		${Else}
			DetailPrint "Visual studio 2013 32bit 용 재배포패키지가 설치되어 있지 않습니다. 설치를 진행합니다."
			MessageBox MB_OK "Visual studio 2013 32bit 용 재배포패키지가 설치되어 있지 않아 재배포패키지를 먼저 설치합니다."
			SetOutPath $INSTDIR
			File "vcredist_x86_vs2013.exe"
			ExecWait '"$INSTDIR\vcredist_x86_vs2013.exe"'
			Delete "$OUTDIR\vcredist_x86_vs2013.exe"
		${EndIf}

	# Windows 64bit인 경우,
	${ElseIf} $0 == '1'
		ReadRegDword $R2 HKLM "SOFTWARE\Wow6432Node\Microsoft\VisualStudio\12.0\VC\Runtimes\x64" "Installed"

		# Visual studio 2013 재배포패치키 설치됨
		${if} $R2 == '1'
			DetailPrint "이미 Visual studio 2013 64bit 용 재배포패키지가 설치되어 있습니다."

		${Else}
			DetailPrint "Visual studio 2013 64bit 용 재배포패키지가 설치되어 있지 않습니다. 설치를 진행합니다."
			MessageBox MB_OK "Visual studio 2013 64bit 용 재배포패키지가 설치되어 있지 않아 재배포패키지를 먼저 설치합니다."
			SetOutPath $INSTDIR
			File "vcredist_x64_vs2013.exe"
			ExecWait '"$INSTDIR\vcredist_x64_vs2013.exe"'
			Delete "$OUTDIR\vcredist_x64_vs2013.exe"
		${EndIf}
	${EndIf}

FunctionEnd


Function setReg

	Call estimatedSize

	# 레지스트리 등록: 프로그램 추가/제거를 위해서 수행
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${FULLNAME}" "DisplayName"			"${FULLNAME} - ${DESCRIPTION}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${FULLNAME}" "UninstallString"		'"$INSTDIR\Uninstall.exe"'
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${FULLNAME}" "QuietUninstallString"	'"$INSTDIR\Uninstall.exe" /S'
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${FULLNAME}" "InstallLocation"		"$INSTDIR"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${FULLNAME}" "DisplayIcon"			"$INSTDIR\bin\EdisonDesigner.exe"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${FULLNAME}" "HelpLink"				"${HELPURL}"
   	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${FULLNAME}" "URLInfoAbout"			"${ABOUTURL}"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${FULLNAME}" "URLUpdateInfo"			"${UPDATEURL}"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${FULLNAME}" "Publisher"				"${PUPNAME}"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${FULLNAME}" "DisplayVersion"			"${VERSIONMAJOR}.${VERSIONMINOR}.${VERSIONBUILD}"
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${FULLNAME}" "VersionMajor"			${VERSIONMAJOR}
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${FULLNAME}" "VersionMinor"			${VERSIONMINOR}
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${FULLNAME}" "EstimatedSize"		$GetInstalledSize.total

FunctionEnd


Function estimatedSize
	Push $0
	Push $1

	StrCpy $GetInstalledSize.total 0
	${ForEach} $1 0 256 + 1
		${if} ${SectionIsSelected} $1
			SectionGetSize $1 $0
			IntOp $GetInstalledSize.total $GetInstalledSize.total + $0
		${Endif}

		; Error flag is set when an out-of-bound section is referenced
		${if} ${errors}
			${break}
		${Endif}
	${Next}

	ClearErrors
	Pop $1
	Pop $0
	IntFmt $GetInstalledSize.total "0x%08X" $GetInstalledSize.total
	Push $GetInstalledSize.total

FunctionEnd