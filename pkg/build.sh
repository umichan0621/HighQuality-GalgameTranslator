go build -o libGoInterface.so -buildmode=c-shared cmd/main.go

DES_PATH=../third_party/
mkdir -p ${DES_PATH}/include
mkdir -p ${DES_PATH}/lib

mv libGoInterface.h ${DES_PATH}/include/GoInterface.h
mv libGoInterface.so ${DES_PATH}/lib/libGoInterface.so
