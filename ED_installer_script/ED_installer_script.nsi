# Include Mordern UI header
!include "MUI2.nsh"
!include "LogicLib.nsh"

# EdisonDesigner version info
!include Version.nsi

# Program name and description
!define APPNAME				"EdisonDesigner"
!define PUPNAME				"KAIST iCAD laboratory"
!define DESCRIPTION			"A freeware CAD system for education"
!define HELPURL				"http://kiay.kr/ED/manual"
!define ABOUTURL			"http://kiay.kr/ED/manual"
!define UPDATEURL			"http://kiay.kr/ED/manual"

# Set "Run as administrator"
RequestExecutionLevel admin

# Install directory
InstallDir "$PROGRAMFILES\${APPNAME}"

# Installer and Uninstaller name
Name "${APPNAME}"

# Installer name
OutFile "${APPNAME}_${VERSIONMAJOR}.${VERSIONMINOR}_x86.exe"

!define MUI_ABORTWARNING
!define MUI_ICON	"Install.ico"
!define MUI_UNICON	"Uninstaller.ico"

# -------------------------------------------------------
# Check admin
Function checkAdmin
	UserInfo::GetAccountType
	pop $0

	${If} $0 != "admin"
		MessageBox MB_ICONSTOP \
			"Needs an administrator authority. Please right click the installer and run as administrator"
		QUIT
	${EndIf}
FunctionEnd

# -------------------------------------------------------

; Function .onInit
; 	# Set splash image
; 	; File /oname=splash.bmp "splash.bmp"
;     ; splash::show 1000 splash
; 	AdvSplash::show 200 1000 500 -1 "Splash_2018.png"
;
; 	Call checkAdmin
; FunctionEnd

# -------------------------------------------------------
# Pages
# Welcome page
;!define			MUI_WELCOMEFINISHPAGE_BITMAP "${NSISDIR}\Contrib\Graphics\Wizard\orange.bmp"
!define 		WELCOME_TITLE "Welcome to install ${APPNAME}"
!define 		MUI_WELCOMEPAGE_TITLE '${WELCOME_TITLE}'
!insertmacro 	MUI_PAGE_WELCOME

# Setting pages
!insertmacro 	MUI_PAGE_LICENSE "License.rtf"					 # License page
!insertmacro 	MUI_PAGE_COMPONENTS								 # Component page
!insertmacro 	MUI_PAGE_DIRECTORY								 # Install directory page
!insertmacro 	MUI_PAGE_INSTFILES								 # Install status page

; !define			MUI_FINISHPAGE_RUN "$INSTDIR\bin\${APPNAME}.exe" # ��ġ ���� ��, ���α׷� ����
!insertmacro    MUI_PAGE_FINISH                             	 # Finish page

!insertmacro    MUI_UNPAGE_WELCOME                  			 # Uninstaller welcome page
!insertmacro 	MUI_UNPAGE_CONFIRM								 # Ask uninstall
!insertmacro 	MUI_UNPAGE_INSTFILES							 # Uninstall status page


# -------------------------------------------------------
# Languages

!insertmacro 	MUI_LANGUAGE "Korean"							# Language

# -------------------------------------------------------
# ��ġ���� ���� ����

VIProductVersion "${APP_VI_PRODUCT_VER}"
VIAddVersionKey /LANG=${LANG_KOREAN} "FileDescription" "${APPNAME} installer"
VIAddVersionKey /LANG=${LANG_KOREAN} "ProductName"     "${APPNAME}"
VIAddVersionKey /LANG=${LANG_KOREAN} "ProductVersion"  "${VERSIONMAJOR}.${VERSIONMINOR}.${VERSIONBUILD}"
VIAddVersionKey /LANG=${LANG_KOREAN} "CompanyName"     "${PUPNAME}"
VIAddVersionKey /LANG=${LANG_KOREAN} "LegalCopyright"  "Copyright 2014-2018. iCAD Lab. all rights reserved"
VIAddVersionKey /LANG=${LANG_KOREAN} "FileVersion"     "${APP_VI_PRODUCT_VER}"

# -------------------------------------------------------
# Show details install and uninstall process (hide | show | nevershow)
ShowInstDetails     show
ShowUninstDetails   show

# -------------------------------------------------------

