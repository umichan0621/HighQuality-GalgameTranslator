package main

import "C"
import (
	"main/translate"
)

//export TencentTranslate
func TencentTranslate(secretId, secretKey, region, srcLanguage, desLanguage, srcText *C.char) *C.char {

	tencentTrans := translate.NewTencentTrans()
	err := tencentTrans.Init(C.GoString(secretId), C.GoString(secretKey))
	if err != nil {
		return C.CString("error")
	}

	tencentTrans.SetRegion(C.GoString(region))
	desText, err := tencentTrans.Translate(C.GoString(srcLanguage), C.GoString(desLanguage), C.GoString(srcText))
	if err != nil {
		return C.CString("error")
	}
	return C.CString(desText)
}

func main() {}
