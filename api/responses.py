from rest_framework.response import Response
from rest_framework import status


class ResponseFail(Response):
    def init(self, data=""):
        data = {"code":200, "error":True, "status": "fail", "result": data}
        self.init__ = super().init(data, status=status.HTTP_200_OK)


class ResponseSuccess(Response):
    def init(self, data=""):
        if isinstance(data, Response):
            data = data.data

        data = {"code":200, "error":False, "status": "success", "result": data}
        super().init(data, status=status.HTTP_200_OK)

