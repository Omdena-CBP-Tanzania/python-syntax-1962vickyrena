def format_string(name, age):
    return f"My name is {name} and I am {age} years old"

intro = format_string("Alice", 38)
print(intro)


def conditional_check(number):
    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    else:
        return "Equal"
result = conditional_check(40)
print(result)  


def loop_sum(n):
    total = 0 
    for i in range (1, n + 1 ):
        total +=i
    return total
print(loop_sum(5))


def list_operations(numbers):
    
    total_sum=sum(numbers)
    maximum=max(numbers)
    minimum=min(numbers)
    return total_sum,maximum,minimum

numbers=[20,60,40]
result=list_operations(numbers)
print(result)


def dict_operations(students_dict):
    student_library = [name for name, score in students_dict.items() if score > 80]
    return student_library
students = {
    "hamida": 400,
    "Baraka": 65,
    "Charlie": 85,
    "David": 70
}
result = dict_operations(students)
print(result)


def set_operations(list1, list2):
   
    def set_operations(list1, list2):
    # Base case: Stop if either list is empty
     if len(list1) == 0 or len(list2) == 0:
        return {}  # Return an empty dictionary to prevent NoneType error

    # Set operations (for example, intersection)
    set1 = set(list1)
    set2 = set(list2)
    result = set1 & set2  # Intersection of both sets

    print(result)  # Print the result of the operation

    # Recursively call with smaller portions of the lists
    return {"intersection": result}  # Return a dictionary containing the result

# Example usage
list1 = [1, 2, 3]
list2 = [2, 3, 4]
result = set_operations(list1, list2)

# Handling result
if result:  # Check if result is not None or empty
    if isinstance(result, dict):
        # If result is a dictionary, iterate with .items()
        for operation, value in result.items():
            print(f"Operation: {operation}, Value: {value}")
    else:
        # If result is not a dictionary, handle accordingly (e.g., print the result)
        print(result)
else:
    print("The result is None or empty.")





def arithmetic_ops(a, b):

    operations = {
        'sum': a + b,            
        'difference': a - b,                   
        'product': a * b,                  
        'quotient': a / b if b != 0 else None,     
        
    }
    return operations
    
    result = arithmetic_ops(a, b)
for operation, value in result.items():
    print(f"{operation}: {value}")
a = 10
b = 2
result = arithmetic_ops(a, b)
print("\nEdge case (b = 2):")
for operation, value in result.items():
    print(f"{operation}: {value}")


def logical_ops(x, y):
    
    operations = {
        'AND': x and y,       
        'OR': x or y,         
        'NOT_x': not x,       
    }
    return operations
x = True
y = False
result = logical_ops(x, y)
for op, value in result.items():
    print(f"{op}: {value}")


def bitwise_ops(a, b):
 
    operations = {
        'and': a & b,       
        'or': a | b,           
        'xor': a ^ b,          
    }
    return operations
    a = 5
b = 3
result = bitwise_ops(a, b)
for operation, value in result.items():
    print(f"{operation}: {value}")