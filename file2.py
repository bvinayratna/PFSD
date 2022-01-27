import csv
from xml.dom.expatbuilder import parseString
#in csv we have reader and writer instead of read() and writer()

f1 = open("student1.csv","r")
data = csv.reader(f1)
next(data)
for s in data:
    if s[3]=="male" and float(s[5])> 9.0:
        print(s[0],s[1],s[4])
f1.close()

#creaete a python script to display students whose gender is male and cgpa is less than 9