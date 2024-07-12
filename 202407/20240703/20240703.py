

######################################################################
age = 25; name="유재석"; is_student = True
is_employee = False

print("이름:" , name)
print("나이:" , age)
print("학생여부:" , is_student) 
 
print("이름:" , name , "\n나이:" , age)
print("학생여부:" , is_student)
print("직장인여부:" , is_employee)


is_employee = "직장인 아님"
# 콤마를 쓰면, 자동 한칸 뛰어쓰기가 적용된다. +합치기는 공백 없슴.
print("직장인여부2:" , is_employee)
print("result1:", 100 + 1000)
print("result2:" + " aaaaaaaaaa")
print("result3: " + str(2000))
print("1. It's a good day.!!")
print('2. It\'s a good day.!!')

# 튜플은 상수 개념, 선언 후 변경할 수 없다.
tuple1 = (1,2,3,4)

# dictionary
person = {"name": "한솔", "age" : 29, "city": "서울"}
print(type(person))
print(person['name'])
print(person['age'])
print(person['city'])

# 조건문
age = 6
if age < 7:
    # if age < 3:
    #   print("3세 미만은 무료입니다.")
    # else:
        print("어린이 가격이 적용됩니다.")
elif 7 <= age < 20:
    print("청소년 가격이 적용됩니다.")
else:
    print("성인 가격이 적용됩니다.")



# 반복문
i = 200
li = ["11","하마","33","44","55"]
result = 5

# i에 1이 대입되기 때문에, 위에 변수값을 설정하여도 의미가 없다.
for i in range(result):
  print(i)
  print(li[i])

print("True")
print(type(True))
print(1==1)
 

# 이터레이터 Iterator? 순서대로 다음 값을 리턴함. 
# 리스트를 이용한 반복문
fruits = ['사과', '바나나', '딸기']
for fruit in fruits:
  print(fruit)


# 반복문
count = 0
while count < 5:
    print(count)
    count = count + 1


# 반복문
for i in range(10):
    if i == 3:
        continue 
    if i == 7:
        break 
    print(i)

# 함수
def add(a, b):
    result = a + b
    return result

sum_result = add(10, 20)  # 함수 호출
print(sum_result) 


# 함수
def calculate(x, y):
    sum_val = x + y
    diff_val = x - y
    return sum_val, diff_val

result = calculate(10, 5)
print(result)

sum_val, diff_val = calculate(10, 5)
print(sum_val)  
print(diff_val) 


