# 경우의 수 1,2,3, ~, 10
# num=10

# if num>=1 and num < 4:
#     print("A")
# elif num>=4 and num <7:
#     print("B")
# else:
#     print("C")


# # 경우의 수 1,2,3, ~, 10
# num=7

# if 1<= num < 4:
#     print("A")
# elif 4 <= num < 7:
#     print("B")
# else:
#     print("C")


# 봄 3,4,5
# 여름 6,7,8
# 가을 9,10,11
# 겨울 12, 1,2 


mon=int(input("현재 몇 월:"))

if mon >=3 and mon <6:
    print("봄")
elif mon >=6 and mon <9:
    print("여름")
elif mon >=9 and mon <12:
    print("가을")
else:
    print("겨울")
