# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    day = []
    condition = []
    header = False
    for row in data:
        if header:
            day.append(row[0])
            temperature.append(int(row[1]))
            condition.append(row[2])
        header = True
        print(row)

    print(day)
    print(temperature)
    print(condition)
