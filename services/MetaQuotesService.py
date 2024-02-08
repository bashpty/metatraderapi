from MT5Manager import ManagerAPI, MTConGroup
import json
from dotenv import load_dotenv
import os
import sys

from services.IMetaQuotesService import IMetaQuotesService

sys.path.append(os.path.split(os.getcwd())[0])
load_dotenv()


def to_list_json(obj):
    return {"name": obj.group}


class MetaQuotesService(IMetaQuotesService):

    def __init__(self):
        self.server = os.getenv("SERVER")
        self.login = os.getenv("LOGIN")
        self.password = os.getenv("PASSWORD")

    def getMtGroups(self):
        manager = ManagerAPI()
        manager.Connect(self.server, self.login, self.password)

        if manager:
            print("Conexión exitosa al servidor:")
        else:
            print("Error al conectar al servidor:")

        for g in manager.GroupRequestArray():
            group: MTConGroup = g
            print(group.Group)
            # item = {"name": group.Group}
            # groupList.append(item)

        #json_array_string = json.dumps([to_list_json(obj) for obj in groupList])
        #manager.LoggerOut()
        #return json.loads(json_array_string)
