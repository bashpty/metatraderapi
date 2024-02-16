from datetime import datetime
from MT5Manager import ManagerAPI, MTConGroup, MTAccount, MTUser, MTDeal
import json
from dotenv import load_dotenv
import os
import sys
from models.Deal import Deal
from models.EnableOptions import EnableOptions
from utils import globalConst
from models.Account import Account
from models.UserAdd import UserAdd

from services.IMetaQuotesService import IMetaQuotesService


sys.path.append(os.path.split(os.getcwd())[0])
load_dotenv()


def to_list_json(obj):
    return obj


class MetaQuotesService(IMetaQuotesService):

    def __init__(self, server, login, password):
        self.server = server
        self.login = login
        self.password = password

    def getMtGroups(self):
        manager = ManagerAPI()
        manager.Connect(str(self.server), int(self.login), str(self.password))

        groupList = []
        for g in manager.GroupRequestArray():
            group: MTConGroup = g
            item = {"name": group.Group}
            groupList.append(item)

        json_array_string = json.dumps([to_list_json(obj) for obj in groupList])
        manager.LoggerOut()
        return json.loads(json_array_string)

    def getAccountbyGroup(self, searchGroup: str):
        manager = ManagerAPI()
        manager.Connect(str(self.server), int(self.login), str(self.password))
        list = []
        accountList: [MTAccount] = manager.UserAccountGetByGroup(searchGroup)  # type: ignore

        for account in accountList:

            item = Account(
                account.Assets,
                account.Balance,
                account.BlockedCommission,
                account.BlockedProfit,
                account.Credit,
                account.CurrencyDigits,
                account.Equity,
                account.Floating,
                account.Liabilities,
                account.Login,
                account.Margin,
                account.MarginFree,
                account.MarginInitial,
                account.MarginLevel,
                account.MarginLeverage,
                account.MarginMaintenance,
                account.ObsoleteValue,
                account.Profit,
                account.SOActivation,
                account.SOEquity,
                account.SOLevel,
                account.SOMargin,
                account.SOTime,
                account.Storage,
            )
            list.append(item.__json__())

        manager.LoggerOut()
        return list

    def getAccount(self, login: int):
        manager = ManagerAPI()
        manager.Connect(str(self.server), int(self.login), str(self.password))

        result: MTAccount = manager.UserAccountGet(login=int(login))

        item = Account(
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
        manager.LoggerOut()
        return item.__json__()

    def postLogin(self, acc: UserAdd, master: str, investor: str):

        created_user = {}
        manager = ManagerAPI()
        manager.Connect(str(self.server), int(self.login), str(self.password))

        userList = manager.UserGetByGroup(acc.Group)
        user: MTUser = userList[0]
        user.Clear()
        user.Name = acc.Name
        user.Group = acc.Group
        user.Leverage = acc.Leverage
        user.EMail = acc.EMail
        user.Rights = acc.Rights

        result = manager.UserAdd(user, master, investor)
        if result == True:
            created = manager.UserGetByGroup(acc.Group)
            filtered: MTUser = [u for u in created if u.EMail == acc.EMail][0]
            created_user = {
                "login": filtered.Login,
                "master": master,
                "investor": investor,
            }
        manager.LoggerOut()
        return created_user

    def updateLogin(self, acc: UserAdd):
        manager = ManagerAPI()
        manager.Connect(str(self.server), int(self.login), str(self.password))

        user = manager.UserGet(acc.Login)
        user.Name = acc.Name
        user.Group = acc.Group
        user.Leverage = acc.Leverage
        user.Comment = acc.Comment

        result = manager.UserUpdate(user)

        manager.LoggerOut()
        return result

    def addBalance(self, login: int, balance: float):
        manager = ManagerAPI()
        manager.Connect(str(self.server), int(self.login), str(self.password))

        result = manager.DealerBalance(
            login, balance, MTDeal.EnDealAction.DEAL_BALANCE, "addBalance"
        )
        return result

    def disableAccount(self, login: int):
        manager = ManagerAPI()
        manager.Connect(str(self.server), int(self.login), str(self.password))

        user = manager.UserGet(login)
        user.Rights = globalConst.MT_DISABLE_ACCOUNT
        result = manager.UserUpdate(user)

        manager.LoggerOut()
        return result

    def disableTrading(self, login: int):
        manager = ManagerAPI()
        manager.Connect(str(self.server), int(self.login), str(self.password))

        user = manager.UserGet(login)
        user.Rights = globalConst.MT_DISABLE_TRADING
        result = manager.UserUpdate(user)

        manager.LoggerOut()
        return result

    def enableAccount(self, login: int, options: EnableOptions):
        manager = ManagerAPI()
        manager.Connect(str(self.server), int(self.login), str(self.password))

        user = manager.UserGet(login)
        if options.single == True:
            user.Rights = globalConst.MT_ENABLE_ACCOUNT
        if options.all == True:
            user.Rights = globalConst.MT_ENABLE_ACCOUNT_WITH_ALL
        if options.expert == True:
            user.Rights = globalConst.MT_ENABLE_ACCOUNT_WITHEXPERT
        if options.trailing == True:
            user.Rights = globalConst.MT_ENABLE_ACCOUNT_WITHTRAILING

        result = manager.UserUpdate(user)

        manager.LoggerOut()
        return result

    def getLogin(self, login: int):
        manager = ManagerAPI()
        manager.Connect(str(self.server), int(self.login), str(self.password))

        result = manager.UserGet(login=int(login))
        manager.LoggerOut()
        return result

    def getJournal(self, login: int, from_date: str, to_date: str):
        manager = ManagerAPI()

        manager.Connect(str(self.server), int(self.login), str(self.password))
        logins = []
        logins.append(login)
        result = manager.DealRequestByLogins(
            logins, getTimeStamp(from_date), getTimeStamp(to_date)
        )
        dealsList = []
        for d in result:

            deal: MTDeal = d
            item = Deal.__json__(deal)
            dealsList.append(item)

        manager.LoggerOut()
        return dealsList


def getTimeStamp(dat: str):
    datetime_obj = datetime.strptime(
        dat, "%Y-%m-%d %H:%M:%S"
    )  # Adjust format as needed
    timestamp = int(datetime_obj.timestamp())
    return timestamp
