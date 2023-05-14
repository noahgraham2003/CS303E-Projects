# Benford.py
# Noah Graham
# nlg838
# CS303E
# 
# 3/31/23
# This program is used to verify Benford's Law in 2009 US Census data

import os
import os.path

def main():
    # says file doesn't census data doesn't exist
    fileInput = input("Enter the name of a file of census data: ")
    if not os.path.isfile(fileInput):
        print("File does not exist")
        return
    else:
        set1 = set()
        dict1 = {"1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8" : 0, "9" : 0}
        # starts the loop at the second line
        readFile = open(fileInput, "r")
        line = readFile.readline()
        # loops through the txt file and counts the first digit in each population num
        while line:
            line = readFile.readline().split()
            if len(line) == 0:
                break
            set1.add(int(line[-1]))
            number = line[-1]
            firstIndex = number[0]
            dict1[firstIndex]+=1
        readFile.close()
        # gets the total city and unique population counts
        totalCities = 0
        for digit in dict1:
            totalCities += dict1[digit]
        upc = len(set1)
        print("Output written to benford.txt")
        # idk how to do the writing onto benford.txt thing so heres prints:
        writeFile = open("benford.txt","w")
        writeFile.write("Total number of cities: " + str(totalCities)+"\n")
        writeFile.write("Unique population counts: " + str(upc)+"\n")
        writeFile.write("First digit frequency distributions:\n")
        writeFile.write("Digit\tCount\tPercentage\n")
        for i in range(1,10):
            intPop = dict1[str(i)]
            strPop = str(dict1[str(i)])
            percentage = round(intPop * 100/totalCities, 1)
            writeFile.write(str(i)+"\t"+ strPop + "\t" + str(percentage)+"\n")
        writeFile.close()
main()