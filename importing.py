import csv
import json
data = []
def thingy():
    with open("locations.csv","r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            data.append({
                "City" : row[0],
                "Lattitude" : float(row[1])
                })
            line_count += 1
        print(f'Processed {line_count} lines.')
        with open("data.json","w") as json_file:
            json.dump(data, json_file)

def main():
    thingy()

if __name__ == "__main__":
    main()
