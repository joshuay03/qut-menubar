from PyQt5.QtWidgets import *


class OptionsGUI(QApplication):
    def __init__(self, student, app):
        self.student = student
        self.app = app
        super(OptionsGUI, self).__init__([])
        self.setStyle('Fusion')
        self.window = QWidget()
        self.layout = QVBoxLayout()
        self.credentials_button = QPushButton("Select Credentials")
        self.timetable_button = QPushButton("Select Timetable")
        self.credentials_button.clicked.connect(self.credentials_clicked)
        self.timetable_button.clicked.connect(self.timetable_clicked)
        self.layout.addWidget(self.credentials_button)
        self.layout.addWidget(self.timetable_button)
        self.window.setLayout(self.layout)

    def credentials_clicked(self):
        self.student.credentials = 'credentials.csv'
        self.student.login()
        self.student.extract_gpa()
        self.app.menu.insert_after("Login", f"Current GPA: {self.student.gpa}")
        self.window.close()
        self.layout.removeWidget(self.credentials_button)
        self.window.setLayout(self.layout)

    def timetable_clicked(self):
        self.student.timetable = 'timetable.csv'
        self.student.extract_timetable()
        self.window.close()


class TimetableGUI(QApplication):
    def __init__(self, student, app):
        self.student = student
        self.app = app
        super(TimetableGUI, self).__init__([])
        self.timetable_csv = self.student.timetable
        self.setStyle('Fusion')
        self.window = QWidget()
        self.layout = QVBoxLayout()
        self.table_widget = self.create_table()
        self.layout.addWidget(self.table_widget)
        self.window.setLayout(self.layout)
        self.window.resize(900, self.table_widget.rowCount() * 45)

    def create_table(self):
        rows = self.student.rows
        table_widget = QTableWidget(len(rows), len(rows[0]))
        row_index = 0
        for row in rows:
            column_index = 0
            for item in row:
                table_widget_item = QTableWidgetItem(item)
                table_widget.setItem(row_index, column_index, table_widget_item)
                column_index += 1
            row_index += 1
        table_widget.resizeColumnsToContents()

        return table_widget
