# File: Project3.py
# Student: Noah Graham
# UT EID: nlg838
# Course Name: CS303E
# 
# Date Created: 4/18/23
# Date Last Modified: 4/21/23
# Description of Program: Reads census data and allows a user to interact with it

import os
import os.path

def help():
    print("Enter any of the following commands:")
    print("\033[1m" + "Help" + "\033[0m" + " - list available commands;")
    print("\033[1m" + "Quit" + "\033[0m" + " - exit this dashboard;")
    print("\033[1m" + "Cities" + "\033[0m" + " - list all Texas cities;")
    print("\033[1m" + "Census" + "\033[0m" + " <cityName>/Texas - population in 2020 census by specified city or statewide;")
    print("\033[1m" + "Estimated" + "\033[0m" + " <cityName>/Texas - estimated population in 2023 by specified city or statewide.")
    print("\033[1m" + "Growth" + "\033[0m" + " <cityName>/Texas - percent change from 2020 to 2023, by city or statewide.")
    print()

def loopThrough():
    dict = {}
    readFile = open("citiesData.csv", "r")
    line = readFile.readline()
    sum20 = 0
    sum23 = 0
    cityList = []
    while line:
        if line[0] == "#":
            line = readFile.readline()
            continue
        else:
            line = line.strip()
            if line:
                parts = line.split(",")
                if len(parts) >= 4:
                    pop2020 = int(parts[1])
                    pop2023 = int(parts[0])
                    name = parts[3]
                    lowerName = name.lower()
                    finalName = lowerName[1:-1]
                    tuple = (pop2020, pop2023)
                    dict[finalName] = tuple
                    sum20 += pop2020
                    sum23 += pop2023
                    cityList.append(name)
        line = readFile.readline()
    sortedcityList = sorted(cityList)
    texasTuple = (sum20, sum23)
    dict["Texas"] = texasTuple
    readFile.close()
    return (dict, sortedcityList)

def findCommand(command, argument = ""):
    dict, sortedcityList = loopThrough()
    if command != "help" and command != "quit" and command != "cities" and command != "census" and command != "estimated" and command != "growth":
        print("Command is not recognized. Try again!")
        print()

    elif command == "help": # prints out the list of commands again
        help()
        print()

    elif command == "quit": # prints an exit message and exits the program
        print("\033[1m"+"Thank you for using the Texas Cities Population Database Dashboard.  Goodbye!"+"\033[0m")
        quit()

    elif command == "cities": # prints the sorted list of cities with 10 items per line
        counter = 0
        for city in sortedcityList:
            if counter % 10 == 0 and counter != 0:
                print()
            print(city, end=" ")
            counter += 1
        print()

    elif command == "census": # prints the 2020 population data for a given city or for Texas
        if argument == "Texas":
            print("Texas' total population in the 2020 Census: ", dict["Texas"][0])
        elif argument.lower() in dict:
            print(argument, "'s total population in the 2020 Census: ", dict[argument.lower()][0])
        else:
            print("City", argument, "is not recognized.")
        print()
        
    elif command == "estimated": # prints the 2023 population data for a given city or for Texas
        if argument == "Texas":
            print("Texas' estimated population in the 2023 Census: ", dict["Texas"][1])
        elif argument.lower() in dict:
            print(argument, "'s estimated population in the 2023 Census: ", dict[argument.lower()][1])
        else:
            print("City", argument,"is not recognized.")
        print()

    elif command == "growth": # prints the percent growth from 2020 - 2023
        if argument == "Texas":
            percentGrowth = ((dict[argument][1] - dict[argument][0]) / dict[argument][0]) * 100.0
            print(argument, "had percent population change 2020 to 2023: {:.2f}%".format(percentGrowth))
        elif argument.lower() in dict:
            percentGrowth = ((dict[argument.lower()][1] - dict[argument.lower()][0]) / dict[argument.lower()][0]) * 100.0
            print(argument, "had percent population change 2020 to 2023: {:.2f}%".format(percentGrowth))
        else:
            print("City", argument,"is not recognized.")
        print()


    
def query():
    # intro text
    print("\033[1m" + "Welcome to the Texas Cities Population Dashboard." + "\033[0m")
    print("This provides census data from the 2020 census and ")
    print("estimated population data in Texas as of 2023.")
    print()
    print("Creating dictionary from file: citiesData.csv")
    print()
    help() # prints list of commands

    while True:
        commandInput = input("\033[1m" + "Please enter a command: " + "\033[0m")
        # Parse the command.  Note that the city name may contain multiple words.
        commWords = commandInput.split()
        # Extract the first word in the command.  It should be one of: help,
        # quit, cities, census, estimated, growth. Lowercase it because we 
        # don't want case to matter for the command.
        comm = commWords[0].lower()
        # Extract the rest of the words and re-assemble them into a single string, 
        # separated by spaces. This should either be 'Texas' or a city name. 
        args = commWords[1:]
        arg = " ".join(args)
        findCommand(comm,arg)

def main():
    query()
main()