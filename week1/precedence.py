print(" 1. Arithmetic Precedence ")
result = 10 + 5 * 2
print(f"10 + 5 * 2 = {result}")  # 20 (multiplication first)

result = (10 + 5) * 2
print(f"(10 + 5) * 2 = {result}")  # 30 (parentheses first)

result = 20 - 10 / 2
print(f"20 - 10 / 2 = {result}")  # 15.0 (division first) observed change

print("\n2. Exponentiation Precedence ")
result = 2 * 3 ** 2
print(f"2 * 3 ** 2 = {result}")  # 18 (3**2 = 9 first, then 2*9 = 18))

result = (2 * 3) ** 2
print(f"(2 * 3) ** 2 = {result}")  # 36 (2*3 = 6 first, then 6**2 = 36)

result = 2 ** 3 ** 2
print(f"2 ** 3 ** 2 = {result}")  # 512 (right to left: 2**(3**2) = 2**9 = 512)

result = (2 ** 3) ** 2
print(f"(2 ** 3) ** 2 = {result}")  # 64 (left to right: (2**3)**2 = 8**2 = 64)

print("\n 3. Comparison Precedence ")
result = 5 > 3 and 2 < 4
print(f"5 > 3 and 2 < 4 = {result}")  # True

result = 10 == 10 or 5 > 10
print(f"10 == 10 or 5 > 10 = {result}")  # True

print("\n 4. Logical Operator Precedence ")
# Precedence: not > and > or
result = True or False and False
print(f"True or False and False = {result}")  # True (and evaluated first)

result = not True or False
print(f"not True or False = {result}")  # False (not evaluated first)

result = True or not False and False
print(f"True or not False and False = {result}")  # True (not -> and -> or)

print("\n 5. Bitwise Precedence ")
result = 5 | 3 & 6
print(f"5 | 3 & 6 = {result}")  # 7 (& has higher precedence than |)

result = (5 | 3) & 6
print(f"(5 | 3) & 6 = {result}")  # 7

print("\n Mixed Operators ")
result = 2 + 3 * 4 - 5 / 2
print(f"2 + 3 * 4 - 5 / 2 = {result}")  # 11.5

result = 10 > 5 and 3 < 8 or False
print(f"10 > 5 and 3 < 8 or False = {result}")  # True



print("\n 2. RIGHT-TO-LEFT Associativity ")
result = 2 ** 3 ** 2
print(f"2 ** 3 ** 2 = {result}")  # 512 (2**(3**2) = 2**9 = 512)

x = y = z = 5
print(f"x = y = z = 5; x={x}, y={y}, z={z}")  # All are 5 (right to left assignment)

print("\n 3. Comparison Operators (CHAINED) ")    # observed change
result = 5 > 3 > 1
print(f"5 > 3 > 1 = {result}")  # True (True and True = True)

result = 5 > 3 > 6
print(f"5 > 3 > 6 = {result}")  # False (True and False = False)

result = 1 < 2 < 3 < 4
print(f"1 < 2 < 3 < 4 = {result}")  # True (all comparisons are true)
