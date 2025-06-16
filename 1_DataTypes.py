# 1. Numbers: Integer, Float, and Complex
integer_num = 42       # Integer data type
float_num = 3.14159    # Floating-point data type
complex_num = 1 + 2j   # Complex number (real + imaginary part)

print("Integer:", integer_num)
print(type(integer_num))    
print("Float:", float_num)
print(type(float_num))
print("Complex:", complex_num)
print(type(complex_num))

# 2. Boolean Type
is_true = True    # Boolean data type
is_false = False

print(x)
print(y)

print("Boolean True:", is_true)
print("Boolean False:", is_false)

# 3. Sequence Types: String, List, Tuple
# String (Immutable)
string_example = "Hello, Python!"

# List (Mutable)
list_example = [1, 2, 3, 4, 5]
print(list_example)
list_example[2]=30 
print(list_example)

# Tuple (Immutable)
tuple_example = (10, 20, 30, 40)


# The values in a list can be changed unlike the tupple 

print("String:", string_example)
print("List:", list_example)
print("Tuple:", tuple_example)

# 4. Mapping Type: Dictionary (Mutable)
dictionary_example = {
    "name": "Alice",
    "age": 30,
    "location": "New York"
}

print("Dictionary:", dictionary_example)

# 5. None Type: Used to represent the absence of a value
none_value = None
print("None value:", none_value)

# 6. Mutable vs Immutable Data Types
# Mutable: List, Dictionary
list_example[0] = 99   # You can modify lists
dictionary_example["age"] = 31  # You can modify dictionary entries

print("Modified List:", list_example)
print("Modified Dictionary:", dictionary_example)

# Immutable: Integer, String, Tuple
# Uncommenting the following lines will raise an error
# string_example[0] = "h"  # Strings are immutable
# tuple_example[0] = 100   # Tuples are immutable

# 7. Complex Number Arithmetic
complex_result = complex_num + (2 - 3j)
print("Complex Arithmetic Result:", complex_result)