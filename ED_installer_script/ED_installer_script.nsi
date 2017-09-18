# Include Mordern UI header
!include "MUI2.nsh"
!include "LogicLib.nsh"

# ���α׷� ���� ������ ����
!include Version.nsi

# ���α׷� ��Ī ����
!define APPNAME				"EdisonDesigner"
!define EXEName				"ED"
!define PUPNAME				"KAIST iCAD laboratory"
!define DESCRIPTION			"A freeware CAD system for education"
!define HELPURL				"http://edisondesigner.tistory.com"
!define ABOUTURL			"http://edisondesigner.tistory.com"
!define UPDATEURL			"http://edisondesigner.tistory.com"


!define FULLNAME "${APPNAME} ${VERSIONMAJOR}.${VERSIONMINOR}"

# ���α׷� ���� ���� ����
RequestExecutionLevel admin

# ���α׷� ��ġ ��� ����
InstallDir "$PROGRAMFILES\${FULLNAME}"

# �ν��緯�� ���ν��緯�� �̸� ����
Name "${FULLNAME}"

# ���� �ν��緯 ���� �̸�
OutFile "${FULLNAME}_x86_setup.exe"

!define MUI_ABORTWARNING
!define MUI_ICON	"Install_icon.ico"
!define MUI_UNICON	"Install_icon.ico"

# -------------------------------------------------------
# �ν��緯 ���� ������ admin���� Ȯ��
Function checkAdmin
	UserInfo::GetAccountType
	pop $0

	${If} $0 != "admin"
		MessageBox MB_ICONSTOP \
			"�����ڱ����� �ʿ��մϴ�. ���α׷��� ��Ŭ���Ͽ� �����ڱ������� �������ֽñ� �ٶ��ϴ�."
		QUIT
	${EndIf}
FunctionEnd

# -------------------------------------------------------

Function .onInit
	# �ν��緯 ���� ��, ȭ�鿡 ��Ÿ���� splash �̹��� ����
	File /oname=splash.bmp "splash.bmp"
    splash::show 1000 splash

	Call checkAdmin
FunctionEnd

# -------------------------------------------------------
# Pages
# �ν��緯 ����ȭ�� ����
;!define			MUI_WELCOMEFINISHPAGE_BITMAP "${NSISDIR}\Contrib\Graphics\Wizard\orange.bmp"
!define 		WELCOME_TITLE "${FULLNAME} ��ġ�� �����մϴ�."
!define 		MUI_WELCOMEPAGE_TITLE '${WELCOME_TITLE}'
!insertmacro 	MUI_PAGE_WELCOME

!insertmacro 	MUI_PAGE_LICENSE "License.rtf"					 # ���۱� ������
!insertmacro 	MUI_PAGE_COMPONENTS								 # ������Ʈ ������
!insertmacro 	MUI_PAGE_DIRECTORY								 # ��ġ ��� ������
!insertmacro 	MUI_PAGE_INSTFILES								 # ��ġ ��Ȳ ������

!define			MUI_FINISHPAGE_RUN "$INSTDIR\bin\${APPNAME}.exe" # ��ġ ���� ��, ���α׷� ����
!insertmacro    MUI_PAGE_FINISH                             	 # ��ġ ���� ��, ������ �ȳ� ������

!insertmacro    MUI_UNPAGE_WELCOME                  			 # ���ν��� ���� ����
!insertmacro 	MUI_UNPAGE_CONFIRM								 # ���ν���??
!insertmacro 	MUI_UNPAGE_INSTFILES							 # ���ν��� ���� ��Ȳ


# -------------------------------------------------------
# Languages

!insertmacro 	MUI_LANGUAGE "Korean"				# ��� ����

# -------------------------------------------------------
# ��ġ���� ���� ����

VIProductVersion "${APP_VI_PRODUCT_VER}"
VIAddVersionKey /LANG=${LANG_KOREAN} "FileDescription" "${APPNAME} ��ġ����"
VIAddVersionKey /LANG=${LANG_KOREAN} "ProductName"     "${APPNAME}"
VIAddVersionKey /LANG=${LANG_KOREAN} "ProductVersion"  "${VERSIONMAJOR}.${VERSIONMINOR}.${VERSIONBUILD}"
VIAddVersionKey /LANG=${LANG_KOREAN} "CompanyName"     "${PUPNAME}"
VIAddVersionKey /LANG=${LANG_KOREAN} "LegalCopyright"  "Copyright 2014-2016. iCAD Lab. all rights reserved"
VIAddVersionKey /LANG=${LANG_KOREAN} "FileVersion"     "${APP_VI_PRODUCT_VER}"

# -------------------------------------------------------
# ��ġ �� ���� ���� �ڼ��� ���� ����(hide|show|nevershow)
ShowInstDetails     show
ShowUninstDetails   show

# -------------------------------------------------------

Section "EdisonDesigner(Required)" EdisonDesigner

	# VS 2013 �������Ű�� ��ġ ��/�� Ȯ��
	Call checkVCRedist

	# bin, data, Mod, Addons ���� ��ġ
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

	
	# ��ġ ������ EdisonDesigner �ٷΰ��� ����
	CreateShortcut "$INSTDIR\${APPNAME}.lnk" "$INSTDIR\bin\ED.exe" "" ""

	# ���α׷� �߰�/���Ÿ� ���� ������Ʈ�� ���
	Call setReg

	# Create uninstaller
	WriteUninstaller "$INSTDIR\Uninstall.exe"

SectionEnd

# -------------------------------------------------------
# ���۸޴� �� �ٷΰ��� ���� section

Section "Add to start menu" AddStartMenu

	createDirectory	"$SMPROGRAMS\${FULLNAME}"
	createShortCut	"$SMPROGRAMS\${FULLNAME}\${APPNAME}.lnk" "$INSTDIR\bin\ED.exe" "" ""

