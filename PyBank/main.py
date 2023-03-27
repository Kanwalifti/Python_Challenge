# Import the csv file and join it with the os path

import csv
import os

file = os.path.join('PyBank/Resources/budget_data.csv')

#creating variable & assuming its value is 0

months = []
total_net_amount = []

#open a file with empty string line with read properties
with open (file, 'r') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=',')

#telling it to use next function for header to go on nextline
    csv_header = next(csvfile)

#creating a list of similar structure 
    for row in readcsv:
        months.append(row[0])
        total_net_amount.append(int(row[1]))

#count the number of months
    month_count = len(months)

#set variable for loop
    i= 1
    j= 0

#Average Change variable

    AverageChange = (total_net_amount[1]- total_net_amount[0])

#Variable for change with no valuein it
    changes=[]

#using "for loop" to calculate monthly changes

    for month in range(month_count - 1):
        AverageChange = (total_net_amount[i] - total_net_amount[j])
        changes.append(int(AverageChange))
        i+=1
        j+=1

#calculate average monthly changeand rounding it with 2 deicmal places
    Average_monthchange = round(sum(changes)/(month_count -1),2)

#finding & creating min & max change variables
    minchange = min(changes)
    maxchange = max(changes)

#return the index value to find the position in the list
    change_index_min = changes.index(minchange)
    change_index_max = changes.index(maxchange)

#finding the minimum & maximum changes in a month
    #min_change_month = months(change_index_min + 1)
    #max_change_month = months(change_index_max + 1)

#print the value

    print("Financial Analysis")
    print("-------------------------")
    print(f"Months: {len(months)}")
    print(f"Total: ${sum(total_net_amount)}")
    print(f"Average Monthly Change:{Average_monthchange}")
    print(f"Greatest Increase in Profits:(${maxchange})")
    print(f"Greatest Decrease in Profits:(${minchange})")


#Write the Analysis in Text File

    fin_analysis = open("Financial Analysis.txt","w")

    fin_analysis.write("Financial Analysis\n")
    fin_analysis.write("-------------------------------")
    fin_analysis.write(f"Months: {int(month)}\n")
    fin_analysis.write(f"Total: ${sum(total_net_amount)}\n")
    fin_analysis.write(f"Average Monthly Change: {Average_monthchange}\n")
    #fin_analysis.write(f"Greatest Increase in Profits: {max_change_month}(${maxchange})\n")
    #fin_analysis.write(f"Greatest Decrease in Profits:{min_change_month}(${minchange})\n")














