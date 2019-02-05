#not solid on what this means but it's in a bunch of activities, I know it means import operation system support or something
#like that, and csv support, but I don't actually get what that means
import os
import csv


# instead of writing out the location of the file every time, I can call up ElectionCSV 
ElectionCSV = os.path.join('election_data.csv')

# declare some variables
TotalVotes = 0 
KhanVotes = 0
CorreyVotes = 0
LiVotes = 0
OTooleyVotes = 0

#reading essentially Election_Data.csv as the variable ElectionData and splitting it at the ,s
#giving us 3 lists of lists
with open(ElectionCSV, 'r') as ElectionData:
    ElectionData = csv.reader(ElectionData, delimiter=',')
    header = next(ElectionData)

#go through the first list of lists in ElectionData and add 1 to the variable TotalVotes
    for Rows in ElectionData: 
        TotalVotes +=1

#In the third list of lists each time the names Khan, Correy, Li, or O'Tooley, are found, add 1 to their corresponding vote counter variables
        if Rows[2] == "Khan": 
            KhanVotes +=1
        elif Rows[2] == "Correy":
            CorreyVotes +=1
        elif Rows[2] == "Li": 
            LiVotes +=1
        elif Rows[2] == "O'Tooley":
            OTooleyVotes +=1

#use prints to check on stuff
#print(TotalVotes)
#print(KhanVotes)
#print(CorreyVotes)
#print(LiVotes)
#print(OTooleyVotes)


# take the things we know nad put them in 2 lists
Candidates = ["Khan", "Correy", "Li","O'Tooley"]
Votes = [KhanVotes, CorreyVotes, LiVotes, OTooleyVotes]

#take the 2 lists above and zip them together in a dictionary called DictionaryCandidatesVotes
#where the key is Candidates
DictionaryCanidatesVotes = dict(zip(Candidates,Votes))
#find the winner by looking for the highest number in our dictionary, and get
#the dictionary key associated with that value and return it as a keyword within the max function
# winner is the keyword associated with the highest value in the dictionary
Winner = max(DictionaryCanidatesVotes,key=DictionaryCanidatesVotes.get)

#change number of votes for each candidate to a percentage of the total number of votes
KhanPercent = (KhanVotes/TotalVotes) * 100
CorreyPercent = (CorreyVotes/TotalVotes) * 100
LiPercent = (LiVotes/TotalVotes) * 100
OTooleyPercent = (OTooleyVotes/TotalVotes) * 100

#use prints to check on stuff
#print(KhanPercent)
#print(CorreyPercent)
#print(LiPercent)
#print(OTooleyPercent)
#print(Winner)



print(f"Election Results")
print(f"____________________________________")
#print total votes with f-string
print(f"Total Votes: {TotalVotes}")
print(f"____________________________________")
#print Name, percentage to the third decimal, and number of votes receieved
print(f"Khan: {KhanPercent:.3f}% ({KhanVotes})")
print(f"Correy: {CorreyPercent:.3f}% ({CorreyVotes})")
print(f"Li: {LiPercent:.3f}% ({LiVotes})")
print(f"O'Tooley: {OTooleyPercent:.3f}% ({OTooleyVotes})")
print(f"____________________________________")
print(f"Winner: {Winner}")
print(f"____________________________________")

#make a file in the current directory called ElectionResults.txt and assign to variable ElectionResults
ElectionResults = os.path.join(".", "ElectionResults.txt")

#use ElectionResults to write to file in ElectionResults with variable Output
with open(ElectionResults,"w") as Output:

# writes to ElectionResults with \n going to the next line
    Output.write(f"Election Results \n")
    Output.write(f"____________________________________ \n")
    Output.write(f"Total Votes: {TotalVotes} \n")
    Output.write(f"____________________________________ \n")
    Output.write(f"Khan: {KhanPercent:.3f}% ({KhanVotes}) \n")
    Output.write(f"Correy: {CorreyPercent:.3f}% ({CorreyVotes}) \n")
    Output.write(f"Li: {LiPercent:.3f}% ({LiVotes}) \n")
    Output.write(f"O'Tooley: {OTooleyPercent:.3f}% ({OTooleyVotes}) \n")
    Output.write(f"____________________________________ \n")
    Output.write(f"Winner: {Winner} \n")
    Output.write(f"____________________________________")