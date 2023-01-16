package translate

import (
	v20180321 "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tmt/v20180321"
)

type TencentTrans struct {
	client *v20180321.Client
	region string
}

func NewTencentTrans() *TencentTrans {
	return &TencentTrans{nil, "ap-shanghai"}
}

func (tencentTrans *TencentTrans) SetRegion(region string) {
	tencentTrans.region = region
}

func (tencentTrans *TencentTrans) Init(secretId string, secretKey string) error {
	var err error
	tencentTrans.client, err = v20180321.NewClientWithSecretId(secretId, secretKey, tencentTrans.region)
	if err != nil {
		return err
	}
	return nil
}

func (tencentTrans *TencentTrans) Translate(srcLanguage, desLanguage, srcText string) (string, error) {
	transRequest := v20180321.NewTextTranslateRequest()
	transRequest.Source = &srcLanguage
	transRequest.Target = &desLanguage
	transRequest.SourceText = &srcText
	id := int64(0)
	transRequest.ProjectId = &id

	transResponse, err := tencentTrans.client.TextTranslate(transRequest)
	if err != nil {
		return "", err
	}
	return *transResponse.Response.TargetText, nil
}
