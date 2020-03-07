import os
import csv

f=open("Output//output.txt","w")

csvpath1 = "Resources//election_data.csv"

with open(csvpath1) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csvheader= next(csvfile)

    Votes=0
    Candidates = []
    for row in csvreader:
        Votes+=1
        Candidates.append(row[2])

#To file
print("\n\n\nElection Results ",file=f)
print("------------------------------------- ",file=f)
print("Total Votes:  " + str(Votes),file=f)
print("------------------------------------- ",file=f)

#To terminal
print("\n\n\nElection Results ")
print("------------------------------------- ")
print("Total Votes:  " + str(Votes))
print("------------------------------------- ")

unicos=[]
for i in Candidates:
    if i not in unicos:
        unicos.append(i)

a=0
Winner=0
for i in unicos:
    Votos_count= Candidates.count(unicos[a])
    Votos_percentage = round(((Votos_count/Votes)*100),0)
    print(unicos[a] + ": " + str(Votos_percentage)+ "%  ("+ str(Votos_count)+")",file=f)
    print(unicos[a] + ": " + str(Votos_percentage)+ "%  ("+ str(Votos_count)+")")
    if Votos_count > Winner:
        Winner=Votos_count
        Winner_Candidate=unicos[a]
    a=a+1

#To file
print("------------------------------------- ",file=f)
print("Winner:  " + Winner_Candidate ,file=f)

#To Terminal
print("------------------------------------- ")
print("Winner:  " + Winner_Candidate )

f.close()
