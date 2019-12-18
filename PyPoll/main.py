#import os module
import os
#import csv module
import csv

csvPath = os.path.join("","Resources","02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

print(f"Election Results\n-------------------------")
#Read CSV file with CSV module
with open (csvPath, newline="") as csvFile:

    csvReader = csv.reader(csvFile,delimiter=",")
    csvHeader = next(csvReader)
    totalVotes = 0
    khanVotes = []
    correyVotes = []
    liVotes = []
    otooleyVotes = []
    for row in csvReader:
        #Track votes based on candidate
        #Store votes in individual lists
        if row[2] == "Khan":
            khanVotes.append(int(row[0]))
        elif row[2] == "Correy":
            correyVotes.append(int(row[0]))
        elif row[2] == "Li":
            liVotes.append(int(row[0]))
        elif row[2] == "O'Tooley":
            otooleyVotes.append(int(row[0]))

    #Calculate total votes for all candidates
    totalVotes = len(khanVotes)+len(correyVotes)+len(liVotes)+len(otooleyVotes)
    #Total votes of individual candidates
    khanTotalVotes = len(khanVotes)
    correyTotalVotes = len(correyVotes)
    otooleyTotalVotes = len(otooleyVotes)
    liTotalVotes = len(liVotes)
    #Create dictionary to store total votes and percentage
    candidates = ["Khan","Correy","Li","O'Tooley"]
    candidateTotal = [khanTotalVotes,correyTotalVotes,liTotalVotes,otooleyTotalVotes]
    percentTotal = [float(khanTotalVotes/totalVotes),float(correyTotalVotes/totalVotes),float(liTotalVotes/totalVotes),float(otooleyTotalVotes/totalVotes)]
    print(f"Total Votes: {totalVotes}\n-------------------------")
    print(f"Khan: {round((percentTotal[0]*100),3)}% ({candidateTotal[0]})")
    print(f"Correy: {round((percentTotal[1]*100),3)}% ({candidateTotal[1]})")
    print(f"Li: {round((percentTotal[2]*100),3)}% ({candidateTotal[2]})")
    print(f"O'Tooley: {round((percentTotal[3]*100),3)}% ({candidateTotal[3]})")
    print("-------------------------")
    #The winner based on index locations
    higestVotes = max(candidateTotal)
    highestIndex = candidateTotal.index(higestVotes)
    print(f"Winner: {candidates[highestIndex]}\n-------------------------")
    #Write result to txt file
    #Open results.txt
    file = open("results.txt","w")
    print(f"Total Votes: {totalVotes}\n-------------------------",file=file)
    print(f"Khan: {round((percentTotal[0]*100),3)}% ({candidateTotal[0]})",file=file)
    print(f"Correy: {round((percentTotal[1]*100),3)}% ({candidateTotal[1]})",file=file)
    print(f"Li: {round((percentTotal[2]*100),3)}% ({candidateTotal[2]})",file=file)
    print(f"O'Tooley: {round((percentTotal[3]*100),3)}% ({candidateTotal[3]})",file=file)
    print("-------------------------",file=file)
    print(f"Winner: {candidates[highestIndex]}\n-------------------------",file=file)
    file.close()
