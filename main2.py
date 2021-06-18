import csv

try:
    f = open('data.csv', 'r')

    data = csv.reader(f)

    Details = {}

    for datas in data:
        Details[datas[0]] = {"lastname": datas[1], "age": datas[2]}
    print(Details)

except:
    print('File Not Found')