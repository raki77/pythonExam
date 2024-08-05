# print(list(range(5)))
# print(list(range(4,6)))
# print(list(range(7,0,-1)))
# print(list(range(3,8)))
# print(list(range(3,10,3)))

# key_list=["name","hp","mp","level"]
# value_list=["기사",200,30,5]
# character={}

# for i in range(len(key_list)):
#     character[key_list[i]]=value_list[i]
# print(character)


# tot=0
# for i in range(1,10000+1):
#     tot=tot+i
#     if tot > 10000:
#         print(i)
#         break

# print(tot)


# tot=0
# for i in range(1,141+1):
#     tot=tot+i

# print(tot)










# limit=10000
# i = 1
# sum_value=0

# for i in range(i, limit):
#     sum_value=sum_value + i
#     if sum_value > limit:  
#         print(i)      
#         break            

# print(f"{i+1}를 더할 때 {limit}을 넘으며 그 때의 값은 {sum_value}")




# 1*99, 2*98, 3*97, ..., 98*2, 99*1
# 최대값 구하기
# max=1
# for i in range(1, 99+1):
#     gop=i*(100-i)
#     if gop>max:
#         max=gop
#         print(f"최대가 되는 경우 : {i} * {100-i} = {max}")

# print(max)





max_value=0
a=0
b=0
for i in range(1, 100//2 + 1 ):
    j=100-i
    
    tmp=i*j
    if max_value < tmp:
        a=i
        b=j
        max_value=tmp
    
print(f"최대가 되는 경우 {a}*{b}={max_value}")








