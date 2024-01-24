from pathlib import Path
import csv

def overhead():
    # Creates a file path to csv file.
    fp = Path.cwd()/"csv_reports"/"Overheads.csv"

    # Check if the file exists at the specified path.
    # print(fp.exists()) 

    # Read the csv file.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        # Create an empty list for overheads
        overheads_record=[] 

        # Append overheads into the overheadsRecord list
        for row in reader:
            # Get the overhead and append to the overheads_record list
            overheads_record.append([row[0],row[1]])   

    # print(overheads_record)

    # Initializing variables to keep track of the highest overhead.
    highest_overhead = 0
    highest_category = ""

    # Iterate through each overhead in the list.
    for category, overheads in overheads_record:
        # Coverting the overhead to float for comparison.
        overheads = float(overheads)
        # Convert category to uppercase.
        category = category.upper()

        # Check if the overhead is greater than the current highest.
        if overheads > highest_overhead:
            highest_overhead = overheads # Replacing the current oveerhead with the new highest overhead if is higher.
            highest_category = category # Replacing the current category with the new highest category if is higher.

    # Prepare the final highest overhead string
    final_highest_overhead = f"[HIGHEST OVERHEAD] {highest_category}: {highest_overhead}%"

    # Set up filepath for writing results to a text file named "summary_report.txt".
    # fp_write = Path.cwd() / "summary_report.txt"

    # # Write the data to the file.
    # with fp_write.open(mode="a", encoding="UTF-8") as file:
    #     file.write(final_highest_overhead)
    return final_highest_overhead