import pandas as pd

# Task 1 — Create the initial DataFrame
task1_data_frame = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})

# Add a Salary column
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]

# Increment the Age column
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1

# Save to CSV
task1_older.to_csv('employees.csv', index=False)


task1_older.to_csv('employees.csv', index=False)


task2_employees = pd.read_csv('employees.csv')


# Task 2: Read from CSV
# --------------------------
task2_employees = pd.read_csv('employees.csv')
print("\nTask 2 - CSV Loaded:")
print(task2_employees)

# Task 2: Read from JSON
# --------------------------
# Save JSON file (only run once, or check if it exists before overwriting)
additional_employees = [
    {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
    {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}
]


import json
with open('additional_employees.json', 'w') as f:
    json.dump(additional_employees, f)

# Load JSON
json_employees = pd.read_json('additional_employees.json')
print("\nTask 2 - JSON Loaded:")
print(json_employees)

# --------------------------
# Task 2: Combine both DataFrames
# --------------------------
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("\nTask 2 - Combined DataFrame:")
print(more_employees)



# Task 3
first_three = more_employees.head(3)
print(first_three)

last_two = more_employees.tail(2)
print(last_two)

employee_shape = more_employees.shape
print(employee_shape)

more_employees.info()


# Task 4

dirty_data = pd.read_csv('dirty_data.csv')
print("\nDirty Data:")
print(dirty_data)

clean_data = dirty_data.copy()


clean_data.drop_duplicates(inplace=True)
print("\nAfter Dropping Duplicates:")
print(clean_data)


clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print("\nAfter Converting Age to Numeric:")
print(clean_data)


clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
print("\nAfter Cleaning Salary:")
print(clean_data)


clean_data['Age'].fillna(clean_data['Age'].mean(), inplace=True)
clean_data['Salary'].fillna(clean_data['Salary'].median(), inplace=True)
print("\nAfter Filling Missing Numeric Values:")
print(clean_data)

clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')
print("\nAfter Converting Hire Date:")
print(clean_data)


clean_data['Hire Date'] = clean_data['Hire Date'].fillna(pd.Timestamp('2000-01-01'))

clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print("\nAfter Cleaning Name and Department:")
print(clean_data)
