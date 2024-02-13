class Account:
    def __init__(
        self,
        assets=None,
        balance=None,
        blockedCommission=None,
        blockedProfit=None,
        credit=None,
        currencyDigits=None,
        equity=None,
        floating=None,
        liabilities=None,
        login=None,
        margin=None,
        marginFree=None,
        marginInitial=None,
        marginLevel=None,
        marginLeverage=None,
        marginMaintenance=None,
        obsoleteValue=None,
        profit=None,
        sOActivation=None,
        sOEquity=None,
        sOLevel=None,
        sOMargin=None,
        sOTime=None,
        storage=None,
    ):
        self.assets: float = assets
        self.balance: float = balance
        self.blockedCommission: float = blockedCommission
        self.blockedProfit: float = blockedProfit
        self.credit: float = credit
        self.currencyDigits: int = currencyDigits
        self.equity: float = equity
        self.floating: float = floating
        self.liabilities: float = liabilities
        self.login: int = login
        self.margin: float = margin
        self.marginFree: float = marginFree
        self.marginInitial: float = marginInitial
        self.marginLevel: float = marginLevel
        self.marginLeverage: int = marginLeverage
        self.marginMaintenance: float = marginMaintenance
        self.obsoleteValue: float = obsoleteValue
        self.profit: float = profit
        self.sOActivation: float = sOActivation
        self.sOEquity: float = sOEquity
        self.sOLevel: float = sOLevel
        self.sOMargin: float = sOMargin
        self.sOTime: int = sOTime
        self.storage: float = storage

    def __json__(self):
        return {
            "assets": self.assets,
            "balance": self.balance,
            "blockedCommission": self.blockedCommission,
            "blockedProfit": self.blockedProfit,
            "credit": self.credit,
            "currencyDigits": self.currencyDigits,
            "equity": self.equity,
            "floating": self.floating,
            "liabilities": self.liabilities,
            "login": self.login,
            "margin": self.margin,
            "marginFree": self.marginFree,
            "marginInitial": self.marginInitial,
            "marginLevel": self.marginLevel,
            "marginLeverage": self.marginLeverage,
            "marginMaintenance": self.marginMaintenance,
            "obsoleteValue": self.obsoleteValue,
            "profit": self.profit,
            "sOActivation": self.sOActivation,
            "sOEquity": self.sOEquity,
            "sOLevel": self.sOLevel,
            "sOMargin": self.sOMargin,
            "sOTime": self.sOTime,
            "storage": self.storage,
        }
