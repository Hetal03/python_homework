import pandas as pd
import json
import os
from io import StringIO

# Task 1
task1_data_frame = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']  # Changed Department to City to match test
})

task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]  # Updated salaries to match test

task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1

# Write employees.csv for Task 1 test (must be in current dir)
task1_older.to_csv('employees.csv', index=False)

# Task 2
# Read employees.csv to create task2_employees (for the test)
task2_employees = pd.read_csv('employees.csv')

# Read additional_employees.json for test
# Ensure this file exists in the same directory as this script
if os.path.exists('additional_employees.json'):
    json_employees = pd.read_json('additional_employees.json')
else:
    # Fallback: create the JSON file (optional)
    json_data = [
        {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
        {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}
    ]
    with open('additional_employees.json', 'w') as f:
        json.dump(json_data, f, indent=4)
    json_employees = pd.read_json('additional_employees.json')

# Concatenate for more_employees
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)

# Task 3 variables
first_three = more_employees.head(3)
last_two = more_employees.tail(2)
employee_shape = more_employees.shape





# Task 4

dirty_data_str = """Name,Age,Salary,Hire Date,Department
Alice, 29,50000,2021/01/15, Sales 
Bob, 32, unknown,2020-03-18,MARKETING
 charlie, NaN, 70000,3/25/2019,marketinG
Dana, 41, n/a,2020/12/01, HR
Eve, 24,65000,2021/06/07,  hr
Frank, 32,75000, 2019-07-11,Sales
Bob, 32, unknown,2020-03-18,MARKETING
"""

dirty_data = pd.read_csv(StringIO(dirty_data_str))

clean_data = dirty_data.copy()
# Drop duplicates first
clean_data.drop_duplicates(inplace=True)

# Convert Age, fill missing Age with median
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].median())

# Convert Salary, replace unknown/n/a, convert to numeric, then fill missing with median
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())

# Clean and convert Hire Date, strip strings, convert, fill missing with earliest date
clean_data['Hire Date'] = clean_data['Hire Date'].astype(str).str.strip()
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')
clean_data['Hire Date'] = clean_data['Hire Date'].fillna(clean_data['Hire Date'].min())

# Strip strings in Name and Department, uppercase Department
clean_data['Name'] = clean_data['Name'].str.strip()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()



