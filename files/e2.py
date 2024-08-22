import csv
with open("../weather.csv", "r") as file:
    data=list(csv.reader(file))
city=input("enter the city name")
for row in data:
    if row[0]==city:
        print(row[1])
print(data)