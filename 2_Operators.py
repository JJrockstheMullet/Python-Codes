# 1. Arithmetic Operators: +, -, *, /, //, %, **
a = 10
b = 3

print("Arithmetic Operators:")
print(f"a + b = {a + b}")    # Addition
print(f"a - b = {a - b}")    # Subtraction
print(f"a * b = {a * b}")    # Multiplication
print(f"a / b = {a / b}")    # Division (float result)
print(f"a // b = {a // b}")  # Floor Division (integer result)
print(f"a % b = {a % b}")    # Modulus (remainder)
print(f"a ** b = {a ** b}")  # Exponentiation (power)

# 2. Relational Operators: <, >, <=, >=, ==, !=
print("\nRelational Operators:")
print(f"a > b: {a > b}")   # Greater than
print(f"a < b: {a < b}")   # Less than
print(f"a == b: {a == b}") # Equal to
print(f"a != b: {a != b}") # Not equal to
print(f"a >= b: {a >= b}") # Greater than or equal to
print(f"a <= b: {a <= b}") # Less than or equal to

# 3. Logical Operators: and, or, not
x = True
y = False

print("\nLogical Operators:")
print(f"x and y: {x and y}")  # Logical AND
print(f"x or y: {x or y}")    # Logical OR
print(f"not x: {not x}")      # Logical NOT

# 4. Assignment Operators: =, +=, -=, *=, /=, etc.
c = 5  # Assignment operator

print("\nAssignment Operators:")
c += 2  # Augmented assignment (c = c + 2)
print(f"c after c += 2: {c}")
c *= 3  # Augmented assignment (c = c * 3)
print(f"c after c *= 3: {c}")

# 5. Identity Operators: is, is not
p = 10
q = 10
r = [1, 2, 3]
s = [1, 2, 3]

print("\nIdentity Operators:")
print(f"p is q: {p is q}")       # p and q refer to the same integer object
print(f"r is s: {r is s}")       # r and s are different list objects, even with the same content
print(f"r is not s: {r is not s}")  # True, because r and s are distinct objects

# 6. Membership Operators: in, not in
my_list = [1, 2, 3, 4, 5]

print("\nMembership Operators:")
print(f"2 in my_list: {2 in my_list}")   # Check if 2 is in the list
print(f"6 not in my_list: {6 not in my_list}")  # Check if 6 is not in the list