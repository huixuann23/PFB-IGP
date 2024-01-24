from pathlib import Path
import csv

# Creates a file path to csv file.
fp = Path.cwd()/"csv_reports"/"Cash_on_Hand.csv"

# Check if the file exists at the specified path.
# print(fp.exists()) 

# Read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # Create an empty list for cash on hand.
    cash_on_hand_record= []

    # Append cash on hand into the cash_on_hand_record list.
    for row in reader:
        # Convert day to integer and cash on hand to float.
        day = int(row[0])
        cash_on_hand = float(row[1]) 
        # Append to cash_on_hand_record list.
        cash_on_hand_record.append([day, cash_on_hand])

# print(cash_on_hand_record)

# Iterate over the list to calculate the day-to-day cash differences
daily_differences = []

for i in range(1, len(cash_on_hand_record)):
    current_day, current_cash = cash_on_hand_record[i]
    previous_day, previous_cash = cash_on_hand_record[i - 1]

    # Calculate the difference
    difference = round(current_cash - previous_cash)
    daily_differences.append([current_day, difference])

# print(daily_differences)

# Initialize variables for analysis
highest_surplus = 0
highest_surplus_day = 0
highest_deficit = 0
highest_deficit_day = 0
deficits = []

# Analyze the daily differences
for record in daily_differences:
    day, difference = record

    # Check if the cash-on-hand is always increasing or decreasing
    if difference < 0:
        deficits.append((day, difference))  # Add to deficits if it's a negative difference
        if difference < highest_deficit:
            highest_deficit = difference
            highest_deficit_day = day
    elif difference > 0:
        if difference > highest_surplus:
            highest_surplus = difference
            highest_surplus_day = day

def get_deficit_amount(deficits):
    """
    - Extract the deficit amount from the deficit record.
    - Returns the deficit amount which is the second item in each record
    """
    return deficits[1]

def find_top_3_deficits(deficits):
    """
    - Identify the top 3 deficits.
    - Returns the top 3 days with the highest deficits.
    """
    deficits.sort(key=get_deficit_amount)
    return deficits[0:3]

# Determine if cash-on-hand is always increasing or always decreasing
always_increasing = highest_deficit == 0
always_decreasing = highest_surplus == 0

# Creates a string to store the final results.
final_cash_on_hand = ""

# Scenario 1: Cash-on-hand is always increasing
if  always_increasing:
    final_cash_on_hand += f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"
    final_cash_on_hand += f"[HIGHEST CASH SURPLUS] DAY: {highest_surplus_day}, AMOUNT: SGD{highest_surplus}\n"

# Scenario 2: Cash-on-hand is always decreasing
elif always_decreasing:
    final_cash_on_hand += f"[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY\n"
    final_cash_on_hand += f"[HIGHEST CASH DEFICIT] DAY: {highest_deficit_day}, AMOUNT: SGD{highest_deficit}\n"

# Scenario 3: Cash-on-hand fluctuates
else:
    for item in deficits:
        day, deficit = item
        final_cash_on_hand += f"[CASH DEFICIT] DAY: {item[0]}, AMOUNT: SGD{-item[1]}\n"
    
    top_3_deficits = find_top_3_deficits(deficits)
    final_cash_on_hand += f"[HIGHEST CASH DEFICIT] DAY: {top_3_deficits[0][0]}, AMOUNT: SGD{-top_3_deficits[0][1]}\n"
    final_cash_on_hand += f"[2ND HIGHEST CASH DEFICIT] DAY: {top_3_deficits[1][0]}, AMOUNT: SGD{-top_3_deficits[1][1]}\n"
    final_cash_on_hand += f"[3RD HIGHEST CASH DEFICIT] DAY: {top_3_deficits[2][0]}, AMOUNT: SGD{-top_3_deficits[2][1]}\n"

# Set up filepath for writing results to a text file named "summary_record.txt".
fp_write = Path.cwd() / "summary_report.txt"

# Write the results to the file
with fp_write.open(mode="w", encoding="UTF-8") as file:
    file.write(final_cash_on_hand)