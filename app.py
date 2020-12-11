import rumps
from gui import *


class MenuBarApp(rumps.App):
    def __init__(self, student):
        self.student = student
        super(MenuBarApp, self).__init__("MyQUT")
        self.menu = ["Login", "Timetable"]
        self.options_gui = OptionsGUI(self.student, self)

    @rumps.clicked("Login")
    def login(self, _):
        if self.student.username == '':
            self.options_gui.window.show()
            self.options_gui.exec()
        else:
            pass  # TODO: Display already logged in message

    @rumps.clicked("Timetable")
    def timetable(self, _):
        if not self.student.timetable_file == '':
            timetable_gui = TimetableGUI(self.student, self)
            timetable_gui.window.show()
            timetable_gui.exec()
        else:
            pass  # TODO: Display extract timetable first message
