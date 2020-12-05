import rumps
from extractor import Student
from gui import GUI


class MenuBarApp(rumps.App):
    def __init__(self):
        super(MenuBarApp, self).__init__("MyQUT")
        student = Student()
        student.login()
        self.menu = [f"Current GPA: {student.gpa}", "View Timetable"]

    @rumps.clicked("View Timetable")
    def timetable(self, _):
        gui = GUI("timetable.csv")
        gui.window.show()
        gui.exec()


if __name__ == "__main__":
    MenuBarApp().run()
