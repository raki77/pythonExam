# 다음 중 enumerate() 함수와 items() 함수의 사용법으로 올바른 것은?
# 현재 인덱스가 몇 번째인지 확인하기 : enumerate()
# list(enumerate([1234324,234,234,234,423]))[1]
# 딕셔너리.items()



# 2진수, 8진수, 16진수로 변환하는 코드는 많이 사용됩니다.
#     다음과 같은 형태로 10진수를 변환할 수 있습니다.
output = [i for i in range(1, 100+1) if f"{i:b}".count("0") == 1]
for x, value in enumerate(output):
    print(f"{value} : {value:b}")
print("합계:", sum(output))



# 숫자의 종류
# 다음리스트에서 몇 가지 종류의 숫자가 사용되었는지 구하는 프로그램을 만들어 보세요. 
# 1, 2, 3, 4가 사용되었으므로 4개가 사용되었다고 출력하면 됩니다
nums = [1,2,3,4,1,2,3,1,4,1,2,3]
count = {}

for i in nums:    
    if bool(count) == False:
        count[i] = 1
    else:
        if i in count.keys():
            count[i] += 1
        else :
            count[i] = 1
print(f"{nums}에서")
print(f"사용된 숫자의 종류는 {len(count.keys())}개입니다.")
print("참고:", count)


# 염기의 개수
# 염기 서열을 입력했을 때 각각의 염기가 몇 개 포함되어 있는지 세는 
# 프로그램을 구현해 보세요
dict1 = {}
ipt1 = input("염기 서열을 입력해 주세요:")
for i in range(len(ipt1)):
    if bool(dict1) == False:
        dict1[ipt1[i]] = 1
    else:
        if ipt1[i] in dict1.keys():
            dict1[ipt1[i]] += 1
        else:
            dict1[ipt1[i]] = 1

for key, val in dict1.items():
    if key.strip() != "":
        print(f"{key}의 개수: {val}")


# 염기 코돈 개수
# 염기 서열을 입력했을 때 어떤 코돈이 몇 개 존재하는지 
# 다음과 같이 출력하는 프로그램을 구현해 보세요.
dict2 = {}
ipt2 = input("염기 서열을 입력해 주세요:")
for i in range(0, len(ipt2), 3):    
    str1 = ""
    try:
        str1 = ipt2[i] + ipt2[i+1] +ipt2[i+2]
    except:
        print("", end="")    
    
    if bool(dict2) == False:
        dict2[str1] = 1
    else:
        if key.strip() != "":
            if str1 in dict2.keys():
                dict2[str1] += 1
            else:
                dict2[str1] = 1 
print(dict2)
 

# 2차원 리스트 평탄화
# 리스트 평탄화(list flatten) - 다음과 같이 리스트가 중첩되어 있을 때
# 중첩을 제거하는 처리
# [1, 2, [3, 4], 5, [6, 7], [8, 9]]이라는 중첩 리스트를 입력했을 때 
# 다음과 같이 출력하는 프로그램을 구현해 보세요.

li1 = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
li2 = []
for i in range(len(li1)):    
    if type(li1[i]) is list:
        for x in li1[i]:
            li2.append(x) 
    else:
        li2.append(li1[i])
print(li2)

