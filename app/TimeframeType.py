from enum import Enum
from app.ArgumentType import ArgumentType

class TimeframeType(Enum):
    INVALID = -1
    WEEK = 1
    TWO_WEEKS = 2
    MONTH = 3
    #LONG
    QUARTER = 4
    YEAR = 5

def print_available_timeframes(timeframeType):
    names = ["Tydzień", "Dwa tygodnie", "Miesiąc", "Kwartał", "Rok"]
    for idx, name in enumerate(names[2:4]) if timeframeType == ArgumentType.TIMEFRAME_LONG else enumerate(names):
        print(f"{idx+1}. {name}")
