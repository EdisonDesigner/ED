@echo off
:: %cd%: return current path
:: /y 사용자 확인 없이 덮어쓰기
:: /e 디렉토리가 비어있어도 복사
:: /q 복사하는 동안 파일 이름을 표시하지 않기
:: /d 파일의 날짜/시간을 비교하여, 원본이 갱신된 경우에만 복사
:: /k 파일의 속성까지 복사
:: xcopy를 실행 시, 파일인지 폴더인지 질문하는 것을 자동으로
:: 처리하기 위해서 echo D를 이용

set SRC=E:\ED_v4_solution\data
set DST=%cd%\data

if not exist %DST%\data\ (
    md data
)

:: Copy example files(*.FCStd)
if not exist %DST%\examples\ (
    md %DST%\examples
)
copy %SRC%\examples\*.FCStd     %DST%\examples\ > nul

:: Copy Gui file
if not exist %DST%\Gui\ (
    md %DST%\Gui
)
echo D | xcopy /y %SRC%\Gui\*.*     %DST%\Gui /e/q/d/k > nul

:: Copy workbench icons in data/Mod
if not exist %DST%\Mod\ (
    md %DST%\Mod
)
echo D | xcopy /y %SRC%\Mod\*.*     %DST%\Mod /e/q/d/k > nul

echo Finished copying [ data ]