def create_row(names):
    seating[names] = seating
    return seating

def get_student_at(row, index):
    if index in row:
        return row[index]
    return None

def swap_seats(row, index1, index2)
    hold_spot = row[1]
    row[1] = row [2]
    row [2] = hold_spot

def remove_student(row, name):
    if name in row:
        row.remove(name)