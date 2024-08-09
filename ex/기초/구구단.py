# for i in range(2, 9+1):
#     for j in range(1, 9+1):
#         print("%d*%d=%2d " %(i,j, i*j), end=' ')
#     print()

# for i in range(2, 9+1):
#     for j in range(1, 9+1):
#         print(f"{i}*{j}={i*j:2}", end='  ')
#     print()

# for i in range(5):
#     print('*', end=' ')

# for i in range(1,5+1):
#     print('*'*i)

# for i in range(1,5+1):
#     for j in range(i):
#         print('*', end=' ')
#     print()




# 6 * 11
str1=''
for i in range(1,7):
    for j in range(6, i, -1):
        str1 +=' '
    for k in range(0, 2*i -1):
        str1 +='*'
    str1 +='\n'

for i in range(2):
    for j in range(4):
        str1 +=' '
    for k in range(3):
        str1 +='*'
    str1 +='\n'

print(str1)