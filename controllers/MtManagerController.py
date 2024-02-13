from datetime import datetime
from flask import request
from flask_restful import Resource
from models.EnableOptions import EnableOptions
from models.UserAdd import UserAdd
from MT5Manager import MTUser


from services.MetaQuotesService import MetaQuotesService

from dotenv import load_dotenv
import os
import sys

sys.path.append(os.path.split(os.getcwd())[0])
load_dotenv()


class MtGroupsController(Resource):

    def get(self):
        metaQuotesService = MetaQuotesService()
        return metaQuotesService.getMtGroups()


class MtLoginController(Resource):

    def get(self):

        metaQuotesService = MetaQuotesService()
        return metaQuotesService.getLoginsByGroup("demo\\FYT_SDT_USD")


class MtUserController(Resource):

    def get(self):
        metaQuotesService = MetaQuotesService()
        login = [8097]
        return metaQuotesService.getLogin(login)

    def put(self):
        data = request.get_json()

        metaQuotesService = MetaQuotesService()
        userAdd = UserAdd(
            Name=data["name"],
            Group=data["group"],
            Leverage=data["leverage"],
            Login=data["login"],
            Comment=data["comment"],
        )
        return metaQuotesService.updateLogin(userAdd)

    def patch(self):
        addBalance = bool(request.args.get("addBalance"))
        disbleAccount = bool(request.args.get("disbleAccount"))
        enableAccount = bool(request.args.get("enableAccount"))
        data = request.get_json()
        metaQuotesService = MetaQuotesService()

        if addBalance == True:
            return metaQuotesService.addBalance(data["login"], data["balance"])
        if disbleAccount == True:
            return metaQuotesService.disableAccount(data["login"])
        if enableAccount == True:
            options: EnableOptions = EnableOptions(
                bool(data["single"]),
                bool(data["trailing"]),
                bool(data["expert"]),
                bool(data["all"]),
            )
            return metaQuotesService.enableAccount(data["login"], options)

    def post(self):

        data = request.get_json()

        metaQuotesService = MetaQuotesService()
        userAdd = UserAdd(
            Name=data["name"],
            Group=data["group"],
            Leverage=data["leverage"],
            Rights=2403,
            EMail=data["eMail"],
        )

        return metaQuotesService.postLogin(
            userAdd, str(data["password"]), str(data["passwordInvestor"])
        )


class MtMetricsController(Resource):
    def get(self):
        login = request.args.get("login")
        from_date = request.args.get("from")
        to_date = request.args.get("to")

        metaQuotesService = MetaQuotesService()
        return metaQuotesService.getJournal(int(login), from_date, to_date)


def getTimeStamp():
    now = datetime.now()
    timestamp = now.timestamp()
    return int(timestamp)
