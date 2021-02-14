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
        return TimeframeType(idx + 2) if idx <= 2 and idx >= 1 else TimeframeType.INVALID
