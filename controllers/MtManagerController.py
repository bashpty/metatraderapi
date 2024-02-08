

from flask_restful import Resource
from services.MetaQuotesService import MetaQuotesService
from dotenv import load_dotenv
import os
import sys
sys.path.append(os.path.split(os.getcwd())[0])
load_dotenv()

class MtManagerController(Resource):

    def get(self):

        metaQuotesService = MetaQuotesService()
        return metaQuotesService.getMtGroups()