mkdir %~dp0..\build
cd %~dp0..\build

cmake -G "MinGW Makefiles" ..
mingw32-make install -j8 

cd %~dp0..\test
.\test.exe
