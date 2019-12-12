#import os module
import os
#import csv module
import csv

csvPath = os.path.join("..","Resources","02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

#Read CSV file with CSV module
with open (csvPath, newline="") as csvfile:

    csvReader = csv.reader(csvfile,delimiter=",")
    print(csvreader)
