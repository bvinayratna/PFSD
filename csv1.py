import csv

f = open("product.csv", "r")
data = csv.reader(f)
print(data)

for s in data:
    print(s)