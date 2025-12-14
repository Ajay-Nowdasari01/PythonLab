a = 25
print(f"Int: {a}, type: {type(a)}\n")

b = -5.5
print(f"Float: {b}, type: {type(b)}\n")

sentence = "Hello, World!"
empty_str = ""
print(f"sentence: {sentence}, type: {type(sentence)}")
print(f"empty_str: {empty_str}, type: {type(empty_str)}\n")

boo = False
result = (10 > 5)
print(f"boo: {boo}, type: {type(boo)}")
print(f"result (10 > 5): {result}, type: {type(result)}\n")

mixed = [1, "hello", 3.14, True]
print(f"Mixed list: {mixed}, type: {type(mixed)}\n")
  #we used same result variable for 2 different 
tpl = ("Bob", 30, "Engineer")
print(f"Tuple: {tpl}, type: {type(tpl)}\n")

student = {"name": "ajay", "age": 22, "grade": "A"}
print(f"student Dictionary: {student}, type: {type(student)}\n")

colors = {"red", "green", "blue"}
print(f"colors set: {colors}, type: {type(colors)}\n")

nothing = None
print(f"None Data type: {nothing}, type: {type(nothing)}\n")

complex_num = 3 + 4j
print(f"complex_num: {complex_num}, type: {type(complex_num)}\n")