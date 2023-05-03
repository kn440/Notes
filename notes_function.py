import csv
from datetime import date

filename = "notes.csv"
current_date = date.today()

def rowcount(filename):
    cnt = 0
    with open(filename) as f:
        cr = csv.reader(f)
        for row in cr:
            cnt += 1
    return cnt


def add(name, note):
    with open(filename, mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
        file_writer.writerow([rowcount(filename), name, note,current_date])


def list():
    with open(filename, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=";")
        for row in file_reader:
            print(f' {", ".join(row)}')


def read(number):
    with open(filename, encoding='utf-8') as r_file:
        lines = r_file.readlines()
        print(lines[number])


def change(number,name,note):
    lines2 = []
    with open(filename, mode="r", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=";", lineterminator="\r")
        for line in file_reader:
            if line[0] != number:
                lines2.append(line)
            else:
                 lines2.append([number,name,note,current_date])
                 print(lines2)
    with open(filename, mode="w+", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
        file_writer.writerows(lines2)

def delete(number):
    lines2=[]
    with open(filename, mode="r", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=";", lineterminator="\r")
        for line in file_reader:
            if line[0]!=number:
                lines2.append(line)
            else:
                lines2.append(["","","",""])
                print(lines2)
    with open(filename, mode="w+", encoding='utf-8') as w_file:
            file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
            file_writer.writerows(lines2)