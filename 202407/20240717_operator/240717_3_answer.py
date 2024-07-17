a = input("<문자열입력>")
b = input("<문자열입력>")
print(a, b)
tmp = a  # assigned A address to tmp variable.
a = b
b = tmp
print(a, b)