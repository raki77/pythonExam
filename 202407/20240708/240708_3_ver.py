

subway = [10, 20, 30]
print(subway)
print(subway[0])
print(subway[1])
print(subway[2])



subway = ["푸","피글렛", "티거"]
print(subway)
print(subway.index("피글렛"))
# print(subway.index("이요르")) # err





subway.append("이요르")
print(subway)





subway.insert(1, "루")
print(subway)




print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)

 



# 자료구조 (리스트, 딕셔너리, 튜플, 세트)
# 지하철에서 모두 내림
subway.clear()
print(subway)







# 같은 이름이 몇 명 있는지 확인
subway = ["푸", "피글렛", "티거"]
subway.append("푸") # 푸 추가
print(subway)
print(subway.count("푸"))







num_list = [5, 2, 4, 3, 1]

# num_list.sort() # 오름차순 정렬
# print(num_list)

# num_list.sort(reverse=True) # 내림차순 정렬
# print(num_list)

num_list.reverse() # 순서 뒤집기
print(num_list)






my_list = [1, 3, 2]


my_list.sort() # 리스트 정렬
print(my_list) # my_list 리스트 데이터 변경



your_list = [1, 3, 2]
new_list = sorted(your_list) # 정렬할 리스트를 소괄호 안에 넣음



print(your_list) # your_list 리스트 데이터는 변경되지 않음
print(new_list) # 정렬된 새로운 리스트












mix_list = ["푸", 20, True, [5, 2, 4, 3, 1]]
print("리스트 안에 모두 포함 (문자, 숫자, 불리언, 리스트) : " , mix_list)


mix_list = ["푸", 20, True]
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list) # 리스트 합치기 , 요소로써 하나씩 들어간다.
# append 는 내용을 요소로 풀어서 넣는 것이 아니라, 통으로 1요소에 들어간다.

print(mix_list)
print("합치기 extend : " , num_list)




# 딕션너리 dictionary
cabinet = {3: "푸", 100: "피글렛"}

print(cabinet[3]) # key 3에 해당하는 value
print(cabinet[100]) # key 100에 해당하는 value

print(cabinet.get(3)) # key 3에 해당하는 value
# 5에 해당되는 값이 없기에 None 으로 출력
print(cabinet.get(5)) 
print("hi")

#print(cabinet[5]) # KeyError 발생
print("hi")
print("캐비넷 안에 5가 없으면, 기본 문자 대체 출력. ---> " , cabinet.get(5, "사용 가능")) # key에 해당하는 값이 없으면 기본값을 사용하게 함

print("캐비넷 안에 3이 들었냐? " , 3 in cabinet)
print("캐비넷 안에 5이 들었냐? ", 5 in cabinet)

cabinet = {"A-3": "푸", "B-100": "피글렛"}
print("캐비넷: " , cabinet)
print("A-3 : " , cabinet["A-3"])
print("B-100 : ", cabinet["B-100"])

print("곰돌이 안에 [곰]이 있느냐? ", "곰" in "곰돌이")
print("곰돌이 안에 [돌이]가 있느냐? ", "돌이" in "곰돌이")
print("곰돌이 안에 [푸]가 있느냐? ", "푸" in "곰돌이")



try:
    # 예외가 발생할 가능성이 있는 코드
    #num = int(input("숫자를 입력하세요: ")) 
    num = 2
    result = 10 / num
except ValueError:
    # ValueError 예외가 발생했을 때 실행되는 코드
    print("유효한 숫자를 입력하세요.")
except ZeroDivisionError:
    # ZeroDivisionError 예외가 발생했을 때 실행되는 코드
    print("0으로 나눌 수 없습니다.")
else:
    # 예외가 발생하지 않았을 때 실행되는 코드
    print(f"결과는 {result}입니다.")
finally:
    # 예외 발생 여부와 상관없이 항상 실행되는 코드
    print("프로그램을 종료합니다.")
    
    
    


cabinet = {"A-3": "푸", "B-100": "피글렛"}
print("원본:", cabinet)


cabinet["A-3"] = "티거" # key에 해당하는 값이 있을 때 -> 값 변경
cabinet["C-20"] = "이요르" # key에 해당하는 값이 없을 때 - > 값 추가
print("수정:", cabinet)

del cabinet["A-3"] # key 'A-3'에 해당하는 값 삭제
print("삭제:", cabinet)





print("key  출력: \n\t", cabinet.keys()) # key만 출력
print("value 출력: \n\t" , cabinet.values()) # value만 출력
print("key, value 출력: \n\t", cabinet.items()) # key, value 한 쌍으로 출력

cabinet.clear() # 값 전체 삭제
print("값 전체 삭제: \n\t", cabinet)
 




# 튜플 >>>>>>>>>>> 소괄호를 쓴다. 상수를 묶어둔 것이다.
menu = ("돈가스", "치즈돈가스")
print("menu[0]:", menu[0])
print("menu[1]:", menu[1])

try:
    menu[0] = "dddd"
except:
    print("튜플이라 변경 안됨. ERROR")


name = "피글렛"
age = 20
hobby = "코딩"
print("name, age, hobby --> " , name, age, hobby)



(name, age, hobby) = ("피글렛", 20, "코딩")
print("name, age, hobby -->" , name, age, hobby)
(departure, arrival) = ("김포", "제주")
print("departure > arrival:", departure, ">", arrival) # 김포 > 제주
(departure, arrival) = (arrival, departure)
print("departure > arrival:", departure, ">", arrival) # 제주 > 김포



my_set = {1, 2, 3, 3, 3}
print("my_set : ", my_set)

 

java = {"푸", "피글렛", "티거"} # 자바 개발자 세트
python = set(["푸", "이요르"]) # 파이썬 개발자 세트 , set은 수학의 집합 기능 (중복을 제거한다.)
print("java :", java)
print("python :", python)     
      
# 교집합(자바와 파이썬을 모두 다룰 수 있는 개발자)
print("교집합")
print("java & python:" , java & python)
print("java.intersection(python):", java.intersection(python))
print("java : " , java)

# 합집합(자바 또는 파이썬을 다룰 수 있는 개발자)
print("합집합")
print(java | python)
print(java.union(python))

# 차집합(자바는 할 수 있지만 파이썬은 할 줄 모르는 개발자)
print("차집합")
print(java - python)
print(java.difference(python))



 
 
 
# 파이썬 개발자 추가(기존 개발자: 푸, 이요르)
python.add("피글렛")
print("java:" , java)
print("python:" , python)

# 자바 개발자 삭제(기존 개발자: 푸, 피글렛, 티거)
java.remove("피글렛")
print(java)




menu = {"커피", "우유", "주스"}
print(menu)
print(type(menu))

# 리스트 변환
menu = list(menu) 
print(menu, type(menu))
# 세트 변환
menu = set(menu) 
print(menu, type(menu))
# 튜플 변환
menu = tuple(menu)
print(menu, type(menu))

 






