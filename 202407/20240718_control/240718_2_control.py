# 제어문 연습
num = int(input("정수입력"))
print("입력값:", num)

if num > 0:
    print("양수 입니다.")
    
if num == 0:
    print("0입니다.")
    # 들여쓰기로 조건문 영역을 구분한다.
    # print("끝")  

if num < 0:
    print("음수입니다")


print("END") 


if True:
    print("짜장")
elif True:
    print("짬뽕")
else :
    print("볶음밥")  
    
if False :
    print("짜")
elif True:
    print("짬")
else :
    print("밥")
    
if False:
    print("짜")
elif False:
    print("짬")
else :
    print("밥")