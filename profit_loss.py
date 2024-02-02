from pathlib import Path
import csv

def Profit_And_Loss():
    # Creates a file path to csv file.
    fp = Path.cwd()/"csv_reports"/"Profit_and_Loss.csv"

    # Check if the file exists at the specified path.
    # print(fp.exists()) 

    # Read the csv file.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header.

        # Create an empty list for profit and loss.
        profit_and_loss_record= []

        # Append profit and loss into the profit_and_loss_record list.
        for row in reader:
            # Convert day to integer and net profit to float.
            day = int(row[0])
            net_profit = float(row[4]) 
            # Append to profit_and_loss_record list.
            profit_and_loss_record.append([day, net_profit])

    # print(profit_and_loss_record)

    # Iterate over the list to calculate the day-to-day net profit differences.
    daily_differences = []
    
    # loops the whole profit_and_loss_record from day 12 to day 90.
    for i in range(1, len(profit_and_loss_record)):
        # On a day, a row is made up of the first item which is the day while the second item is the net profit.
        current_day, current_netprofit = profit_and_loss_record[i]
        # Takes data from the day before.
        previous_day, previous_netprofit = profit_and_loss_record[i - 1]

        # Calculate the difference.
        difference = round(current_netprofit - previous_netprofit)
        daily_differences.append([current_day, difference])

    # print(daily_differences)

    # Initialize variables for analysis.
    highest_increment = 0
    highest_increment_day = 0
    highest_decrement = 0
    highest_decrement_day = 0
    deficits = []

    # Analyze the daily differences.
    for record in daily_differences:
        day, difference = record # first item in record is day and second item is difference.

        # Check if the net profit is always increasing or decreasing.
        if difference < 0:
            deficits.append((day, difference))  # Add to deficits if it's a negative difference.
            if difference < highest_decrement:
                highest_decrement = difference # Replace the highest decrement with the new highest difference.
                highest_decrement_day = day # Replace the highest decrement day with the new highest difference day.
        elif difference > 0:
            if difference > highest_increment:
                highest_increment = difference # Replace the highest increment with the new highest difference.
                highest_increment_day = day # Replace the highest increment day with the new highest difference day.

    def get_deficit_amount(deficits):
        """
        - Extract the deficit amount from the deficit record.
        - Returns the deficit amount which is the second item in each record.
        """
        return deficits[1]

    def find_top_3_deficits(deficits):
        """
        - Identify the top 3 deficits.
        - Returns the top 3 days with the highest deficits.
        """
        deficits.sort(key=get_deficit_amount) # sort it in ascending order.
        return deficits[0:3]

    # Determine if net profit is always increasing or always decreasing.
    always_increasing = highest_decrement == 0
    always_decreasing = highest_increment == 0

    # Creates a string to store the final results.
    final_profit_and_loss = ""

    # Scenario 1: Net profit is always increasing.
    if  always_increasing:
        final_profit_and_loss += f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"
        final_profit_and_loss += f"[HIGHEST NET PROFIT SURPLUS] DAY: {highest_increment_day}, AMOUNT: SGD{highest_increment}\n"

    # Scenario 2: Net profit is always decreasing.
    elif always_decreasing:
        final_profit_and_loss += f"[NET PROFIT DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY\n"
        final_profit_and_loss += f"[HIGHEST NET PROFIT DEFICIT] DAY: {highest_decrement_day}, AMOUNT: SGD{highest_decrement}\n"

    # Scenario 3: Net profit fluctuates.
    else:
        for item in deficits:
            day, deficit = item
            final_profit_and_loss += f"[NET PROFIT DEFICIT] DAY: {item[0]}, AMOUNT: SGD{-item[1]}\n"
        
        top_3_deficits = find_top_3_deficits(deficits)

        # If data is fluctuating but only has 1 deficit.
        if len(top_3_deficits) == 1:
           final_profit_and_loss += f"[HIGHEST NET PROFIT DEFICIT] DAY: {top_3_deficits[0][0]}, AMOUNT: SGD{-top_3_deficits[0][1]}\n"
        
        # If data is fluctuating but only has 2 deficit.
        elif len(top_3_deficits) == 2:
            final_profit_and_loss += f"[HIGHEST NET PROFIT DEFICIT] DAY: {top_3_deficits[0][0]}, AMOUNT: SGD{-top_3_deficits[0][1]}\n"
            final_profit_and_loss += f"[2ND HIGHEST NET PROFIT DEFICIT] DAY: {top_3_deficits[1][0]}, AMOUNT: SGD{-top_3_deficits[1][1]}\n"
       
        # If data is fluctuating and gives top 3 deficits.
        elif len(top_3_deficits) == 3:
            final_profit_and_loss += f"[HIGHEST NET PROFIT DEFICIT] DAY: {top_3_deficits[0][0]}, AMOUNT: SGD{-top_3_deficits[0][1]}\n"
            final_profit_and_loss += f"[2ND HIGHEST NET PROFIT DEFICIT] DAY: {top_3_deficits[1][0]}, AMOUNT: SGD{-top_3_deficits[1][1]}\n"
            final_profit_and_loss += f"[3RD HIGHEST NET PROFIT DEFICIT] DAY: {top_3_deficits[2][0]}, AMOUNT: SGD{-top_3_deficits[2][1]}\n"

    return final_profit_and_loss

# Setup the filepath for writing results to a text file named "summary_report.txt"
fp_write = Path.cwd() / "summary_report.txt"

# Call the function to get the profit and loss data.
Profit_And_Loss_data = Profit_And_Loss()

# Write the data to the file.
with fp_write.open(mode="a", encoding="UTF-8") as file:
    file.write(Profit_And_Loss_data)
