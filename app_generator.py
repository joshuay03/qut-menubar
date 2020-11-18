import rumps
import gui_creator


class MenuBarApp(rumps.App):
    def __init__(self):
        super(MenuBarApp, self).__init__("MyQUT")
        self.menu = ["View Timetable"]

    @rumps.clicked("View Timetable")
    def timetable(self, _):
        gui = gui_creator.GUI()
        gui.window.show()
        gui.exec()


if __name__ == "__main__":
    MenuBarApp().run()
