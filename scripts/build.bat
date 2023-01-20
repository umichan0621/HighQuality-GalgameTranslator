mkdir %~dp0..\build
cd %~dp0..\build
echo %~dp0
cmake -G "MinGW Makefiles" ..

mingw32-make -j8
.\test.exe
