@echo off
:: %cd%: return current path
:: /y 사용자 확인 없이 덮어쓰기
:: /e 디렉토리가 비어있어도 복사
:: /q 복사하는 동안 파일 이름을 표시하지 않기
:: /d 파일의 날짜/시간을 비교하여, 원본이 갱신된 경우에만 복사
:: /k 파일의 속성까지 복사
:: xcopy를 실행 시, 파일인지 폴더인지 질문하는 것을 자동으로
:: 처리하기 위해서 echo D를 이용
:: > nul "파일이 복사되었습니다." 문장 출력 하지 않도록 설정

set SRC=E:\ED_v4_solution\Addons
set DST=%cd%\Addons

if not exist %DST%\Addons\ (
    md Addons
)

:: Copy python files
copy %SRC%\clamping.py          %DST%\ > nul
copy %SRC%\control.py           %DST%\ > nul
copy %SRC%\shaft.py             %DST%\ > nul
copy %SRC%\transmission.py      %DST%\ > nul
copy %SRC%\Sci_box.py           %DST%\ > nul
copy %SRC%\MSketch_parser.py    %DST%\ > nul

:: Copy image folders
:: Clamping module
echo D | xcopy /y %SRC%\clamping_module\*.* %DST%\clamping_module /e/q/d/k > nul

:: control module
echo D | xcopy /y %SRC%\control_module\*.* %DST%\control_module /e/q/d/k > nul

:: shaft module
echo D | xcopy /y %SRC%\shaft_module\*.* %DST%\shaft_module /e/q/d/k > nul

:: transmission module
echo D | xcopy /y %SRC%\transmission_module\*.* %DST%\transmission_module /e/q/d/k > nul

:: SCI BOX module
echo D | xcopy /y %SRC%\sci_box\*.* %DST%\sci_box /e/q/d/k > nul

:: L-shape bracket modeler
echo D | xcopy /y %SRC%\L-ShapeBracketModeler\*.* %DST%\L-ShapeBracketModeler /e/q/d/k > nul

echo Finished copying [ Addons ]
