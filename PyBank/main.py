#import os module
import os
#import csv module
import csv

csvPath = os.path.join("","Resources","02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

print(f"Financial Analysis\n----------------------------")
#Read CSV file with CSV module
with open (csvPath, newline="") as csvFile:

    csvReader = csv.reader(csvFile,delimiter=",")
    #print(csvReader)
    #Count number of rows in csv csv file
    csvHeader = next(csvReader)
    #print(f"Header: {csvHeader}")
    totalProfitLoss = 0
    rowCount = 0
    data = []
    months = []
    for row in csvReader:
        #Iterate through csv and sum profits
        #Store in data list
        totalProfitLoss += int(row[1])
        data.append(int(row[1]))
        #Store months in months list
        months.append(row[0])
        rowCount += 1

    changeMonthOverMonth = []
    for i in range(len(data)-1):
        #Store month over month data in changeMonthOverMonth
        changeMonthOverMonth.append(data[i+1]-data[i])
    #Find max and min value of changeMonthOverMonth list
    #Use index of each value to find max and min month
    maxValue = max(changeMonthOverMonth)
    maxIndex = changeMonthOverMonth.index(maxValue)
    minValue = min(changeMonthOverMonth)
    minIndex = changeMonthOverMonth.index(minValue)
    #Desired outputs
    print(f"Total Months: {rowCount}")
    print(f"Total Months: ${totalProfitLoss}")
    print(f"Average Change: ${round((data[rowCount-1]-data[0])/(rowCount-1),2)}")
    print(f"Greatest Increase in Profits: {months[maxIndex + 1]} ${max(changeMonthOverMonth)}")
    print(f"Greatest Decrease in Profits: {months[minIndex + 1]} ${min(changeMonthOverMonth)}")

    file = open("results.txt","w")
    print(f"Total Months: {rowCount}",file=file)
    print(f"Total Months: ${totalProfitLoss}",file=file)
    print(f"Average Change: ${round((data[rowCount-1]-data[0])/(rowCount-1),2)}",file=file)
    print(f"Greatest Increase in Profits: {months[maxIndex + 1]} ${max(changeMonthOverMonth)}",file=file)
    print(f"Greatest Decrease in Profits: {months[minIndex + 1]} ${min(changeMonthOverMonth)}",file=file)
    file.close()
