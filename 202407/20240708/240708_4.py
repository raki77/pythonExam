

# weather = "비"
weather = "눈"
if weather == "비": # 대입 연산자(=)가 아닌 비교 연산자(==) 사용
    print("우산을 챙기세요.")




weather = "맑음"
if weather == "비":
    print("우산을 챙기세요.")
elif weather == "맑음":
    print("날씨가 맑으니, 썬크림을 바르세요.")
    print("하지만, 외출은 자제 하세요.")


weather = "미세먼지"
if weather == "비":
    print("우산을 챙기세요.") # 1번
elif weather == "미세먼지":
    print("마스크를 챙기세요.") # 2번
else:
    print("준비물이 필요 없어요.")    
    
    
    
    
weather = "맑음"
if weather == "비":
    print("우산을 챙기세요.")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요.")
else:
    print("준비물이 필요 없어요.")
    
 
 
 
for waiting_no in [1, 2, 3, 4, 5]:
    print("대기번호 : {0}".format(waiting_no)) # {0} 위치에 waiting_no의 값이 들어감


for waiting_no in range(5): # 0부터 5 직전까지(0~4)
    print("대기번호 : {0}".format(waiting_no))


for waiting_no in range(1, 6): # 1부터 6 직전까지(1~5)
    print("대기번호 : {0}".format(waiting_no))


for waiting_no in range(1, 6, 2): # 1부터 6미만 직전까지(1~5)에서 2씩 간격 주기
    print("대기번호 : {0}".format(waiting_no))






aaa = "-ON"
bbb = "-OFF"
orders = ["아이언맨", "토르", "스파이더맨"] # 손님 닉네임 리스트
for customer in orders:
    print("{0}{2}님, 커피가 준비됐습니다. 픽업대로 와 주세요.".format(customer,aaa,bbb))






def prType(va):
    print("문자열타입 {0} : {1}".format(va, type(va)))

cc = "a"
prType(cc)
prType(1)
prType(1==1)
prType(3.14)
 
 
 
 
 
 
 
customer = "토르" # 손님 닉네임
index = 5 # 초깃값, 부르는 횟수 최대 5번

while index >= 1: # 부르는 횟수가 1 이상일 때만 실행
    print("{} 님, 커피가 준비됐습니다.".format(customer))
    index -= 1 # 횟수 1회 차감
    print("{}번 남았어요.".format(index))
    if index == 0: # 5번 모두 불렀다면
        print("커피를 폐기 처분합니다.")
        
        

customer = "아이언맨"
index = 1

while True:
    print("{0} 님, 커피가 준비됐습니다. 호출 {1}회".format(customer, index))
    index += 1
    if index == 20:
        break


        
 
 

customer = "토르"
# 예약어 None
#person = None
person = "토르"

while person != customer:
    print("이름이 같지 않습니다.")
    if person != customer :        
        person = input("이름이 어떻게 되세요? ")       
    else:
        break
print("{0} 님, 커피가 준비되었습니다.".format(person))







absent = [2, 5] # 결석한 학생 출석번호
no_book = [7] # 책을 가져오지 않은 학생 출석번호

for student in range(1, 11): # 출석번호 1~10번
    if student in absent: # 결석한 학생이면
        continue # 다음 학생으로 넘어가기
    elif student in no_book: # 책을 가져오지 않으면 바로 수업 종료
        print("오늘 수업은 여기까지. {0}번 학생은 교무실로 따라와요.".format(student))            
        break # 반복문 탈출
    print("{0}번 학생, 책을 읽어 보세요.".format(student))





students = [1, 2, 3, 4, 5]
print(students)

# 한 줄 for 문으로 각 항목에 100 더하기
students = [i + 100 for i in students]
#students = [students[0] + 100, students[1] + 100, students[2] + 100, students[3] + 100, students[4] + 100]
#students = [1 + 100, 2 + 100, 3 + 100, 4 + 100, 5 + 100]
print(students)





students = ["Iron man", "Thor", "Spider Man"]
print(students)

# 한 줄 for 문으로 각 이름을 이름의 길이 정보로 변환
students = [len(i) for i in students]
#students = [len(students[0]), len(students[1]), len(students[2])]
#students = [len("Iron man"), len("Thor"), len("Spider Man")]
print(students)

students = ["Iron man", "Thor", "Spider Man"]
print(students)

# 한 줄 for 문으로 각 이름을 모두 대문자로 변경
students = [i.upper() for i in students]
print(students)








