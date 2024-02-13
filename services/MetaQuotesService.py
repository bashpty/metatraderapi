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

    def __init__(self):
        self.server = os.getenv("SERVER")
        self.login = os.getenv("LOGIN")
        self.password = os.getenv("PASSWORD")

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

    def getLoginsByGroup(self, searchGroup: str):
        manager = ManagerAPI()
        manager.Connect(str(self.server), int(self.login), str(self.password))
        accountList = []

        manager.NetworkAddress
        for acc in manager.UserAccountGetByGroup(searchGroup):
            account: MTAccount = acc
            item = Account(
                assets=account.Assets,
                balance=account.Balance,
                blockedCommission=account.BlockedCommission,
                blockedProfit=account.BlockedProfit,
                credit=account.Credit,
                currencyDigits=account.CurrencyDigits,
                equity=account.Equity,
                floating=account.Floating,
                liabilities=account.Liabilities,
                login=account.Login,
                margin=account.Margin,
                marginFree=account.MarginFree,
                marginInitial=account.MarginInitial,
                marginLevel=account.MarginLevel,
                marginLeverage=account.MarginLeverage,
                marginMaintenance=account.MarginMaintenance,
                obsoleteValue=account.ObsoleteValue,
                profit=account.Profit,
                sOActivation=account.SOActivation,
                sOEquity=account.SOEquity,
                sOLevel=account.SOLevel,
                sOMargin=account.SOMargin,
                sOTime=account.SOTime,
                storage=account.Storage,
            )
            accountList.append(item.__json__())

        manager.LoggerOut()
        return accountList

    def postLogin(self, acc: UserAdd, master: str, investor: str):
        manager = ManagerAPI()

        manager.Connect(str(self.server), int(self.login), str(self.password))
        userList = manager.UserGetByGroup(acc.Group)
        user: MTUser = userList[0]
        user.Clear()
        user.Name = acc.Name
        user.Group = acc.Group
        user.Leverage = acc.Leverage
        user.EMail = acc.EMail
        user.Color = acc.Color
        user.Rights = acc.Rights

        result = manager.UserAdd(user, master, investor)
        manager.LoggerOut()
        return result

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

    def getLogin(self, login: any):
        manager = ManagerAPI()
        manager.Connect(str(self.server), int(self.login), str(self.password))
        result = manager.UserGet(login)

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
