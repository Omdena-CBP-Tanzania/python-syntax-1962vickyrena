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
    return (total_sum,maximum,minimum)

numbers=[20,60,40]
result=list_operations(numbers)
print(result)


def dict_operations(students_dict):
    student_library = [name for name, score in students_dict.items() if score > 80]
    return student_library
students = {
    "Hamida": 90,
    "Baraka": 65,
    "Charlie": 85,
    "David": 70
}
result = dict_operations(students)
print(result)


def set_operations(list1, list2):
    # Check for empty lists
    if not list1 or not list2:
        return set()  # Return an empty set if either list is empty

    # Perform set intersection
    set1 = set(list1)
    set2 = set(list2)
    result = set1 & set2  # Intersection of both sets

    return result  # Return the intersection set
# Example usage
list1 = [1, 2, 3]
list2 = [2, 3, 4]
result = set_operations(list1, list2)
# Handling result
if result:  # Check if the result is not empty
    print(f"Intersection: {result}")
else:
    print("The result is empty.")


def arithmetic_ops(a, b):
    # Perform arithmetic operations
    operations = {
        'sum': a + b,
        'difference': a - b,
        'product': a * b,
        'quotient': a / b if b != 0 else None,  # Handle division by zero
    }
    return operations
# Call the function and store the result
result = arithmetic_ops(10, 5)
print(result)


def logical_ops(x, y):
    operations = {
        'and': x and y,       
        'or': x or y,         
        'not_x': not x,       
    }
    return operations
result = logical_ops(True, False)
print(result)


def bitwise_ops(a, b):
    operations = {
        'and': a & b,       
        'or': a | b,           
        'xor': a ^ b,          
    }
    return operations
result = bitwise_ops(12, 10)
print(result)