# always import the library to use
import csv

total_months = 0
total_net = 0
sum_change = 0
avg_change = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month =""
greatest_decrease_month =""

avg_change = 0.0

dataList = []

# opening the file as "r" read only
with open ('budget_data.csv',"r") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')

# inserting file rows into the dataList to work
    for row in csvReader:
        dataList.append(row)

# loop the list
for i in range(1,len(dataList)):
        
    # total months
    total_months = total_months + 1

    # Total net over entire period
    total_net = total_net + int(dataList[i][1])

# loop the list
for i in range(1,len(dataList)-1):
      
    # Avg change in between the months
    sum_change = sum_change + int(dataList[i+1][1]) - int(dataList[i][1])

    # greatest incraese profits (date and amt)
    
    change = int(dataList[i+1][1]) - int(dataList[i][1])

    if (change > greatest_increase):
        greatest_increase = change 
        greatest_increase_month = dataList[i+1][0]
        
    # greatest decrease profits (date and amt)
    if (change < greatest_decrease):
        greatest_decrease = change 
        greatest_decrease_month = dataList[i+1][0]
        
# Avg change in between the months
avg_change = sum_change/(total_months-1)

#print results table

print(" Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_net))
print("Average  Change: $" + str(avg_change))
print("Greatest Increase in Profits: "+ str(greatest_increase_month)+ " $"+str(greatest_increase))
print("Greatest Decrease in Profits: " + str(greatest_decrease_month)+ " $"+str(greatest_decrease))


