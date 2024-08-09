# 자연수(1,2,3, .... ) 
# 홀수는 1,3 5 ...
# 짝수는 2,4,6 ...

# 2로 나누어서 나머지가 0이면 짝수
# 2로 나누어서 나머지가 0이 아니면 홀수

# num=int(input("자연수 입력>"))
# if num % 2 == 0:
#     print("짝")
# else:
#     print("홀")


# 홀수만 찍음
for i in range(1,10+1):
    if i % 2 ==0:
        continue   
    print(i)

print("========================")

# 짝수만 찍음
for i in range(1,10+1):
    if i % 2 !=0:
        continue   
    print(i)