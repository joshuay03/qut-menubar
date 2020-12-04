from _csv import reader


def extract_timetable(timetable_file):
    with open(timetable_file) as csv_file:
        csv_reader = reader(csv_file)
        rows = []
        for row in csv_reader:
            rows.append(row)

    return rows
