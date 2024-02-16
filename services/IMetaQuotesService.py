from abc import ABC, abstractmethod
from MT5Manager import ManagerAPI, MTAccount, MTUser
from models.EnableOptions import EnableOptions

from models.UserAdd import UserAdd


class IMetaQuotesService(ABC):

    @abstractmethod
    def getMtGroups(self, server: str, login: int, password: str):
        pass

    @abstractmethod
    def getAccountbyGroup(self, searchGroup: str):
        pass

    @abstractmethod
    def postLogin(self, acc: UserAdd, master: str, investor: str):
        pass

    @abstractmethod
    def updateLogin(self, acc: UserAdd):
        pass

    @abstractmethod
    def addBalance(self, login: int, balance: float):
        pass

    @abstractmethod
    def disableAccount(self, login: int):
        pass

    @abstractmethod
    def disableTrading(self, login: int):
        pass

    @abstractmethod
    def enableAccount(self, login: int, options: EnableOptions):
        pass

    @abstractmethod
    def getJournal(self, login: int, from_date: str, to_date: str):
        pass

    @abstractmethod
    def getAccount(self, login: int):
        pass
    


    @abstractmethod
    def getLogin(self, login: any):
        pass
