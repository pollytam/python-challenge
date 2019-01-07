
import csv

total_votes=0


candidate_list = {}
dataList = []

with open('election_data.csv',"r") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")

    for row in csvReader:
        dataList.append(row)


for i in range(1, len(dataList)):
    
    # total number of votes
    total_votes = total_votes + 1

    # complete list of candidates who rcv votes

    
    candidate = dataList[i][2]
    VoterID = dataList[i][0]

    if (candidate not in candidate_list):

        candidate_list[candidate]=1
        
    else:
        candidate_list[candidate] = candidate_list[candidate] + 1

print("Election Results")
print(" -------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
      
winner = ""
vote = 0
for candidate in candidate_list:
    
    # percent of votes each candidate won

    percent_votes=(candidate_list[candidate]/total_votes)*100


    # total number of votes each candidates won
    
    print(candidate + " : " + "%0.3f"% (percent_votes) + "%" + "(" + str(candidate_list[candidate]) + ")")
    
    # winner of the election based on popular vote
    
    if (candidate_list[candidate] > vote):
        vote = candidate_list[candidate]
        winner = candidate


print("-------------------------")
print("Winner: " + str(winner))
print("-------------------------")
