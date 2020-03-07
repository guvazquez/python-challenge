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

f.close()
