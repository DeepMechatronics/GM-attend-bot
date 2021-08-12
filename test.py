import csv

search_string = "MSM18B031"
with open('sample.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        fw=row[0].split()[0]
        #print(fw)
        if search_string == fw:
         print(row)

with open('main.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if search_string == row[2]:
         print(row)


