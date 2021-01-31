from app.ArgumentType import ArgumentType
from app.TimeframeType import TimeframeType

def parse_timeframe(option, timeframeType):
    idx = 0
    try:
        idx = int(option)
    except ValueError:
        return TimeframeType.INVALID
    if timeframeType == ArgumentType.TIMEFRAME_ALL:
        return TimeframeType(idx)
    elif timeframeType == ArgumentType.TIMEFRAME_LONG:
        if (idx < 3):
            return TimeframeType(idx + 2)
        else:
            return TimeframeType.INVALID
