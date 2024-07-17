
# ----------------------------
# 02-04 문제풀이
# ----------------------------
# 1. 
#   3번
# 2. 
#   split() : d번, 문자열 특정문자로 자릅니다.
#   upper() : b번, 문자열 대문자로 변환.
#   lower() : a번, 문자열 소문자로 변환
#   strip() : c번, 문자열 양옆 공백 제거.
# ----------------------------
#
#
import math 

print()
a = int(input("> 1번째 숫자:"))
b = int(input("> 2번째 숫자:"))
print("{0} + {1} = {2}".format(a, b, a+b))


print()
string = "hello"
string.upper()
print("A 지점:", string)
print("B 지점:", string.upper())
# 답변 : hello, HELLO
print(id(string))
string = string.upper()
print(id(string))


print()
r1 = int(input("구의 반지름을 입력해 주세요:"))
#result1 = (4/3) * math.pi* r1**3
result1 = (4/3) * (3.141592)* r1**3
print("구의 부피는" , result1 , "입니다.")
# result2 = 4* math.pi * r1**2
result2 = 4* (3.141592) * r1**2
print("구의 겉넓이는 %.4f입니다." %result2)



print()
num1 = float(input("밑 변의 길이를 입력해 주세요:")) #3.0
num2 = float(input("높이의 길이를 입력해 주세요:")) #4.0
result3 = (num1**2 + num2**2)**0.5
print("빗변의 길이는 %.1f 입니다." %result3) 
# math.sqrt (squaretimes : 사각형)
print("빗변의 길이는 {} 입니다.".format(  math.sqrt(num1**2 + num2**2))  )
print(f"빗변의 길이는 {math.sqrt(num1**2 + num2**2)} 입니다.")





