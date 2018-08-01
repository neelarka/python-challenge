import os
import csv
from pathlib import Path 
filepath = Path("../../Desktop/election_data.csv")
with open(filepath, newline="", encoding='utf-8' ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    reader = csv.reader(csvfile)
    next(reader, None)
    Voter_Id = []
    county = []
    candidate = []
    for row in csvreader:
                Voter_Id.append(row[0])
                county.append(row[1])
                candidate.append(row[2])
length = len(Voter_Id)
# print ("The Total Votes : " + str(length))

# Votes For Khan
candidates = []
for name in candidate:
     if name == "Khan":
        candidates.append(candidate)
    
#print(candidates)
#print(county)
length1 = len(candidates)
#print ("The Total Votes for Khan: " + str(length1))
percentage_Khan = length1/length
#print(percentage_Khan)

# Votes For Correy
candidates1 = []
for name in candidate:
     if name == "Correy":
        candidates1.append(candidate)
    
#print(candidates)
#print(county)
length2 = len(candidates1)
#print ("The Total Votes for Correy: " + str(length2))
percentage_Correy = length2/length
#print(percentage_Correy)

# Votes For Li

candidates2 = []
for name in candidate:
     if name == "Li":
        candidates2.append(candidate)
length3 = len(candidates2)
#print ("The Total Votes for Li: " + str(length3))
percentage_Li = length3/length
#print(percentage_Li)

# Votes For O'Tooley
candidates3 = []
for name in candidate:
     if name == "O'Tooley":
        candidates3.append(candidate)
length4 = len(candidates3)
#print ("The Total Votes for O'Tooley: " + str(length4))
percentage_O_Tooley = length4/length
#print(percentage_O_Tooley)

print("Election Results" + "\n --------------------")
print ("The Total Votes : " + str(length) + "\n --------------------")
print("Khan: " + str("%.3f" % percentage_Khan)  + " (" + str(length1)+ ")" )
print("Correy: " + str("%.3f" % percentage_Correy)  + " (" + str(length2)+ ")" )
print("Li: " + str("%.3f" % percentage_Li)  + " (" + str(length3)+ ")" )
print("O'Tooley: " + str("%.3f" % percentage_O_Tooley)  + " (" + str(length4)+ ")" )
print("--------------------")

winner = max(length1, length2, length3, length4)
if winner == length1 :
    print(" Winner : " + "Khan" )
elif winner == length2 :
    print(" Winner : " + "Correy" )
elif winner == length3 :
    print(" Winner : " + "Li" )
else :
    print(" Winner : " + "O'Tooley" )
print("--------------------")

text_file = open("Output_PyPoll.txt", "w")

text_file.write("Election Results \n" )
text_file.write("\n--------------------")
text_file.write("The Total Votes : " + str(length) + "\n")
text_file.write("\n--------------------\n")
text_file.write("Khan: " + str("%.3f" % percentage_Khan)  + " (" + str(length1)+ ")" )
text_file.write("\n Li: " + str("%.3f" % percentage_Li)  + " (" + str(length3)+ ")" )
text_file.write("\n O'Tooley: " + str("%.3f" % percentage_O_Tooley)  + " (" + str(length4)+ ") \n" )
text_file.write("\n--------------------\n")
winner = max(length1, length2, length3, length4)
if winner == length1 :
    text_file.write(" Winner : " + "Khan" )
elif winner == length2 :
    text_file.write(" Winner : " + "Correy" )
elif winner == length3 :
    text_file.write(" Winner : " + "Li" )
else :
    text_file.write(" Winner : " + "O'Tooley" )
text_file.write("\n--------------------")
text_file.close()

