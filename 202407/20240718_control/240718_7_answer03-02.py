# --------------------------------------------------
# 연습문제 03-02 [1번]
# --------------------------------------------------

x=2
y=10
if x>4:
    if y>2:
        print(x*y)
else:
    print(x+y)    
print("-"*60)



x=1
y=4
if x>4:
    if y>2:
        print(x*y)
else:
    print(x+y)
print("-"*60)





x=10
y=2
if x>4:
    if y>2:
        print(x*y)
else:
    print(x+y)
    
    
    
# --------------------------------------------------
# 연습문제 03-02 [2번]
# --------------------------------------------------
x=15
if x > 10 and x <20:
    print("조건에 맞습니다.")

# --------------------------------------------------
# 연습문제 03-02 [3번]
# --------------------------------------------------
import datetime


now = datetime.datetime.now()   
str1 = input("입력:")
str1 = str1.strip().replace(" ","")
'''
if "안녕" in str1 :
    print("안녕하세요")
elif "몇시" in str1 :
    print("지금 {} {}시입니다.".format("AM" if now.hour < 12 else "PM", now.hour))
''' 
#----------------------------------------------------
result2 = {
    "안녕": "안녕하세요.",    
    "몇시": "지금 {} {}시입니다.".format("AM" if now.hour < 12 else "PM", now.hour)    
}
for key, value in result2.items():    
    if str1 == key:
        print(value)
# --------------------------------------------------
# 연습문제 03-02 [4번]
# --------------------------------------------------
num1 = round(float(input("숫자 값을 입력하시오 (소수점 라운드처리):")))
if num1 < 1 :
    print("자연수를 입력하시오.")
else : 
    result = ""
    if num1%2 == 0:
        result += "2,"
    if num1%3 == 0:
        result += "3,"
    if num1%4 == 0:        
        result += "4,"
    if num1%5 == 0:        
        result += "5" 
            
    str2 = "나누어 떨어지는"               
    str3 = "숫자입니다."
    str4 = "숫자가 아닙니다."
    print(f"{num1}은 2로", str2, str3 if result.find("2") > -1 else str4)   
    print(f"{num1}은 3로", str2, str3 if result.find("3") > -1 else str4)   
    print(f"{num1}은 4로", str2, str3 if result.find("4") > -1 else str4)   
    print(f"{num1}은 5로", str2, str3 if result.find("5") > -1 else str4)       