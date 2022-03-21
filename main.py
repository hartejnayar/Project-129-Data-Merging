import csv
import pandas as pd

file1 = "unit_converted_stars.csv"
file2 = "bright_stars.csv"

d1 = []
d2 = []

with open(file1, 'r', encoding='utf-8') as f:
    csvreader = csv.reader(f)

    for i in csvreader:
        d1.append(i)

with open(file2, 'r', encoding='utf-8') as f:
    csvreader = csv.reader(f)

    for i in csvreader:
        d2.append(i)

h1 = d1[0]
h2 = d2[0]

p_d1 = h1[1:]
p_d2 = h2[1:]

p_d = []

h = h1 + h2

for i in p_d1:
    p_d.append(i)

for j in p_d2:
    p_d.append(j)

with open("total_stars.csv", 'w', encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)   
    csvwriter.writerows(p_d)
    
df = pd.read_csv('total_stars.csv')