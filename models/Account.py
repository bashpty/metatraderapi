from dataclasses import dataclass

@dataclass
class Account:
    def __init__(
        self,
        Assets=None,
        Balance=None,
        BlockedCommission=None,
        BlockedProfit=None,
        Credit=None,
        CurrencyDigits=None,
        Equity=None,
        Floating=None,
        Liabilities=None,
        Login=None,
        Margin=None,
        MarginFree=None,
        MarginInitial=None,
        MarginLevel=None,
        MarginLeverage=None,
        MarginMaintenance=None,
        ObsoleteValue=None,
        Profit=None,
        SOActivation=None,
        SOEquity=None,
        SOLevel=None,
        SOMargin=None,
        SOTime=None,
        Storage=None,
    ):
        self.Assets: float = Assets
        self.Balance: float = Balance
        self.BlockedCommission: float = BlockedCommission
        self.BlockedProfit: float = BlockedProfit
        self.Credit: float = Credit
        self.CurrencyDigits: int = CurrencyDigits
        self.Equity: float = Equity
        self.Floating: float = Floating
        self.Liabilities: float = Liabilities
        self.Login: int = Login
        self.Margin: float = Margin
        self.MarginFree: float = MarginFree
        self.MarginInitial: float = MarginInitial
        self.MarginLevel: float = MarginLevel
        self.MarginLeverage: int = MarginLeverage
        self.MarginMaintenance: float = MarginMaintenance
        self.ObsoleteValue: float = ObsoleteValue
        self.Profit: float = Profit
        self.SOActivation: float = SOActivation
        self.SOEquity: float = SOEquity
        self.SOLevel: float = SOLevel
        self.SOMargin: float = SOMargin
        self.SOTime: int = SOTime
        self.Storage: float = Storage
         


    def __json__(self):
        return {
            "assets": self.Assets,
            "balance": self.Balance,
            "blockedCommission": self.BlockedCommission,
            "blockedProfit": self.BlockedProfit,
            "credit": self.Credit,
            "currencyDigits": self.CurrencyDigits,
            "equity": self.Equity,
            "floating": self.Floating,
            "liabilities": self.Liabilities,
            "login": self.Login,
            "margin": self.Margin,
            "marginFree": self.MarginFree,
            "marginInitial": self.MarginInitial,
            "marginLevel": self.MarginLevel,
            "marginLeverage": self.MarginLeverage,
            "marginMaintenance": self.MarginMaintenance,
            "obsoleteValue": self.ObsoleteValue,
            "profit": self.Profit,
            "sOActivation": self.SOActivation,
            "sOEquity": self.SOEquity,
            "sOLevel": self.SOLevel,
            "sOMargin": self.SOMargin,
            "sOTime": self.SOTime,
            "storage": self.Storage,
        }
