from timetable_extractor import extract_timetable
from PyQt5.QtWidgets import *


class GUI(QApplication):
    def __init__(self, timetable_csv):
        super(GUI, self).__init__([])
        self.timetable_csv = timetable_csv
        self.setStyle('Fusion')
        self.window = QWidget()
        self.layout = QVBoxLayout()
        self.table_widget = self.create_table()
        self.window.resize(900, self.table_widget.rowCount() * 45)
        self.layout.addWidget(self.table_widget)
        self.window.setLayout(self.layout)

    def create_table(self):
        rows = extract_timetable(timetable_file=self.timetable_csv)
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


if __name__ == '__main__':
    gui = GUI("timetable.csv")
    gui.window.show()
    gui.exec()
