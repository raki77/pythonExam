
# 파이썬으로 LOTTO 추천번호 자동생성 프로그램을 만들어 봅시다.
# 1. random 함수 사용
# 2. 6개 번호 생성 + 1개 번호를 추천. (보너스)
# 3. 번호는 중복되면 안됩니다.
# 4. 1 부터 45 사이의 번호로 추천 되어야 합니다.
# 5. 한번에 5줄 추천 합니다.
# Automatic Create LOTTO Program

import random

def has_duplicates(lst):
    return len(lst) != len(set(lst))

def createNum(cnt):
    idx = 1
    while cnt >= idx:      
        result = [random.randint(1, 46), random.randint(1, 46),random.randint(1, 46),random.randint(1, 46),random.randint(1, 46),random.randint(1, 46), random.randint(1, 46)]        
        while has_duplicates(result) != True:            
            #print(sorted(result))
            print(result)
            idx += 1
            break                
createNum(5) 




# sample test
print("-" * 80)
 
#for i in range(7):
def oneLine():
    lnum = set([]) #set
    while True:
        lnum.add(int(random.random()*45) +1)  # for creating 1 ~ 46 random number.
        if len(lnum) == 6:
            break
    print(sorted(lnum)) 


lottoCnt = int(input("How many lucky lotto cnt you want? "))
for i in range(lottoCnt):
    oneLine()
    
  


# 기초문제 1
print("Mary's cosmetics")


# 기초문제 2
print('신씨가 소리 질렀다. "도둑이야."')


# 기초문제 3
# naver;kakao;sk;samsung  프린터 문에서(sep=";") 사용
print("naver", "kakao", "sk", "samsung", sep=";")
print("naver", "kakao", "sk", "samsung", sep=".")



import operator
# 기초문제 4
s = "hello"
t = " python"
# 두 개의 변수가 있다. 변수를 이용해서 
# hello! python 를 출력 하세요.
print(s, t, sep="!")
print(s + "!" + t)
print(operator.concat((s + "!"), t))

 

# 기초문제 5
letters = 'python'
#위에서 p t 를 출력 하세요.
print(letters[0], letters[2])
print(letters.replace("hon","").replace("y"," "))
print(letters[0:3].replace("y", " "))
print(letters[:2])
print(letters[2:])
print(letters[::2])
idx = letters.find('t')
print(letters[0:idx+1].replace("y", " "))



# 기초문제 6
# license_plate = "24가 2210"
# 2210 만 출력 하세요.
license_plate = "24가 2210"

print(license_plate[-4:])
print(license_plate[4:])
cnum = license_plate[license_plate.find("2210"):]
print(cnum)
cnum = license_plate[license_plate.index(' ')+1:4] 
print(cnum)



# 기초문제 7
phone_number = "010-1111-2222"
# 전화번호의 -를 제거하시오.
print( phone_number.replace("-"," "))
aaa = '01-sample.png'
print(aaa.replace('.png','.jpg'))



# 기초문제 8
url = "http://sharebook.kr"
# 위에서 kr을 출력하세요. (split() 사용가능)
print(url.split(".")[1])
print(url[-2:])

import re
x = re.split("\.",url)
print(x[1])



# 기초문제 9 (strip)
data = "    삼성전자    "
print(data)
print(data.strip())



# 기본 사용 예제
x = 10
print(isinstance(x, int))  # True
y = "hello"
print(isinstance(y, str))  # True


# 기초문제 10
tkn =  "btc_krw"
# (upper 함수를 사용하여, 대문자로 바꾸어 출력 하세요.)
print(tkn.upper())
tkn2 =  "BTC_KRW"
print(tkn2.lower())



# 리스트 컴프리헨션의 문법은 다음과 같다. ‘if 조건문’ 부분은 앞의 예제에서 볼 수 있듯이 생략할 수 있다.
# [표현식 for 항목 in 반복_가능_객체 if 조건문]

a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0] # 3,6,9,12 에서 나눠서 나머지가 2인 값들
print(result)
#[6, 12]

# mod1.py 모듈로 생성함.
import mod1
print(mod1.add(3, 4))
print(mod1.add(4, 2))



