from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.tmt.v20180321 import tmt_client, models
import json


class TencentMachineTranslator:
    client = 0
    req = 0

    def SetIdAndKey(self, api_id, api_key):
        cred = credential.Credential(api_id, api_key)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "tmt.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        self.client = tmt_client.TmtClient(cred, "ap-shanghai", clientProfile)
        self.req = models.TextTranslateRequest()

    def Translate(self, source_text):
        params = '{\"SourceText\":\"' + source_text + '\",\"Source\":\"ja\",\"Target\":\"zh\",\"ProjectId\":0}'
        self.req.from_json_string(params)
        resp = self.client.TextTranslate(self.req)
        dic = json.loads(resp.to_json_string())
        return dic["TargetText"]
