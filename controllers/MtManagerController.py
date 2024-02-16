import base64
from datetime import datetime
from flask import request
from flask_restful import Resource
from models import Account
from models.EnableOptions import EnableOptions
from models.UserAdd import UserAdd
from MT5Manager import MTUser, MTAccount


from services.MetaQuotesService import MetaQuotesService

from dotenv import load_dotenv
import os
import sys

from utils.decodeHeaders import DecodeHeader

sys.path.append(os.path.split(os.getcwd())[0])
load_dotenv()


class MtGroupsController(Resource):

    def get(self):
        decodeService = DecodeHeader(request)
        cred = decodeService.getBrokerCredentials()
        metaQuotesService = MetaQuotesService(cred[0], cred[1], cred[2])
        return metaQuotesService.getMtGroups()


class MtLoginController(Resource):

    def get(self):

        group = request.args.get("group")
        login = request.args.get("login")

        decodeService = DecodeHeader(request)
        cred = decodeService.getBrokerCredentials()
        metaQuotesService = MetaQuotesService(cred[0], cred[1], cred[2])

        if group is not None:
            return metaQuotesService.getLoginsByGroup(str(group))
        if login is not None:
            result: MTAccount = metaQuotesService.getAccount(int(login))
            account = Account(
                result.Assets,
                result.Balance,
                result.BlockedCommission,
                result.BlockedProfit,
                result.Credit,
                result.CurrencyDigits,
                result.Equity,
                result.Floating,
                result.Liabilities,
                result.Login,
                result.Margin,
                result.MarginFree,
                result.MarginInitial,
                result.MarginLevel,
                result.MarginLeverage,
                result.MarginMaintenance,
                result.ObsoleteValue,
                result.Profit,
                result.SOActivation,
                result.SOEquity,
                result.SOLevel,
                result.SOMargin,
                result.SOTime,
                result.Storage,
            )

            return account.__json__()


class MtUserController(Resource):

    def get(self):
        decodeService = DecodeHeader(request)
        cred = decodeService.getBrokerCredentials()
        metaQuotesService = MetaQuotesService(cred[0], cred[1], cred[2])
        login = request.args.get("login")
        result: MTUser = metaQuotesService.getLogin(login)
        obj = UserAdd()
        return obj.__json2__(result)

    def put(self):
        data = request.get_json()

        decodeService = DecodeHeader(request)
        cred = decodeService.getBrokerCredentials()
        metaQuotesService = MetaQuotesService(cred[0], cred[1], cred[2])
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
        decodeService = DecodeHeader(request)
        cred = decodeService.getBrokerCredentials()
        metaQuotesService = MetaQuotesService(cred[0], cred[1], cred[2])

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

        decodeService = DecodeHeader(request)
        cred = decodeService.getBrokerCredentials()
        metaQuotesService = MetaQuotesService(cred[0], cred[1], cred[2])
        userAdd = UserAdd(
            Name=data["name"],
            Group=data["group"],
            Leverage=data["leverage"],
            Rights=2403,
            EMail=data["email"],
        )

        return metaQuotesService.postLogin(
            userAdd, str(data["password"]), str(data["passwordInvestor"])
        )


class MtMetricsController(Resource):
    def get(self):
        login = request.args.get("login")
        from_date = request.args.get("from")
        to_date = request.args.get("to")

        decodeService = DecodeHeader(request)
        cred = decodeService.getBrokerCredentials()
        metaQuotesService = MetaQuotesService(cred[0], cred[1], cred[2])
        return metaQuotesService.getJournal(int(login), from_date, to_date)


def getTimeStamp():
    now = datetime.now()
    timestamp = now.timestamp()
    return int(timestamp)
