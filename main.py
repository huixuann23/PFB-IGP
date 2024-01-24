import overheads, cash_on_hand, profit_and_loss
from pathlib import Path
import csv

# Creates a empty string for all the final results.
summary_report = ''
# Adds the final result for overheads.
summary_report += overheads.overhead() + "\n"

# Adds the final result for cash on hand.
summary_report += cash_on_hand.Cash_On_Hand() 

# Adds the final result for profit and loss.
summary_report += profit_and_loss.Profit_And_Loss()

# Setup the filepath for writing results to a text file named "summary_report.txt"
fp_write = Path.cwd() / "summary_report.txt"

# Write the data to the file.
with fp_write.open(mode="w", encoding="UTF-8") as file:
    file.write(summary_report)