import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Opening and reading CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    

    csv_header = next(csvreader, None)
    
    # Printing the number of months in CSV
    Total_Months = 0
    previous_value = 0
    max_increase = 0
    max_increase_date = None
    max_decrease = 0
    max_decrease_date = None
    Total_profit = 0
    Total_Change = 0

    for row in csvreader:
        Total_Months += 1
        Total_profit += int(row[1])
        change = 0

        # Calculate and store the change in Profit/Losses
        current_value = int(row[1])
        if previous_value != 0:
            change = current_value - previous_value
            Total_Change += change


            # store max and min increase amount and date
            if change > max_increase:
                max_increase = change
                max_increase_date = row[0]

            if change < max_decrease:
                max_decrease = change
                max_decrease_date = row[0]    

        previous_value = current_value


print("Financial Analysis", end = '\n\n')

print("-" * 100, end = '\n\n')
    
print(f'Total Months: {Total_Months}', end = '\n\n')

# Calculate total profit/loss
print(f'Total Profit/Loss: ' + "$" + str(Total_profit), end = '\n\n')

# Calculate average change in Profit/Losses
average_change = Total_Change / (Total_Months - 1) if Total_Months else 0
rounded_avg_change = round(average_change, 2)
print(f'Average Change: ' + "$" + str(rounded_avg_change), end = '\n\n')

# Greatest increase in profits (date and amount)
print(str(max_increase_date) + " " + "($" + str(max_increase) + ")", end = '\n\n')

print(str(max_decrease_date) + " " + "($" + str(max_decrease) + ")")