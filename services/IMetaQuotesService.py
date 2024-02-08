from abc import ABC, abstractmethod
from MT5Manager import ManagerAPI


class IMetaQuotesService(ABC):

    @abstractmethod
    def getMtGroups(self, server: str, login: int, password: str):
        pass
