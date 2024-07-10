
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
print("male" if jumin_no[7] == "1" else "female")




