import csv

roll_list=[ "MSM19B001","MSM19B002","MSM19B003","MSM19B004","MSM19B005","MSM19B006","MSM19B008","MSM19B009","MSM19B010","MSM19B011","MSM19B012","MSM19B013","MSM19B014",
"MSM19B015","MSM19B017","MSM19B018","MSM19B019","MSM19B020","MSM19B021","MSM19B023","MSM19B024","MSM19B025","MSM19B028","MSM19B030","MSM19B031","MSM19B032","MSM19B033",
"MSM19B034","MSM19B035","MSM19B036","MSM19B037","MSM19B038","MSM19B039","MSM19B040","MSM19B041","MSM19B042","MSM19B043","MSM19B044","MSM19B045","MSM19B046","MSM18B031"]

print(roll_list)
with open('sample.csv', 'r') as file:
    reader = csv.reader(file)
       for row in reader:
          fw=row[0].split()[0]
          #print(fw)
          if roll_list[2] == fw:
          print(row)

with open('main.csv', 'r') as file:
    reader_m = csv.reader(file)
    for row in reader_m:
         if row[2].startswith('MSM'):
            print(row[2])


