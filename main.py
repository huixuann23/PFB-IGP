import overheads, cash_on_hand
from pathlib import Path
import csv

summary_report = ''
summary_report += overheads.overhead() + "\n"
summary_report += cash_on_hand.CashOnHand()
# summary_report += profit_and_loss.ProfitAndLoss()


fp_write = Path.cwd() / "summary_report.txt"

# Write the data to the file.
with fp_write.open(mode="w", encoding="UTF-8") as file:
    file.write(summary_report)