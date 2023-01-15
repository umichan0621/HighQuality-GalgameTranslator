package main

import "C"
import (
	"fmt"
)

//export say
func say(text *C.char) {
	fmt.Println(C.GoString(text))
}

func TencentTranslate(secretId, secretKey *C.char) *C.char {
	// region := "ap-shanghai"

	// client, err := v20180321.NewClientWithSecretId(C.GoString(secretId), C.GoString(secretKey), region)
	// if err != nil {
	// 	return "error"
	// }
	z := C.CString("fsfs")
}

func main() {}
