@echo off
:: %cd%: return current path
:: /y 사용자 확인 없이 덮어쓰기
:: /e 디렉토리가 비어있어도 복사
:: /q 복사하는 동안 파일 이름을 표시하지 않기
:: /d 파일의 날짜/시간을 비교하여, 원본이 갱신된 경우에만 복사
:: /k 파일의 속성까지 복사
:: xcopy를 실행 시, 파일인지 폴더인지 질문하는 것을 자동으로
:: 처리하기 위해서 echo D를 이용

set SRC=E:\ED_v4_solution\Mod
set DST=%cd%\Mod
set TAB=    

if not exist %DST%\Mod (
    md Mod
)

echo Start copying [ Workbenches ]

:: Assembly2 workbench
echo D | xcopy /y %SRC%\Assembly2\docs\*.*      %DST%\Assembly2\docs /e/q/d/k > nul
echo D | xcopy /y %SRC%\Assembly2\Gui\*.*       %DST%\Assembly2\Gui /e/q/d/k > nul
echo D | xcopy /y %SRC%\Assembly2\tests\*.*     %DST%\Assembly2\tests /e/q/d/k > nul
echo D | xcopy /y %SRC%\Assembly2\*.py          %DST%\Assembly2 /e/q/d/k > nul

echo %TAB%Finished [ Assembly2 workbench ]

:: Import workbench
echo D | xcopy /y %SRC%\Import\SCL\*.*          %DST%\Import\SCL /e/q/d/k > nul
echo D | xcopy /y %SRC%\Import\*.py             %DST%\Import /e/q/d/k > nul

echo %TAB%Finished [ Import workbench ]

:: Mesh workbench
echo D | xcopy /y %SRC%\Mesh\*.py               %DST%\Import /e/q/d/k > nul

echo %TAB%Finished [ Mesh workbench ]

:: MeshPart workbench
echo D | xcopy /y %SRC%\MeshPart\*.py           %DST%\MeshPart /e/q/d/k > nul

echo %TAB%Finished [ MeshPart workbench ]

:: Part workbench
echo D | xcopy /y %SRC%\Part\AttachmentEditor\*.py      %DST%\Part\AttachmentEditor /e/q/d/k > nul
echo D | xcopy /y %SRC%\Part\AttachmentEditor\*.ui      %DST%\Part\AttachmentEditor /e/q/d/k > nul
echo D | xcopy /y %SRC%\Part\BOPTools\*.py              %DST%\Part\BOPTools /e/q/d/k > nul
echo D | xcopy /y %SRC%\Part\CompoundTools\*.py         %DST%\Part\CompoundTools /e/q/d/k > nul
echo D | xcopy /y %SRC%\Part\*.py                       %DST%\Part /e/q/d/k > nul

echo %TAB%Finished [ Part workbench ]

:: PartDesign workbench
echo D | xcopy /y %SRC%\PartDesign\fcgear\*.py              %DST%\PartDesign\fcgear /e/q/d/k > nul
echo D | xcopy /y %SRC%\PartDesign\PartDesignTests\*.py     %DST%\PartDesign\PartDesignTests /e/q/d/k > nul
echo D | xcopy /y %SRC%\PartDesign\Scripts\*.py             %DST%\PartDesign\Scripts /e/q/d/k > nul
echo D | xcopy /y %SRC%\PartDesign\*.py                     %DST%\PartDesign /e/q/d/k > nul
echo D | xcopy /y %SRC%\PartDesign\*.ui                     %DST%\PartDesign /e/q/d/k > nul

echo %TAB%Finished [ PartDesign workbench ]

:: Sketcher workbench
echo D | xcopy /y %SRC%\Sketcher\ProfileLib\*.py        %DST%\Sketcher\ProfileLib /e/q/d/k > nul
echo D | xcopy /y %SRC%\Sketcher\*.py                   %DST%\Sketcher /e/q/d/k > nul

echo %TAB%Finished [ Sketcher workbench ]

:: Start workbench
echo D | xcopy /y %SRC%\Start\StartPage\*.py         %DST%\Start\StartPage /e/q/d/k > nul
echo D | xcopy /y %SRC%\Start\*.py                   %DST%\Start /e/q/d/k > nul

echo %TAB%Finished [ Start workbench ]

:: Surface workbench
echo D | xcopy /y %SRC%\Surface\*.py                   %DST%\Surface /e/q/d/k > nul

echo %TAB%Finished [ Surface workbench ]

:: Test workbench
echo D | xcopy /y %SRC%\Test\*.py                   %DST%\Test /e/q/d/k > nul

echo %TAB%Finished [ Test workbench ]

:: Web workbench
echo D | xcopy /y %SRC%\Web\*.py                   %DST%\Web /e/q/d/k > nul

echo %TAB%Finished [ Web workbench ]

echo Finished copying [ Workbenches ]
