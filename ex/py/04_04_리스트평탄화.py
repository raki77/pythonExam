# li=input("입력")
# for i in li:
#     if type(i) is list:
#         for i2 in i:
#             print(i2)
#     # print(i, end=' ')
# print(type(li))

# li=[1,2,[3,4],5,[6,7],[8,9]]
# new_li=[]
# for i in li:
#     if type(i) is list:
#         for j in i:
#             print(j, end=' ')
#             new_li.extend(list(j))
#     else:
#         new_li.append(i)
#     # print(i)
#     # new_li.append(i)
# print(new_li)

# li=[1,2,[3,4],5,[6,7],[8,9]]
# # print([i for i in li])

# print([i for i in li if type(i) is list ])


li=[1,2,[3,4],5,[6,7],[8,9]]

li_new=[]

for i in li:
    if type(i) is list:
        for j in i:
            li_new.append(j)
    else:
        li_new.append(i)

print(li_new)
