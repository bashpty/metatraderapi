import base64
from flask import request


class DecodeHeader:
    def __init__(self, request):
        self.request = request

    def getBrokerCredentials(self):
        credentials = []
        auth_header = self.request.headers.get("Authorization")
        auth_server = self.request.headers.get("BrokerSever")
        auth_type, auth_data = auth_header.split(" ", 1)
        decoded_data = base64.b64decode(auth_data).decode("utf-8")
        username, password = decoded_data.split(":", 1)
        credentials.append(auth_server)
        credentials.append(username)
        credentials.append(password)
        return credentials
