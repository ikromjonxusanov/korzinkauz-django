from rest_framework.response import Response
from rest_framework import status


class ResponseFail(Response):
    def init(self, data=""):
        data = {"status": "fail", "data": data}
        self.init__ = super().init(data, status=status.HTTP_200_OK)


class ResponseSuccess(Response):
    def init(self, data=""):
        if isinstance(data, Response):
            data = data.data

        data = {"status": "success", "data": data}
        super().init(data, status=status.HTTP_200_OK)