SectionEnd

# -------------------------------------------------------
# ����ȭ�� �ٷΰ��� ���� section

Section "Add to desktop icon" AddDesktop

	CreateShortCut  "$DESKTOP\${APPNAME}.lnk" "$INSTDIR\bin\ED.exe" "" ""

SectionEnd

# -------------------------------------------------------
# �� section�� ���� ����

	#Language strings
	LangString EdisonDesigner ${LANG_KOREAN} \
		"EdisonDesigner�� ���� �ʼ�����Դϴ�."

	LangString AddStartMenu ${LANG_KOREAN} \
		"���۸޴��� ���α׷� �׷��� �����մϴ�."

	LangString AddDesktop ${LANG_KOREAN} \
		"����ȭ�鿡 �ٷΰ��⸦ �����մϴ�."

	#Assign language strings to sections
	!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
		!insertmacro MUI_DESCRIPTION_TEXT ${EdisonDesigner} $(EdisonDesigner)
		!insertmacro MUI_DESCRIPTION_TEXT ${AddStartMenu}	$(AddStartMenu)
		!insertmacro MUI_DESCRIPTION_TEXT ${AddDesktop}		$(AddDesktop)
	!insertmacro MUI_FUNCTION_DESCRIPTION_END

# -------------------------------------------------------
# Uninstaller section

# Uninstaller�� ������ �� �ߴ� ���
Function un.onInit
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "${FULLNAME}��(��) �����Ͻðڽ��ϱ�?" IDYES +2
  Abort
FunctionEnd

# Uninstaller�� ������ ���� �ߴ� �ȳ���
Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "${FULLNAME}��(��) ������ ���ŵǾ����ϴ�."
FunctionEnd

Section "Uninstall"

	# ���۸޴��� lnk ���� ����
	Delete "$SMPROGRAMS\${FULLNAME}\${APPNAME}.lnk"

	# ���۸޴��� ���� ����
	RMDir "$SMPROGRAMS\${FULLNAME}"

	# ����ȭ���� �������� ����
	Delete "$DESKTOP\${APPNAME}.lnk"

	# ��ġ������ �ٷΰ��� ����
	Delete "$INSTDIR\${APPNAME}.lnk"

	# EdisonDesigner�� �ִ� ���� ����
	RMDir /r "$INSTDIR\bin"
	RMDir /r "$INSTDIR\Data"
	RMDir /r "$INSTDIR\Mod"
	RMDir /r "$INSTDIR\Addons"

    Delete "$INSTDIR\vcredist_x86_vs2013.exe"
    Delete "$INSTDIR\vcredist_x64_vs2013.exe"

	Delete "$INSTDIR\Uninstall.exe"

	RMDir "$INSTDIR"

	# ������Ʈ�� ����
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${FULLNAME}"

SectionEnd

# -------------------------------------------------------
# Functions
Var GetInstalledSize.total

Function checkVCRedist

	# ����� ��ǻ���� Windows OS bit�� Ȯ���Ͽ�
	# bit�� �´� VS2013 ����� ��Ű���� ��ġ
	System::Call "kernel32::GetCurrentProcess() i .s"
	System::Call "kernel32::IsWow64Process(i s, *i .r0)"

	# Windows 32bit�� ���,
	${if} $0 == '0'
		ReadRegDword $R1 HKLM "SOFTWARE\Wow6432Node\Microsoft\VisualStudio\12.0\VC\Runtimes\x86" "Installed"

		# Visual studio 2013 �������ġŰ ��ġ��
		${if} $R1 == '1'
			DetailPrint "�̹� Visual studio 2013 32bit �� �������Ű���� ��ġ�Ǿ� �ֽ��ϴ�."

		${Else}
			DetailPrint "Visual studio 2013 32bit �� �������Ű���� ��ġ�Ǿ� ���� �ʽ��ϴ�. ��ġ�� �����մϴ�."
			MessageBox MB_OK "Visual studio 2013 32bit �� �������Ű���� ��ġ�Ǿ� ���� �ʾ� �������Ű���� ���� ��ġ�մϴ�."
			SetOutPath $INSTDIR
			File "vcredist_x86_vs2013.exe"
			ExecWait '"$INSTDIR\vcredist_x86_vs2013.exe"'
			Delete "$OUTDIR\vcredist_x86_vs2013.exe"
		${EndIf}

	# Windows 64bit�� ���,
	${ElseIf} $0 == '1'
		ReadRegDword $R2 HKLM "SOFTWARE\Wow6432Node\Microsoft\VisualStudio\12.0\VC\Runtimes\x64" "Installed"

		# Visual studio 2013 �������ġŰ ��ġ��
		${if} $R2 == '1'
			DetailPrint "�̹� Visual studio 2013 64bit �� �������Ű���� ��ġ�Ǿ� �ֽ��ϴ�."

		${Else}
			DetailPrint "Visual studio 2013 64bit �� �������Ű���� ��ġ�Ǿ� ���� �ʽ��ϴ�. ��ġ�� �����մϴ�."
			MessageBox MB_OK "Visual studio 2013 64bit �� �������Ű���� ��ġ�Ǿ� ���� �ʾ� �������Ű���� ���� ��ġ�մϴ�."
			SetOutPath $INSTDIR
			File "vcredist_x64_vs2013.exe"
			ExecWait '"$INSTDIR\vcredist_x64_vs2013.exe"'
			Delete "$OUTDIR\vcredist_x64_vs2013.exe"
		${EndIf}
	${EndIf}

FunctionEnd


Function setReg

	Call estimatedSize

	# ������Ʈ�� ���: ���α׷� �߰�/���Ÿ� ���ؼ� ����
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