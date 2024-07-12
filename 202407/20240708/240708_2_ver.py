

# 연산과 연산자
print(1 + 1)
print(3 - 2)
print(5 * 2)
print(6 / 3)

# 제곱
print(2 ** 3)

# 나머지
print(10 % 3)

# 몫
print(10 // 3)


print(10 > 3)
print(4 >= 7)
print(10 < 3)
print(5 <= 5)

print(3 == 3)
print(4 == 2)
print(3 + 4 == 7)
print(1 != 3)


print((3 > 0) and (3 > 5))
print((3 > 0) or (3 > 5))
print(not(1 != 3))




# a > b > c  는   a > b and b > c  와 같다.
print(5 > 4 > 3)                          
print(4 > 5 > 3)
print(2 + 3 * 4)
print((2 + 3) * 4)



number = 2 + 3 * 4
print(number)
# number = number + 2
# print(number)


number = 2

number += 2 # number = number + 2와 동일
print(number)
number -= 2 # number = number - 2와 동일
print(number)
number *= 2 # number = number * 2와 동일
print(number)


# number = 4
# number /= 2 # number = number / 2와 동일
# print(number)
# number **= 2 # number = number ** 2와 동일
# print(number)

number = 9

# number = number // 2와 동일 (몫)
number //= 2 
print(number)

# number = number % 2와 동일 (나머지)
number %= 2 
print(number)

print(abs(-5)) # -5의 절대값
print(pow(4, 2)) # 4를 제곱한 값
print(max(5, 12)) # 5와 12 중 큰 값
print(min(5, 12)) # 5와 12 중 작은 값
print(round(3.14)) # 3.14를 소수점 이하 첫째 자리에서 반올림한 정수
print(round(4.678, 2)) # 4.678을 소수점 이하 셋째 자리에서 반올림한 값




 

#from math import * # math 모듈의 모든 기능을 가져다 쓰겠다는 의미
import math
result = math.floor(4.99)
print(result) # 4.99의 내림
result = math.ceil(3.14)
print(result) # 3.14의 올림
result = math.sqrt(16)
print(result) # 16의 제곱근

# import random

# # 1부터 10까지의 정수 난수 생성
# random_int = random.randint(1, 10000)
# print(f"1부터 10000까지의 정수 난수: {random_int}")

 
#from random import * # random 모듈의 모든 기능을 가져다 쓰겠다는 의미
import random
print(random.random())
print(random.random())
print(random.random())
print(random.random() * 10)                     # 0.0 이상 10.0 미만에서 난수 생성
print(int(random.random() * 10))                 # 0이상 10 미만에서 난수 생성
print(int(random.random() * 10) + 1)           # 1이상 11미만에서 난수생성
print(int(random.random() * 45) + 1)           # 1이상 46미만에서 난수 생성  

print(random.randrange(1, 46))           # 1 이상 46 미만에서 난수 생성
print("********** 로또 번호 **********")
print(random.randint(1, 45))             # 1 이상 45 이하에서 난수 생성
print(random.randint(1, 45))
print(random.randint(1, 45))
print(random.randint(1, 45))
print(random.randint(1, 45))
print(random.randint(1, 45))
print(random.randint(1, 45)) 

 

sentence1 = '나는 소년입니다.'
print(sentence1, type(sentence1))
sentence2 = "파이썬은 쉬워요."
print(sentence2, type(sentence2))

sentence3 = """
나는 소년이고,
    파이썬은 쉬워요.
"""
print(sentence3)



jumin = "990229-1234567"
print("성별 식별번호 : " + jumin[7])

jumin = "990229-1234567"
print("연 : " + jumin[0:2]) # 0부터 2 직전까지(0, 1)
print("월 : " + jumin[2:4]) # 2부터 4 직전까지(2, 3)
print("일 : " + jumin[4:6]) # 4부터 6 직전까지(4, 5)
print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지 -> jumin[0:6]과 같음
print("주민등록번호 뒷자리 : " + jumin[7:]) # 7부터 끝까지 -> jumin[7:14]와 같음
print("주민등록번호 뒷자리(뒤에서부터) : " + jumin[-7:]) # 뒤에서 7번째 위치부터 끝까지



python = "Python is Amazing"
print(python.lower()) # 전체 소문자로 변환
print(python.upper()) # 전체 대문자로 변환
print(python[0].isupper()) # 인덱스 0에 있는 값이 대문자인지 확인
print(python[1:3].islower()) # 인덱스 1부터 2에 있는 값이 소문자인지 확인
print(python.replace("Python", "Java")) # Python을 Java로 바꾸기



python = "Python is Amazing (Java)"
find = python.find("n") # 처음 발견한 n의 인덱스
print(find) # 'Python'에서 n(인덱스 5)
find = python.find("n", find + 1) # 인덱스 6 이후부터 찾아 처음 발견한 n의 인덱스
print(find) # ' is Amazing'에서 n(인덱스15)
find = python.find("Java") # Java가 없으면 -1을 반환(출력)한 후 프로그램 계속 수행
print(find)




index = python.index("n") # 처음 발견한 n의 인덱스
print(index) # 'Python'에서 n
index = python.index("n", index + 1) # 인덱스 6 이후부터 찾아 처음 발견한 n의 인덱스
print(index) # ' is Amazing'에서 n
index = python.index("n", 2, 6) # 인덱스 2부터 6 직전까지 찾아 처음 발견한 n의 인덱스
print(index) # 'thon'에서 n(인덱스 5)
# index = python.index("Java") # Java가 없으면 오류가 발생하며 프로그램 종료
print(index)


python = "Python is Amazing"
print(python.count("n"))
print(python.count("v"))


python = "Python is Amazing"
print("len:" , len(python))
print("ab" + "ab")
print("ab", "ab")


print("나는 %d살입니다." % 20)
print("나는 %s을 좋아합니다." % "파이썬")
print("Apple은 %c로 시작해요." % "A")
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 값이 여럿일 때



print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))
 
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")


print("********************************************************************")
print("백문이 불여일견 백견이 불여일타")
#print("백문이 불여일견 # SyntaxError 발생
#백견이 불여일타")
print("백문이 불여일견\n백견이 불여일타")
#print("저는 "나도코딩"입니다.")
print("저는 '나도코딩'입니다.")
# 또는
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")


#print("C:\Users\Nadocoding\Desktop\PythonWorkspace") # SyntaxError 발생
print("C:\\Users\\Nadocoding\\Desktop\\PythonWorkspace")
# r을 추가하면 문자열 어떤값이든 무시
print(r"C:\Users\Nadocoding\Desktop\PythonWorkspace")    


print("Red Apple\rPine")        # \r 은 커서를 맨 앞으로 이동시킵니다.
print("Redd\bApple")            # \b 는 앞글자 하나를 삭제합니다. Backspace
print("Red\tApple")              # \t 는 탭키와 같은 역할을 합니다.




aa = """
백문이 불여일견,
    백견이 불여일타.
"""

print(aa)
print("백문이 불여일견,\n    백견이 불여일타.") 
print("loc : " , aa.find('백견'))

idx = aa.find('불여')
print("idx : " , idx)
print("loc2 : " , aa.find("백견", idx + 1)) 
print("loc3 : " , aa.index("백견", 2, 30))







