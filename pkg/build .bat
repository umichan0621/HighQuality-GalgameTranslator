go build -o libGoInterface.dll -buildmode=c-shared cmd\main.go

set DES_PATH=..\third_party\GoInterface
mkdir %DES_PATH%\include
mkdir %DES_PATH%\lib

move libGoInterface.h %DES_PATH%\include\GoInterface.h
move libGoInterface.dll %DES_PATH%\lib\libGoInterface.dll
