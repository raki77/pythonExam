


name = "연탄이"
animal = "개"
age = 4

print("우리 집 반려동물은 " + animal + "인데, 이름이 " + name + "이고, " + str(age) + "살 입니다.")
print("우리 집 반려동물은 " , animal , "인데, 이름이 " , name , "이고, " , age , "살 입니다.")
print(type(age))

jumin_no = "270330-2673884"
print(jumin_no[:2])
print(jumin_no[:])

print(jumin_no[::2]) # 2씩 뛰어서 출력
print(jumin_no[::3]) # 3씩 뛰어서 출력
print(jumin_no[::4]) # 4씩 뛰어서 출력

print(jumin_no[7:8])
print(jumin_no[7])
print(jumin_no[-7]) 

print("male" if jumin_no[7] == "4" else "female")
print("male" if jumin_no[7] == "1" else "female")




#print(jumin_no[7].index('1'))
url= "http://sharebook.kr"

print(type(url[7:8]))
print(url[-2:])
print(url[17:20]) 
print(url[-4:-1])
print(url[-4:])

print(type(url[17:20])) 
print(jumin_no.replace("-",""))



# 기초문제 9 (strip)
data = "    삼성전자    "
print(data)
print(data.replace(" ",""))

data = "    삼성전자    "
print(data.strip())
print(len(data.strip()))
print(len(data))
print(data.lstrip())
print(data.rstrip())

# for i in data.strip():
#     print(data)
data = data.strip() 
print(data*3)
data = data*3
print(data)
data = "-" * 80
print(data)

print(bin(80))
print(oct(80))
print(hex(80)) 

print(2 ** 3)
print(10 % 3)
print(10 // 3)


mathTeacher = 3
engTeacher = 2
sum = mathTeacher + engTeacher

print("총 선생님:" , sum)
print("수학 선생님은 몇 분이 영어 선생님 보다 많습니까? : ", mathTeacher-engTeacher, "분이 많네요.")
print("전체 선생님은 {}분 이십니다.".format(sum))
print("전체 선생님은 " + str(sum) + "분 이십니다.")
print("전체 선생님은 ", sum ,"분 이십니다.", sep="")

print(bytes("aaaaa", "utf-8"))
print(type(bytes("aaaaa", "utf-8")))


stockCount = "243,554,300"
stockCount = stockCount.split(",")
print(stockCount)
result = ""
for idx in stockCount:
    print(idx)
    result += idx

print(int(result))
print(type(int(result)))

 
s = "Hi 서울"
arr = bytearray(s, 'utf-8')
print(arr)

 

number = 2 + 3 * 4 
print(number)
print(2 + 3 * 4)

number+=2
print(number)


# 리스트 [] 대괄호
# 딕셔너리, 집합set {} 중괄호
# 튜플 () 소괄호



subway = [10,20,30]
print(subway[0])
print(subway[1])
print(subway[2])
print(subway[-1])
print(subway[1:2])

print("-"*80)
print(subway[0:3])
print(subway[:])
print(subway[-3:])
print(subway)

subway.append(40)
print(subway)

print("-"*80)
print(subway.index(20))
print(subway[2:])


subway.insert(1, 15)
print(subway)

subway.pop()
print(subway)

subway.clear()
print(subway)
print(type(subway))


lnum = set([])