import sys
from app.Command import Command
from app.ArgumentType import ArgumentType
from app.DataPresenter import DataPresenter

CommandsList = [
    Command("sessions",
            DataPresenter.show_sessions,
            "Sesje wzrostowych/spadkowych bez zmian",
            [ArgumentType.BASE_CURRENCY, ArgumentType.TIMEFRAME_ALL]
            ),
    Command("statistics", 
            DataPresenter.show_statistics, 
            "Miary statystyczne",
            [ArgumentType.BASE_CURRENCY, ArgumentType.TIMEFRAME_ALL]
            ),
    Command("ratio_changes",
            DataPresenter.show_ratio_changes,
            "Rozkład zmian pomiędzy dwoma walutami",
            [ArgumentType.BASE_CURRENCY, ArgumentType.COMPARABLE_CURRENCY, ArgumentType.TIMEFRAME_LONG]
            ),
    Command("exit",
            sys.exit,
            "Wyjście",
            []
            )
]
