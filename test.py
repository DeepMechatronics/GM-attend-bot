import csv
with open('sample.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open('main.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

