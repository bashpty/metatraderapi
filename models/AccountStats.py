from datetime import datetime
from decimal import Decimal
from typing import List


class AccountStats:
    def __init__(self):
        self.status: str
        self.firstTradeDate: Decimal = 0
        self.accountSize: Decimal = 0
        self.balance: Decimal = 0
        self.tradesPlaced: int
        self.server: str
        self.profitTarget: ProfitTarget()
        self.maxDailyLoss: MaxDailyLoss()
        self.maxLoss: MaxLoss()
        self.rates: Rates()
        self.orderTypeSummary: OrderTypeSummary()
        self.accountSummary: List[AccountSummary]
        self.tradingJournal: List[TradingJournal]

    def __json__(self):
        return {
            "status": self.status,
            "firstTradeDate": str(self.firstTradeDate),
            "accountSize": str(self.accountSize),
            "balance": str(self.balance),
            "tradesPlaced": self.tradesPlaced,
            "server": self.server,
            "profitTarget": self.profitTarget,
            "maxDailyLoss": self.maxDailyLoss,
            "maxLoss": self.maxLoss,
            "rates": self.rates,
            "orderTypeSummary": self.orderTypeSummary,
            "accountSummary": self.accountSummary,
            "tradingJournal": self.tradingJournal,
        }


class ProfitTarget:
    def __init__(self):
        self.top: Decimal = 0
        self.buttom: Decimal = 0
        self.percentage: Decimal = 0
        self.isBreached: bool

    def __json__(self):
        return {
            "top": str(self.top),
            "buttom": str(self.buttom),
            "percentage": str(self.percentage),
            "isBreached": self.isBreached,
        }


class MaxDailyLoss:
    def __init__(self):
        self.top: Decimal = 0
        self.buttom: Decimal = 0
        self.percentage: Decimal = 0
        self.isBreached: bool

    def __json__(self):
        return {
            "top": str(self.top),
            "buttom": str(self.buttom),
            "percentage": str(self.percentage),
            "isBreached": self.isBreached,
        }


class MaxLoss:
    def __init__(self):
        self.top: Decimal = 0
        self.buttom: Decimal = 0
        self.percentage: Decimal = 0
        self.isBreached: bool

    def __json__(self):
        return {
            "top": str(self.top),
            "buttom": str(self.buttom),
            "percentage": str(self.percentage),
            "isBreached": self.isBreached,
        }


class AccountSummary:
    def __init__(self):
        self.oprDate: datetime
        self.trades: int = 0
        self.lots: Decimal = 0
        self.results: Decimal = 0

    def __json__(self):
        return {
            "oprDate": self.oprDate,
            "trades": self.trades,
            "lots": str(self.lots),
            "results": str(self.results),
        }


class Rates:
    def __init__(self):
        self.winRate: Decimal = 0
        self.lossRate: Decimal = 0
        self.winpercentage: Decimal = 0
        self.losspercentage: Decimal = 0

    def __json__(self):
        return {
            "winRate": str(self.winRate),
            "lossRate": str(self.lossRate),
            "winpercentage": str(self.winpercentage),
            "losspercentage": str(self.losspercentage),
        }


class OrderTypeSummary:
    def __init__(self):
        self.buy: Decimal = 0
        self.sell: Decimal = 0
        self.buypercentage: Decimal = 0
        self.sellpercentage: Decimal = 0

    def __json__(self):
        return {
            "buy": str(self.buy),
            "sell": str(self.sell),
            "buypercentage": str(self.buypercentage),
            "sellpercentage": str(self.sellpercentage),
        }


class TradingJournal:
    def __init__(self):
        self.id: int
        self.ticket: Decimal = 0
        self.openDate: datetime
        self.closeDate: datetime
        self.oprType: str
        self.volume: Decimal = 0
        self.symbol: str
        self.openPrice: Decimal = 0
        self.closePrice: Decimal = 0
        self.sl: Decimal = 0
        self.tp: Decimal = 0
        self.swap: Decimal = 0
        self.comm: Decimal = 0
        self.profit: Decimal = 0
        self.pips: Decimal = 0
        self.duration: str

    def __json__(self):
        return {
            "ticket": str(self.ticket),
            "openDate": self.openDate,
            "closeDate": self.closeDate,
            "oprType": self.oprType,
            "volume": str(self.volume),
            "symbol": self.symbol,
            "openPrice": str(self.openPrice),
            "closePrice": str(self.closePrice),
            "sl": str(self.sl),
            "tp": str(self.tp),
            "swap": str(self.swap),
            "comm": str(self.comm),
            "profit": str(self.profit),
            "pips": str(self.pips),
            "duration": self.duration,
        }
