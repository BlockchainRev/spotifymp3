import csv
import functions
def generate_search(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    search_list = []
    for item in data:
        search_list.append(item[0]+' '+item[1])
    search_list.pop(0)
    print(search_list)

generate_search('UKR.csv')

