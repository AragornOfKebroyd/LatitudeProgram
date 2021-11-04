#Ben Tinsley
#Lattitude thing
#Imports
import json
import importing

#Vars
data = []

#Functions
def addLattitude(city,lattitude):
    with open('data.json') as json_file: 
        data = json.load(json_file)
    data.append({
        "City":str(city),
        "Lattitude":lattitude
    })
    return data

#Main
def main():
    #check if data.json exists and if it doesnt make it
    try:
        with open('data.json') as json_file: 
            data = json.load(json_file)
    except Exception as e:
        print("importing...")
        importing.thingy()
        with open('data.json') as json_file: 
            data = json.load(json_file)
        print("finnished importing!")
    #User Interface
    while True:
        choice = input("\n1. Check if a capital is North or South of another capital\n2. View the database\n3. Delete a value from the database\n\n:")[0]
        if choice not in ["1","2","3"]:
            print("Enter a valid choice.\n")
        else:
            if choice == "1": #Check if a capital is North or South of another capital
                city_one = input("Enter city 1:")
                city_two = input("Enter city 2:")
                for x in data:
                    if x["City"].lower() == city_one.lower() and achieved:
                        city_one_latitude = x["Lattitude"]
                        print(city_one)
                    elif x["City"].lower() == city_two.lower():
                        city_two_latitude = x["Lattitude"]
                        print(city_two)
                if isCity == True:
                    compareLat = float(input("What is the latitude of the city you want to compare to {}.\n(put southern lattitudes as negative number)\n:".format(chosenCity)))
                    if compareLat > Lat:
                        print("The city at the lattitude you entered is "+str(round(compareLat-Lat,4))+" degrees north of {}".format(chosenCity))
                    elif compareLat < Lat:
                        print("The city at the lattitude you entered is "+str(round(Lat-compareLat,4))+" degrees south of {}".format(chosenCity))
                    else:
                        print("The city at the lattitude you entered is at the same lattitude as {}".format(chosenCity))
            elif choice == "2": #View the database
                with open('data.json') as json_file: 
                    data = json.load(json_file)
                print(json.dumps(data, indent=4, sort_keys=True))
            elif choice == "3": #Delete a value from the database
                with open('data.json') as json_file: 
                    data = json.load(json_file)
                if data != []:
                    cities = []
                    for x in data:
                        cities.append(x["City"])
                    while True:
                        option = input("Options:\n" + str(cities) + "\n:")
                        if option in cities:
                            break
                        else:
                            print("Enter a valid city\n")
                    for x in data:
                        if x["City"] == option:
                            data.remove(x)
                    with open("data.json","w") as outfile: #Read all the data
                        json.dump(data, outfile)
                else:
                    print("There is nothing to delete, the database is empty.\n")

#Check if imported or run
if __name__ == "__main__":
    main()
