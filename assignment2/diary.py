# Task 1: Diary Program
import traceback

try:
    # Open diary.txt in append mode using 'with' (auto handles closing)
    with open('diary.txt', 'a') as file:
        prompt = "What happened today? "
        
        while True:
            entry = input(prompt)
            file.write(entry + '\n')  # Write the input to the file
            
            if entry.lower() == "done for now":
                break  # Exit the loop when user is done

            prompt = "What else? "  # Update prompt for next input

except Exception as e:
    # Capture and format traceback
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
