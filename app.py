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
        self.options_gui.window.show()
        self.options_gui.exec()

    @rumps.clicked("Timetable")
    def timetable(self, _):
        if not self.student.timetable == '':
            timetable_gui = TimetableGUI(self.student, self)
            timetable_gui.window.show()
            timetable_gui.exec()
        else:
            self.options_gui.window.show()
            self.options_gui.exec()