Section "EdisonDesigner(Required)" EdisonDesigner

	# Check VS 2013 redistribution package installation
	Call checkVCRedist

	# Addons, bin, data, doc, Ext, lib, Mod
	# 1. Addons folder
	SetOutPath $INSTDIR\Addons
	SetCompress auto
    DetailPrint "Extracting Addons package..."
	SetDetailsPrint listOnly

	File Addons.7z
	SetDetailsPrint both
	Nsis7z::ExtractWithDetails "Addons.7z" "Installing Addons package %s..."

	Delete "$OUTDIR\Addons.7z"

	# --------------------------------------------------------------------
	# 2. bin folder
	SetOutPath $INSTDIR\bin
	SetCompress auto
    DetailPrint "Extracting bin package..."
	SetDetailsPrint listOnly

	File bin.7z
	SetDetailsPrint both
	Nsis7z::ExtractWithDetails "bin.7z" "Installing bin package %s..."

	Delete "$OUTDIR\bin.7z"

	# --------------------------------------------------------------------
	# 3. data folder
	SetOutPath $INSTDIR\data
	SetCompress auto
    DetailPrint "Extracting data package..."
	SetDetailsPrint listOnly

	File data.7z
	SetDetailsPrint both
	Nsis7z::ExtractWithDetails "data.7z" "Installing data package %s..."

	Delete "$OUTDIR\data.7z"

	# --------------------------------------------------------------------
	# 4. doc folder
	SetOutPath $INSTDIR\doc
	SetCompress auto
    DetailPrint "Extracting doc package..."
	SetDetailsPrint listOnly

	File doc.7z
	SetDetailsPrint both
	Nsis7z::ExtractWithDetails "doc.7z" "Installing doc package %s..."

	Delete "$OUTDIR\doc.7z"

	# --------------------------------------------------------------------
	# 5. Ext folder
	SetOutPath $INSTDIR\Ext
	SetCompress auto
    DetailPrint "Extracting Ext package..."
	SetDetailsPrint listOnly

	File Ext.7z
	SetDetailsPrint both
	Nsis7z::ExtractWithDetails "Ext.7z" "Installing Ext package %s..."

	Delete "$OUTDIR\Ext.7z"

	# --------------------------------------------------------------------
	# 6. lib folder
	SetOutPath $INSTDIR\lib
	SetCompress auto
    DetailPrint "Extracting lib package..."
	SetDetailsPrint listOnly

	File lib.7z
	SetDetailsPrint both
	Nsis7z::ExtractWithDetails "lib.7z" "Installing lib package %s..."

	Delete "$OUTDIR\lib.7z"

	# --------------------------------------------------------------------
	# 7. Mod folder
	SetOutPath $INSTDIR\Mod
	SetCompress auto
    DetailPrint "Extracting Mod package..."
	SetDetailsPrint listOnly

	File Mod.7z
	SetDetailsPrint both
	Nsis7z::ExtractWithDetails "Mod.7z" "Installing Mod package %s..."

	Delete "$OUTDIR\Mod.7z"

	# --------------------------------------------------------------------


	# Create shortcut in install directory
	CreateShortcut "$INSTDIR\${APPNAME}.lnk" "$INSTDIR\bin\EdisonDesigner.exe" "" ""

	# Set regstry for Add or Remove programs
	Call setReg

	# Create uninstaller
	WriteUninstaller "$INSTDIR\Uninstall.exe"

SectionEnd

# -------------------------------------------------------
# Section: start menu and shortcut in start menu

Section "Add to start menu" AddStartMenu

	createDirectory	"$SMPROGRAMS\${APPNAME}"
	createShortCut	"$SMPROGRAMS\${APPNAME}\${APPNAME}.lnk" "$INSTDIR\bin\EdisonDesigner.exe" "" ""

SectionEnd

# -------------------------------------------------------
# Section: shortcut in desktop

Section "Add to desktop icon" AddDesktop

	CreateShortCut  "$DESKTOP\${APPNAME}.lnk" "$INSTDIR\bin\EdisonDesigner.exe" "" ""

SectionEnd

# -------------------------------------------------------
# Section description

	#Language strings
	LangString EdisonDesigner ${LANG_KOREAN} \
		"Install EdisonDesigner."

	LangString AddStartMenu ${LANG_KOREAN} \
		"Create program group to start menu..."

	LangString AddDesktop ${LANG_KOREAN} \
		"Create shortcut to desktop..."

	#Assign language strings to sections
	!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
		!insertmacro MUI_DESCRIPTION_TEXT ${EdisonDesigner} $(EdisonDesigner)
		!insertmacro MUI_DESCRIPTION_TEXT ${AddStartMenu}	$(AddStartMenu)
		!insertmacro MUI_DESCRIPTION_TEXT ${AddDesktop}		$(AddDesktop)
	!insertmacro MUI_FUNCTION_DESCRIPTION_END

