import csv
import os

csv_path = os.path.join(os.path.dirname(__file__), '..', 'csv', 'employees.csv')

with open(csv_path, newline='') as file:
    reader = csv.reader(file)
    rows = list(reader)

# Skip header row
data = rows[1:]

# List of full names
names = [f"{row[0]} {row[1]}" for row in data]
print("All names:", names)

# Names containing the letter 'e'
names_with_e = [name for name in names if 'e' in name.lower()]
print("Names with 'e':", names_with_e)