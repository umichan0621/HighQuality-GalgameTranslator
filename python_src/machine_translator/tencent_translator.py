from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.tmt.v20180321 import tmt_client, models
import json


class TencentMachineTranslator:
    def __init__(self, api_id, api_key):
        cred = credential.Credential(api_id, api_key)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "tmt.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        self.__client = tmt_client.TmtClient(cred, "ap-shanghai", clientProfile)
        self.__req = models.TextTranslateRequest()

    def Translate(self, source_text):
        params = '{\"SourceText\":\"' + source_text + '\",\"Source\":\"ja\",\"Target\":\"zh\",\"ProjectId\":0}'
        self.__req.from_json_string(params)
        try:
            resp = self.__client.TextTranslate(self.__req)
            dic = json.loads(resp.to_json_string())
            return dic["TargetText"]
        except Exception:
            return "ERROR"
