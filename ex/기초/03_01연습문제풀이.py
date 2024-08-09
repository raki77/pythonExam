# print(10 == 100) # False
# print(10 != 100) # True
# print(10 > 100) # False
# print(10 < 100) # True
# print(10 <= 100) # True
# print(10 >= 100) # False

# x=2
# if x > 4:
#     print("참")

# x=1
# if x > 4:
#     print("참")

# x=10
# if x > 4:
#     print("참")

# score=int(input("점수 입력하세요."))

# if score >=90 and score <=100:
#     print("A")
# elif score >=80 and score <90:
#     print("B")
# elif score >=70 and score <80:
#     print("C")
# elif score >=0 and score <70:
#     print("F")
# else:
#     print("0점에서 100점 사이 점수로만 넣으세요")

x=10
y=2

# if x >4:
#     if y > 2:
#         print(x*y)
# else:
#     print(x+y)

# if x > 4 and y > 2:
#     print(x*y)
# else:
#     print(x+y)   

# x=15

# if x>10:
#     if x <20:
#         print("O")

# if x>10 and x <20:
#     print("O")


import datetime


msg=input("입력:")
msg=msg.strip()

now=datetime.datetime.now()
# print(now.hour)

if '안녕' in msg:
    print(">안녕하세요")
elif '몇 시' in msg:
    print("지금은 {}시입니다.".format(now.hour))


