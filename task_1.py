import json
from utilities import location


def get_full_name(student):
    return ' '.join([student['name'], student['middle_name'], student['surname']])


# load data
with open(location('data/Students.json'), encoding='utf-8') as f:
    students_list = json.load(f)

# get students full names
students_list = list(map(lambda x: get_full_name(x), students_list))

# sort list by alphabetic
students_list.sort()

# print students
for number, student in enumerate(students_list, start=1):
    print('%s) %s' % (number, student))
