

import platform



print("python version : ", platform.architecture())




print(5, type(5))
print(-10)
print(3.14, type(3.14))
print(1000)
print(5 + 3)
print(2*8)
print(2.0, type(6 / 3))
print(3 * (3 + 1))



print('풍선')
print("나비")
print("abcdefg")


print( type("abcdefg"))
print("10")
print("파이썬" * 3)
print("I don't want to go to school") # 정상 출력 따옴표쌍이 잘 맞음
print('I don\'t want to go to school') # 오류 발생 (이렇게 하면 \' 됨)




# boolean 자료형
print('boolean 자료형')
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))



# 자료형 과 변수
# 변수 지정 
# 변수명 = 값
name = "연탄이"
animal = "개"
age = 4
#hobby = "산책"
is_male = True




# 변수의 출력
# 숫자 변수는 str() 사용하여 문자로 형 변환 해야 된다.
# 쉼표도 사용 가능하나 공백이 하나씩 추가되어 출력된다.
print("우리 집 반려동물은 " + animal + "인데, 이름이 " + name + "예요.")
print("우리 집 반려동물은 " + animal + "인데, 이름이 " + name + "이고, " + str(age) +"살 이예요.")
print("우리 집 반려동물은 ", animal, "인데, 이름이 ", name, "이고, ", str(age), "살 이예요.")




# 형 변환
print(int("3"))
# print(int("3") + "입니다.")            # 오류

print(int(3.5))
# print(int("삼"))                           # 오류

print(float("3.5"))
print(float(3))
# print(float("오"))                        # 오류

print(str(3) + "입니다.")
print(str(3.5) + "입니다.")




# type() 사용
print(type(3)) # 정수(int)
print(type("3")) # 문자열(str)
print(type(3.5)) # 실수(float)
print(type(str(3))) # 정수(int)를 문자열(str)로 형변환



# 변수의 특징
# • 변수는 사용하기 전에 정의한다.
hobby = "산책"
print(hobby)

# • 변수는 사용하기 전에 마지막으로 저장한 값을 사용한다.
name = "연탄이"
name = "개"
print(name)



# 주석      (VSCode에서 단축키 : Ctrl + /    또는 지정 시 Ctrl + K + C 해제 시 Ctrl + K + U )
# • 한줄주석
# print(hobby)
# hobby = "산책"

# • 여러줄 주석
'''
    name = "개"
    print(name)
'''
print ("영희")






