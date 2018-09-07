@echo off
:: %cd%: return current path
:: /y 사용자 확인 없이 덮어쓰기
:: /e 디렉토리가 비어있어도 복사
:: /q 복사하는 동안 파일 이름을 표시하지 않기
:: /d 파일의 날짜/시간을 비교하여, 원본이 갱신된 경우에만 복사
:: /k 파일의 속성까지 복사
:: xcopy를 실행 시, 파일인지 폴더인지 질문하는 것을 자동으로
:: 처리하기 위해서 echo D를 이용

:: Set path
set BIN_SRC=E:\ED_GitHub\_bin_release
set ED_SRC=E:\ED_v4_solution\bin
set DST=%cd%\bin

if not exist %DST%\bin\ (
    md bin
)

:: Copy bin folder for release
echo # Work is in progress, Wait a moment......

echo D | xcopy /y %BIN_SRC%\*.* %DST% /e/q/d/k > nul

echo Finished copying [ bin ]

:: Copy EdisonDesigner files from solution
copy %ED_SRC%\EdisonDesigner.exe        %DST%\ > nul
copy %ED_SRC%\EdisonDesigner.pyd        %DST%\ > nul
copy %ED_SRC%\EdisonDesignerApp.dll     %DST%\ > nul
copy %ED_SRC%\EdisonDesignerBase.dll    %DST%\ > nul
copy %ED_SRC%\EdisonDesignerCmd.exe     %DST%\ > nul
copy %ED_SRC%\EdisonDesignerGui.dll     %DST%\ > nul
copy %ED_SRC%\EdisonDesignerGui.pyd     %DST%\ > nul

echo Finished copying [ EdisonDesigner files ]
