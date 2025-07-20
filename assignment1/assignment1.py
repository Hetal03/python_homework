# Write your code here.

# Task 1
def hello():
    return "Hello!"


print(hello())



# Task 2
def greet(name):
    return f"Hello, {name}!"

print(greet("Hetal"))




# Task 3
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
            case _:
                return "Invalid operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

# Try these examples manually
print(calc(10, 5, "add"))
print(calc(10, 0, "divide"))
print(calc("a", "b", "multiply"))



def data_type_conversion(value, type_name):
    try:
        match type_name:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
            case _:
                return f"{type_name} is not a valid type."
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {type_name}."
    
print(data_type_conversion("123.45", "float"))   # Should return 123.45
print(data_type_conversion("nonsense", "int"))   # Should return error message

def grade(*args):
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided."
    

print(grade(85, 90, 95))     # Should return "A"
print(grade("a", "b")) 

def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result


print(repeat("ha", 3)) 


def student_scores(method, **kwargs):
    try:
        if method == "best":
            return max(kwargs, key=kwargs.get)
        elif method == "mean":
            return sum(kwargs.values()) / len(kwargs)
        else:
            return "Invalid method"
    except (ValueError, ZeroDivisionError, AttributeError):
        return "Invalid input"
    

print(student_scores("best", Alice=90, Bob=85, Charlie=92))  # Should return "Charlie"
print(student_scores("mean", Alice=90, Bob=85, Charlie=92))  # Should return average



def titleize(text):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = text.split()
    result = []

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word not in little_words:
            result.append(word.capitalize())
        else:
            result.append(word.lower())
    return " ".join(result)


print(titleize("the lord of the rings"))   # The Lord of the Rings
print(titleize("a tale of two cities"))    # A Tale of Two Cities


def hangman(secret, guess):
    result = ""
    for char in secret:
        if char in guess:
            result += char
        else:
            result += "_"
    return result

def pig_latin(text):
    vowels = "aeiou"
    words = text.split()
    result = []

    for word in words:
     
        if word.startswith("qu"):
            result.append(word[2:] + "quay")
        else:
            for i in range(len(word)):
     
                if word[i] in vowels:
                    if i > 0 and word[i-1] == 'q' and word[i] == 'u':
                        result.append(word[i+1:] + word[:i+1] + "ay")  
                    else:
                        result.append(word[i:] + word[:i] + "ay")
                    break
    return " ".join(result)


print(pig_latin("square"))  # aresquay
print(pig_latin("quiet"))   # ietquay
