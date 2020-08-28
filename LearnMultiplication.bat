cls
:start
@py LearnMultiplication.py %*
@pause
@echo off
set choice=
set /p choice="Press 'y' and enter to play again or press enter to exit. . ."
if not '%choice%'=='' set choice=%choice:~0,1%
if '%choice%'=='y' goto start