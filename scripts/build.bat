cd ..
mkdir build
cd build
cmake -G "MinGW Makefiles" ..
mingw32-make
.\test.exe