# -------------------------------------------------------
# Uninstaller section

# Warning message when running uninstaller
Function un.onInit
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "Do you want to remove ${APPNAME}?" IDYES +2
  Abort
FunctionEnd

# Message after finishing uninstallation
Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "${APPNAME} was completely uninstalled."
FunctionEnd

Section "Uninstall"

	# Delete lnk file in start menu
	Delete "$SMPROGRAMS\${APPNAME}\${APPNAME}.lnk"

	# Delete folder in start menu
	RMDir "$SMPROGRAMS\${APPNAME}"

	# Delete shortcut in desktop
	Delete "$DESKTOP\${APPNAME}.lnk"

	# Delete shortcut in install directory
	Delete "$INSTDIR\${APPNAME}.lnk"

	# Delete folders in install directory
	RMDir /r "$INSTDIR\Addons"
	RMDir /r "$INSTDIR\bin"
	RMDir /r "$INSTDIR\data"
	RMDir /r "$INSTDIR\doc"
	RMDir /r "$INSTDIR\Ext"
	RMDir /r "$INSTDIR\lib"
	RMDir /r "$INSTDIR\Mod"


    Delete "$INSTDIR\vcredist_x86_vs2013.exe"
    Delete "$INSTDIR\vcredist_x64_vs2013.exe"

	Delete "$INSTDIR\Uninstall.exe"

	RMDir "$INSTDIR"

	# Remove registry
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}"

SectionEnd

# -------------------------------------------------------
# Functions
Var GetInstalledSize.total

Function checkVCRedist

	# Check OS and install the VS2013 Redistribution package for user computer os
	System::Call "kernel32::GetCurrentProcess() i .s"
	System::Call "kernel32::IsWow64Process(i s, *i .r0)"

	# In case of 32 bit OS,
	${if} $0 == '0'
		ReadRegDword $R1 HKLM "SOFTWARE\Wow6432Node\Microsoft\VisualStudio\12.0\VC\Runtimes\x86" "Installed"

		${if} $R1 == '1'
			DetailPrint "Redistribution package for VS2013 x86 is already installed."

		${Else}
			DetailPrint "Redistribution package for VS2013 x86 is not installed. Proceed with installation"
			MessageBox MB_OK "Redistribution package for VS2013 x86 is not installed, so install the Redistribution Package first."
			SetOutPath $INSTDIR
			File "vcredist_x86_vs2013.exe"
			ExecWait '"$INSTDIR\vcredist_x86_vs2013.exe"'
			Delete "$OUTDIR\vcredist_x86_vs2013.exe"
		${EndIf}

	# In case of 64 bit OS,
	${ElseIf} $0 == '1'
		ReadRegDword $R2 HKLM "SOFTWARE\Wow6432Node\Microsoft\VisualStudio\12.0\VC\Runtimes\x64" "Installed"

		${if} $R2 == '1'
			DetailPrint "Redistribution package for VS2013 x64 is already installed."

		${Else}
			DetailPrint "Redistribution package for VS2013 x64 is not installed. Proceed with installation"
			MessageBox MB_OK "Redistribution package for VS2013 x64 is not installed, so install the Redistribution Package first."
			SetOutPath $INSTDIR
			File "vcredist_x64_vs2013.exe"
			ExecWait '"$INSTDIR\vcredist_x64_vs2013.exe"'
			Delete "$OUTDIR\vcredist_x64_vs2013.exe"
		${EndIf}
	${EndIf}

FunctionEnd


Function setReg

	Call estimatedSize

	# Set registry
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "DisplayName"				"${APPNAME} - ${DESCRIPTION}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "UninstallString"			'"$INSTDIR\Uninstall.exe"'
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "QuietUninstallString"	'"$INSTDIR\Uninstall.exe" /S'
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "InstallLocation"			"$INSTDIR"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "DisplayIcon"				"$INSTDIR\bin\EdisonDesigner.exe"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "HelpLink"				"${HELPURL}"
   	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "URLInfoAbout"			"${ABOUTURL}"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "URLUpdateInfo"			"${UPDATEURL}"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "Publisher"				"${PUPNAME}"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "DisplayVersion"			"${VERSIONMAJOR}.${VERSIONMINOR}.${VERSIONBUILD}"
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "VersionMajor"			${VERSIONMAJOR}
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "VersionMinor"			${VERSIONMINOR}
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "EstimatedSize"			$GetInstalledSize.total

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
