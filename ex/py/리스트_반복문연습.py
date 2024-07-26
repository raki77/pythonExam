# help([].append)
# help([].extend)
# list_of_list=[
#     [1,2,3],
#     [4,5,6,7],
#     [8,9]
# ]
# for i in list_of_list:
#     print(i)



# numbers=[273,103,5,32,65,9,72,800,99]

# for i in numbers:
#     if i % 2 == 0 :
#         print(f'{i}는 짝수')
#     else:
#         print(f'{i}는 홀수')

# for i in numbers:
#     if i % 2 == 0 :
#         print(f'{i}는 짝수')
#     else:
#         print(f'{i}는 홀수')


# 1부터 10까지 중 홀수
# for i in range(1,10+1):
#     if i % 2 !=0:
#         print(i)

# numbers=[273, 103, 5,32,65,9,72,800,99]
# for i in numbers:
#     if i % 2 !=0:
#         print("{}는 홀".format(i))
#     else:
#         print("{}는 짝".format(i))

numbers=[273, 103, 5,32,65,9,72,800,99]
for i in numbers:
    # print("{}는 {} 자리수".format(i, len(str(i))) )
    print(f"--{i}는 {len(str(i))} 자리수--")



# 1부터 10까지 중 3의 배수
# for i in range(1,10+1):
#     if i % 3 == 0:
#         print(i)
# 1부터 10까지 중 3의 배수의 누적합
# tot=0
# for i in range(1,10+1):
#     if i % 3 == 0:
#         tot =tot + i

# print(tot)

# numbers=[273, 103, 5,32,65,9,72,800,99]
# for i in numbers:
#     if i >= 100:
#         print(i)
