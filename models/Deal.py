from MT5Manager import MTDeal


class Deal:
    def __init__(
        self,
        Action=None,
        ActionLabel=None,
        Comment=None,
        Commission=None,
        ContractSize=None,
        Deal=None,
        Dealer=None,
        Digits=None,
        DigitsCurrency=None,
        Entry=None,
        EntryEntryLabel=None,
        ExpertID=None,
        ExternalID=None,
        Fee=None,
        Flags=None,
        Gateway=None,
        Login=None,
        MarketAsk=None,
        MarketBid=None,
        MarketLast=None,
        ModificationFlags=None,
        ObsoleteValue=None,
        Order=None,
        PositionID=None,
        Price=None,
        PriceGateway=None,
        PricePosition=None,
        PriceSL=None,
        PriceTP=None,
        Profit=None,
        ProfitRaw=None,
        RateMargin=None,
        RateProfit=None,
        Reason=None,
        Storage=None,
        Symbol=None,
        TickSize=None,
        TickValue=None,
        Time=None,
        TimeMsc=None,
        Value=None,
        Volume=None,
        VolumeClosed=None,
        VolumeClosedExt=None,
        VolumeExt=None,
    ):
        self.Action: int = Action
        self.ActionLabel: str = ActionLabel
        self.Comment: str = Comment
        self.Commission: float = Commission
        self.ContractSize: float = ContractSize
        self.Deal: int = Deal
        self.Dealer: int = Dealer
        self.Digits: int = Digits
        self.DigitsCurrency: int = DigitsCurrency
        self.Entry: int = Entry
        self.EntryLabel: str = EntryEntryLabel
        self.ExpertID: int = ExpertID
        self.ExternalID: str = ExternalID
        self.Fee: float = Fee
        self.Flags: int = Flags
        self.Gateway: str = Gateway
        self.Login: int = Login
        self.MarketAsk: float = MarketAsk
        self.MarketBid: float = MarketBid
        self.MarketLast: float = MarketLast
        self.ModificationFlags: int = ModificationFlags
        self.ObsoleteValue: float = ObsoleteValue
        self.Order: int = Order
        self.PositionID: int = PositionID
        self.Price: float = Price
        self.PriceGateway: float = PriceGateway
        self.PricePosition: float = PricePosition
        self.PriceSL: float = PriceSL
        self.PriceTP: float = PriceTP
        self.Profit: float = Profit
        self.ProfitRaw: float = ProfitRaw
        self.RateMargin: float = RateMargin
        self.RateProfit: float = RateProfit
        self.Reason: int = Reason
        self.Storage: float = Storage
        self.Symbol: str = Symbol
        self.TickSize: float = TickSize
        self.TickValue: float = TickValue
        self.Time: int = Time
        self.TimeMsc: int = TimeMsc
        self.Value: float = Value
        self.Volume: int = Volume
        self.VolumeClosed: int = VolumeClosed
        self.VolumeClosedExt: int = VolumeClosedExt
        self.VolumeExt: int = VolumeExt

    def __json__(obj: MTDeal):
        return {
            "Action": obj.Action,
            "ActionLabel": getActionDesc(obj.Action),
            "Comment": obj.Comment,
            "Commission": obj.Commission,
            "ContractSize": obj.ContractSize,
            "Deal": obj.Deal,
            "Dealer": obj.Dealer,
            "Digits": obj.Digits,
            "DigitsCurrency": obj.DigitsCurrency,
            "Entry": obj.Entry,
            "Entry": getEntryDesc(obj.Entry),
            "ExpertID": obj.ExpertID,
            "ExternalID": obj.ExternalID,
            "Fee": obj.Fee,
            "Flags": obj.Flags,
            "Gateway": obj.Gateway,
            "Login": obj.Login,
            "MarketAsk": obj.MarketAsk,
            "MarketBid": obj.MarketBid,
            "MarketLast": obj.MarketLast,
            "ModificationFlags": obj.ModificationFlags,
            "ObsoleteValue": obj.ObsoleteValue,
            "Order": obj.Order,
            "PositionID": obj.PositionID,
            "Price": obj.Price,
            "PriceGateway": obj.PriceGateway,
            "PricePosition": obj.PricePosition,
            "PriceSL": obj.PriceSL,
            "PriceTP": obj.PriceTP,
            "Profit": obj.Profit,
            "ProfitRaw": obj.ProfitRaw,
            "RateMargin": obj.RateMargin,
            "RateProfit": obj.RateProfit,
            "Reason": obj.Reason,
            "Storage": obj.Storage,
            "Symbol": obj.Symbol,
            "TickSize": obj.TickSize,
            "TickValue": obj.TickValue,
            "Time": obj.Time,
            "TimeMsc": obj.TimeMsc,
            "Value": obj.Value,
            "Volume": obj.Volume,
            "VolumeClosed": obj.VolumeClosed,
            "VolumeClosedExt": obj.VolumeClosedExt,
            "VolumeExt": obj.VolumeExt,
        }


def getActionDesc(val: int) -> str:
    if val == MTDeal.EnDealAction.DEAL_BUY:
        return "DEAL_BUY"
    if val == MTDeal.EnDealAction.DEAL_SELL:
        return "DEAL_SELL"
    if val == MTDeal.EnDealAction.DEAL_SELL_CANCELED:
        return "DEAL_SELL_CANCELED"
    if val == MTDeal.EnDealAction.DEAL_BUY_CANCELED:
        return "DEAL_BUY_CANCELED"
    if val == MTDeal.EnDealAction.DEAL_COMMISSION:
        return "DEAL_COMMISSION"
    if val == MTDeal.EnDealAction.DEAL_CHARGE:
        return "DEAL_CHARGE"
    if val == MTDeal.EnDealAction.DEAL_CREDIT:
        return "DEAL_CREDIT"
    if val == MTDeal.EnDealAction.DEAL_BONUS:
        return "DEAL_BONUS"
    if val == MTDeal.EnDealAction.DEAL_DIVIDEND:
        return "DEAL_DIVIDEND"
    if val == MTDeal.EnDealAction.DEAL_TAX:
        return "DEAL_TAX"
    return ""


def getEntryDesc(val: int) -> str:
    if val == MTDeal.EnDealEntry.ENTRY_IN:
        return "ENTRY_IN"
    if val == MTDeal.EnDealEntry.ENTRY_OUT:
        return "ENTRY_OUT"
    return ""
