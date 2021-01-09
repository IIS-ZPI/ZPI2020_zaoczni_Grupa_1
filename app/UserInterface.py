from app.CommandsList import CommandsList
from app.ArgumentType import ArgumentType
from app.TimeframeType import TimeframeType, print_available_timeframes
from app.Util import parse_timeframe

class UserInterface:
    def show_commands_list(self):
        print("Dostępne opcje:")
        #TODO: print list of all available commands

    def handle_command(self, command):
        #TODO: handle command choosen by user

    def listen_for_user_input(self):
        while True:
            self.show_commands_list()
            try:
                self.handle_command(int(input("Wybierz numer komendy: ")))
            except ValueError:
                print("Niepoprawna komenda")
