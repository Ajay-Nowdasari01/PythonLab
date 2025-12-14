print("Arithmetic Precedence ")
result = 10 + 5 * 2
print(f"10 + 5 * 2 = {result}") 

result = 20 - 10 / 2
print(f"20 - 10 / 2 = {result}") 

print("\nExponentiation Precedence ")
result = 2 * 3 ** 2
print(f"2 * 3 ** 2 = {result}")   

print("\nLogical Operator Precedence ")
# Precedence: not > and > or
result = 10 > 5 and 3 < 8 or False
print(f"10 > 5 and 3 < 8 or False = {result}") 

result = not True or False
print(f"not True or False = {result}") 

print("\n Bitwise Precedence ")
result = (5 | 3) & 6
print(f"(5 | 3) & 6 = {result}")

print("\n Mixed Operators ")
result = 2 + 3 * 4 - 5 / 2
print(f"2 + 3 * 4 - 5 / 2 = {result}")  


print("\n RIGHT-TO-LEFT Associativity ")
result = 2 ** 3 ** 2
print(f"2 ** 3 ** 2 = {result}") 

x = y = z = 5
print(f"x = y = z = 5; x={x}, y={y}, z={z}")  

print("\n Comparison Operators (CHAINED) ")    # observed change
result = 5 > 3 > 1
print(f"5 > 3 > 1 = {result}")  

result = 5 > 3 > 6
print(f"5 > 3 > 6 = {result}") 

result = 1 < 2 < 3 < 4
print(f"1 < 2 < 3 < 4 = {result}")  
