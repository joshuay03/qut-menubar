import rumps
from extractor import Student
from gui import GUI


class MenuBarApp(rumps.App):
    def __init__(self):
        super(MenuBarApp, self).__init__("MyQUT")
        self.student = Student('credentials.csv', 'timetable.csv')
        self.student.login()
        self.student.extract_gpa()
        self.student.extract_timetable()
        self.menu = [f"Current GPA: {self.student.gpa}", "View Timetable"]

    @rumps.clicked("View Timetable")
    def timetable(self, _):
        gui = GUI(self.student)
        gui.window.show()
        gui.exec()


if __name__ == "__main__":
    MenuBarApp().run()
