'''Task5_3_part_1. File `data/students.csv` stores information about students in [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) format.
This file contains the student’s names, age and average mark.
1) Implement a function which receives file path and returns names of top performer students
```python
def get_top_performers(file_path, number_of_top_students=5):
    pass '''

import data
import csv

def get_top_performers(file_path, number_of_top_students=5):
    with open(file_path, encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=",")

        # reading pairs Name - Mark
        all_students = {}
        for row in file_reader:
            all_students[row["student name"]] = row["average mark"]

        # sorting pairs
        sorted_by_mark = sorted(all_students.items(),
                                key=lambda item: float(item[1]),
                                reverse=True)

        # getting top students
        top_students = []
        for i in range(number_of_top_students):
            sorted_st = sorted_by_mark[i][0]
            top_students.append(sorted_st)

    return top_students

print(get_top_performers("data/students.csv"))

