str1=''
for i in range(1,7):
    for j in range(6, i, -1):
        str1 +=' '
    for k in range(0, 2*i-1):
        str1 +='*'
    str1 +='\n'

print(str1)