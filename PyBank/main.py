import os
import csv

f=open("Output//output.txt","w")
csvpath = "Resources//budget_data.csv"

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csvheader= next(csvfile)

    Months=0
    Total_amount = 0
    Increase = []
    Fechas = []
    Valor=0
    for row in csvreader:
        Total_amount= Total_amount + int(row[1])
        Increase.append(-int(Valor)+int(row[1]))
        Fechas.append(row[0])
        Valor=row[1]
        Months+=1
Tabla=dict(zip(Increase,Fechas))
Mayor=max(Tabla.keys())
Menor=min(Tabla.keys())
Increase.pop(0)

Suma=0
for i in Increase:
    Suma=Suma+i

#To file .txt
print("Financial Analisys ",file=f)
print("------------------------------------- ",file=f)
print("Total Months:  " + str(Months),file=f)
print("Total:  $" + str(Total_amount),file=f)
print("Average Change:  $" + str(round(Suma/(Months-1),2)),file=f)
print("Greatest Increase in Profits: " + Tabla.get(Mayor) + " $ " + str(Mayor),file=f)
print("Greatest Decrease in Profits: " + Tabla.get(Menor) + " $ " + str(Menor),file=f)

#To Terminal
print("Financial Analisys ")
print("------------------------------------- ")
print("Total Months:  " + str(Months))
print("Total:  $" + str(Total_amount))
print("Average Change:  $" + str(round(Suma/(Months-1),2)))
print("Greatest Increase in Profits: " + Tabla.get(Mayor) + " $ " + str(Mayor))
print("Greatest Decrease in Profits: " + Tabla.get(Menor) + " $ " + str(Menor))

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
