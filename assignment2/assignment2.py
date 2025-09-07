#Task 2

import csv
import sys
import traceback
import os
import custom_module
from datetime import datetime

def read_employees():
    employees_dict = {}  # Dictionary to hold fields and rows
    rows = []            # List to hold employee rows
    
    try:
        # Open the CSV file for reading
        with open('../csv/employees.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    employees_dict["fields"] = row  # First row: headers
                else:
                    rows.append(row)               # Other rows: data
            
            employees_dict["rows"] = rows        # Add rows list to dictionary
            
    except Exception as e:
        # Catch and print detailed traceback info, then exit
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit(1)
    
    return employees_dict


# Global variable, set on module import
employees = read_employees()
print(employees)  # For verification, can be removed later


#Task 3

def column_index(column_name):
    return employees["fields"].index(column_name)

# Global variable used in later steps
employee_id_column = column_index("employee_id")


#Task 4

def first_name(row_number):
    col_index = column_index("first_name")
    return employees["rows"][row_number][col_index]


#Task 5

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches


#Task 6

def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches


#Task 7

def sort_by_last_name():
    last_name_index = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_index])
    return employees["rows"]


#Task 8
def employee_dict(row):
    fields = employees["fields"]
    values = row
    emp_dict = {field: value for field, value in zip(fields, values) if field != "employee_id"}
    return emp_dict


#Task 9

def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        emp_id = row[employee_id_column]
        emp_data = employee_dict(row)
        result[emp_id] = emp_data
    return result


#Task 10

def get_this_value():
    return os.getenv("THISVALUE")


#Task 11

import custom_module  # Step: import your custom module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

# Call the function with any string
set_that_secret("open_sesame")

# Print the new secret to verify
print("Updated secret:", custom_module.secret)


#Task 12


def read_csv_as_dict_of_tuples(filepath):
    result = {"fields": [], "rows": []}
    with open(filepath, newline="") as f:
        reader = csv.reader(f)
        result["fields"] = next(reader)  # Get header
        for row in reader:
            result["rows"].append(tuple(row))  # Convert row to tuple
    return result


def read_minutes():
    def read_csv_to_dict(path):
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            fields = reader.fieldnames
            rows = [tuple(row[field] for field in fields) for row in reader]  # convert each row to tuple
        return {"fields": fields, "rows": rows}

    minutes1 = read_csv_to_dict("../csv/minutes1.csv")
    minutes2 = read_csv_to_dict("../csv/minutes2.csv")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print("Minutes 1:", minutes1)
print("Minutes 2:", minutes2)



#task 13

def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1.union(set2)


minutes_set = create_minutes_set()
print("\nMinutes Set:")
print(minutes_set)

#Task 14
def create_minutes_list():
    minutes_list = list(minutes_set)  # set to list
    result = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    return result

minutes_list = create_minutes_list()
print("\nMinutes List (with datetime):")
print(minutes_list)


#Task 15
def write_sorted_list():
    # Use the global minutes_list which contains datetime objects
    sorted_minutes = sorted(minutes_list, key=lambda x: x[1])
    
    converted = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_minutes))
    
    with open("./minutes.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])  # Header: ['Name', 'Date']
        writer.writerows(converted)
    
    return converted

converted_list = write_sorted_list()
print("\nWritten and Sorted Minutes List:")
print(converted_list)