a=10
b=1.2
c='A'
d="shyam"
boo=a==b
print("Int",a)
print("Float",b)
print("Char",c)
print("String",d)
print("Boolean",boo)

print("Type conversion \v")

print("int into int:",int(a))
print("float into int:",int(b))
print("char into int",ord(c))
# print("string into int",int(d))  TypeError:  The int() function cannot convert non-numeric characters into an integer, raising a ValueError
print("Boolean into int:",int(boo))
print("\v")
print("int into float:",float(a))
print("float into float:",float(b))
print("char into float:",ord(c))
# print("string into float:",float(d))
print("Boolean into float:",float(boo))
print("\v")
print("int into char",chr(97))
print("float into char",chr(int(98)))
# print("char into char",chr(c))  TypeError
# print("string into char",chr(d))  TypeError
print("Boolean into char",chr(boo))
print("\v")
print("int into String",str(a))
print("float into String",str(b))
print("char into String",str(c))
print("string into String",str(d))
print("Boolean into String",str(boo))
print("\v")
print("int into Boolean",bool(a))
print("float into Boolean",bool(b))
print("char into Boolean",bool(c))
print("string into Boolean",bool(d))
print("Boolean into Boolean",bool(boo))

# s_bad = "12a"
# print("3) str -> int (invalid):", s_bad, "->", int(s_bad)) we cant convert string having alphabets to int

lst = [1, 2, 3]
print("\n list -> tuple:", lst, "->", tuple(lst))

txt = "hi"
b = txt.encode('utf-8')
print("\nstr -> bytes:", txt, "->", b)
print("   bytes -> str:", b, "->", b.decode('utf-8'))