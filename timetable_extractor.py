import csv


def extract_timetable(timetable_file):
    with open(timetable_file) as csv_file:
        csv_reader = csv.reader(csv_file, dialect='excel')
        rows = []
        for row in csv_reader:
            rows.append(row)

    return rows
