
print("-"* 80)
numb = 5
numb += 2
print(numb)
numb = numb + 2
print(numb)



print("-"* 80) 
from math import * # math 모듈의 모든 기능을 가져다 쓰겠다는 의미 
result = floor(4.99)
print(result) # 4.99의 내림
result = ceil(3.14)
print(result) # 3.14의 올림
result = sqrt(16)
print(result) # 16의 제곱근



print("-"* 80) 
from random import * # random 모듈의 모든 기능을 가져다 쓰겠다는 의미 
print(random())
print(random())
print(random())
print(random() * 10)                     # 0.0 이상 10.0 미만에서 난수 생성
print(int(random() * 10))                 # 0이상 10 미만에서 난수 생성
print(int(random() * 10) + 1)           # 1이상 11미만에서 난수생성
print(int(random() * 45) + 1)           # 1이상 46미만에서 난수 생성



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





python = "Python is Amazing"

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
#index = python.index("Java") # Java가 없으면 오류가 발생하며 프로그램 종료
print(index)





python = "Python is Amazing"

print(python.count("n"))
print(python.count("v"))


python = "Python is Amazing"

print(len(python))



def open_account():
    print("새로운 계좌를 개설합니다.")

open_account() # 앞에 정의한 open_account() 함수 호출


def deposit(balance, money): # 입금 처리 함수                       매개변수 parameter
    print("{0}원을 입금했습니다. 잔액은 {1}원입니다.".format(money, balance + money))
    return balance + money # 입금 후 잔액 정보 반환

balance = 0 # 초기 잔액, balance 변수에 초깃값으로 0 저장
balance = deposit(balance, 1000) # 1,000원 입금, balance 변수에 deposit() 함수의 반환값을 다시 저장
#deposit(balance, 1000)




def withdraw(balance, money): # 출금 처리 함수
    if balance >= money: # 잔액이 출금액보다 많으면
        print("{0}원을 출금했습니다. 잔액은 {1}원입니다.".format(money, balance - money))
        return balance - money # 출금 후 잔액 반환
    else:
        print("잔액이 부족합니다. 잔액은 {0}원입니다.".format(balance))
        return balance # 기존 잔액 반환


balance = 0 # 초기 잔액
balance = deposit(balance, 1000) # 1,000원 입금

# 출금
balance = withdraw(balance, 2000) # 2,000원 출금 시도
balance = withdraw(balance, 500) # 500원 출금 시도





def withdraw_night(balance, money): # 업무 시간 외 출금
    commission = 100 # 출금 수수료 100원
    print("업무 시간 외에 {}원을 출금했습니다." .format(money))
    return commission, balance - money - commission

# 업무 시간 외 출금 시도
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))



# - 가변 인자 (variable argument) 
def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    print(language, type(language))
    for lang in language:
        print(lang, end=" ") # 언어를 모두 한 줄에 표시
    print() # 줄 바꿈 목적

profile("찰리", 20, "파이썬", "자바", "C", "C++", "C#", "자바스크립트")
profile("루시", 25, "코틀린", "스위프트")




