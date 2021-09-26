'''Task5_3_part_2 Implement a function which receives the file path with students info and writes CSV
student information to the new file in descending order of age. '''

import data
import csv

def get_top_performers(file_path_r,file_path_w):

    sorted_by_age = []

    with open(file_path_r, encoding='utf-8', mode='r') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=",")

        dicts = [d for d in file_reader]
        sorted_by_age = sorted(dicts, key=lambda d: int(d['age']))

    with open(file_path_w, encoding='utf-8', mode='w') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        file_writer.writerow(['student name', 'age', 'average mark'])
        for cur_dict in sorted_by_age:
            file_writer.writerow([cur_dict['student name'], cur_dict['age'], cur_dict['average mark']])


print(get_top_performers("data/students.csv", "data/sorted_students.csv"))
