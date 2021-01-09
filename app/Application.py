from app.UserInterface import UserInterface

class Application:
    def __init__(self):
        self.ui = UserInterface()

    def run(self):
        self.ui.listen_for_user_input()
