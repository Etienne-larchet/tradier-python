# generated by datamodel-codegen:
#   filename:  market.json
#   timestamp: 2021-10-06T15:42:08+00:00

# from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class QuoteItem(BaseModel):
    symbol: str
    description: str
    exch: str
    type: str
    last: Optional[float]
    change: Optional[float]
    volume: int
    open: Optional[float]
    high: Optional[float]
    low: Optional[float]
    close: Any
    bid: float
    ask: float
    change_percentage: Optional[float]
    average_volume: int
    last_volume: int
    trade_date: int
    prevclose: Optional[float]
    week_52_high: float
    week_52_low: float
    bidsize: int
    bidexch: str
    bid_date: int
    asksize: int
    askexch: str
    ask_date: int
    root_symbols: Optional[str] = None
    underlying: Optional[str] = None
    strike: Optional[float] = None
    open_interest: Optional[int] = None
    contract_size: Optional[int] = None
    expiration_date: Optional[str] = None
    expiration_type: Optional[str] = None
    option_type: Optional[str] = None
    root_symbol: Optional[str] = None


class Quotes(BaseModel):
    quote: List[QuoteItem]


class Greeks(BaseModel):
    delta: float
    gamma: float
    theta: float
    vega: float
    rho: float
    phi: float
    bid_iv: float
    mid_iv: float
    ask_iv: float
    smv_vol: float
    updated_at: str


class OptionItem(BaseModel):
    symbol: str
    description: str
    exch: str
    type: str
    last: Any
    change: Any
    volume: int
    open: Any
    high: Any
    low: Any
    close: Any
    bid: float
    ask: float
    underlying: str
    strike: float
    change_percentage: Any
    average_volume: int
    last_volume: int
    trade_date: int
    prevclose: Any
    week_52_high: float
    week_52_low: float
    bidsize: int
    bidexch: str
    bid_date: int
    asksize: int
    askexch: str
    ask_date: int
    open_interest: int
    contract_size: int
    expiration_date: str
    expiration_type: str
    option_type: str
    root_symbol: str
    greeks: Greeks


class Options(BaseModel):
    option: List[OptionItem]


class Strikes(BaseModel):
    strike: List[float]


class Expirations(BaseModel):
    date: List[str]


class Symbol(BaseModel):
    rootSymbol: str
    options: List[str]


class DayItem(BaseModel):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int


class History(BaseModel):
    day: List[DayItem]


class Datum(BaseModel):
    time: str
    timestamp: int
    price: float
    open: float
    high: float
    low: float
    close: float
    volume: int
    vwap: float


class Series(BaseModel):
    data: List[Datum]


class SecurityItem(BaseModel):
    symbol: str
    exchange: str
    type: str
    description: str


class Securities(BaseModel):
    security: List[SecurityItem]


class Clock(BaseModel):
    date: str
    description: str
    state: str
    timestamp: int
    next_change: str
    next_state: str


class Premarket(BaseModel):
    start: str
    end: str


class Open(BaseModel):
    start: str
    end: str


class Postmarket(BaseModel):
    start: str
    end: str


class DayItem1(BaseModel):
    date: str
    status: str
    description: str
    premarket: Premarket
    open: Open
    postmarket: Postmarket


class Days(BaseModel):
    day: List[DayItem1]


class Calendar(BaseModel):
    month: int
    year: int
    days: Days


class Re(BaseModel):
    quotes: Optional[Quotes] = None
    options: Optional[Options] = None
    strikes: Optional[Strikes] = None
    expirations: Optional[Expirations] = None
    symbols: Optional[List[Symbol]] = None
    history: Optional[History] = None
    series: Optional[Series] = None
    securities: Optional[Securities] = None
    clock: Optional[Clock] = None
    calendar: Optional[Calendar] = None


class Model(BaseModel):
    res: List[Re]
