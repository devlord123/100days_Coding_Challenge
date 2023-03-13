import csv
with open('cafe-data.csv') as file:
    data = csv.reader(file, delimiter=',')
    row_list = []
    for row in data:
        row_list.append(row)

    for row in row_list:
        for item in row:
            print(item)
            if item[0:4] == "http":
                print("Map")
