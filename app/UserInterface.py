from app.CommandsList import CommandsList
from app.ArgumentType import ArgumentType
from app.TimeframeType import TimeframeType, print_available_timeframes
from app.Util import parse_timeframe

class UserInterface:
    def show_commands_list(self):
        print("Dostępne opcje:")
        for idx, commandNr in enumerate(CommandsList):
            print(f"{idx+1}. {commandNr.description}")

    def handle_command(self, commandNr):
        if commandNr not in range(1, len(CommandsList)+1):
            print("Niepoprawna komenda")
            return

        args = []
        for argType in CommandsList[commandNr-1].argumentTypes:
            try:
              if argType == ArgumentType.BASE_CURRENCY:
                  args.append(input("Podaj walutę (kod, np. USD): "))
              elif argType == ArgumentType.COMPARABLE_CURRENCY:
                  args.append(input("Podaj drugą walutę (kod, np. USD): "))
              elif argType in [ArgumentType.TIMEFRAME_ALL, ArgumentType.TIMEFRAME_LONG]:
                  print_available_timeframes(argType)
                  timeframe = parse_timeframe(input("Podaj okres czasu:"), argType)
                  if timeframe == TimeframeType.INVALID:
                      print("Niepoprawny argument")
                      return
                  args.append(timeframe)
            except EOFError as error:
                print("Niepoprawny argument")

        result = CommandsList[commandNr-1].method(*args)
        if result:
            print(f"Wynik: {result}")
        input("Wciśnij enter aby kontynuować...")

    def listen_for_user_input(self):
        while True:
            self.show_commands_list()
            try:
                self.handle_command(int(input("Wybierz numer komendy: ")))
            except ValueError:
                print("Niepoprawna komenda")
