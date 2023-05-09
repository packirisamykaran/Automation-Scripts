import csv

# Step 1: Open the CSV file
with open('webtwi.csv', 'r') as input_file:
    reader = csv.reader(input_file)
    rows = list(reader)

# Step 2: Remove spaces and join strings in each cell
for row in rows:
    for i, cell in enumerate(row):
        row[i] = ''.join(cell.split())

# Step 3: Save the modified CSV to a new file
with open('twitteroutput.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(rows)
