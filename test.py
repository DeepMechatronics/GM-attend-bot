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
    reader_m = csv.reader(file)
    for row in reader_m:
         if row[2].startswith('MSM'):
            print(row[2])


