# -------------------------------------------------------------------------
# 문제01. 다음 표에서 dict_a의 결과가 나오도록 빈칸을 채워보세요.
# -------------------------------------------------------------------------
# dict_a = {}
# dict_a = {"name": "구름"}
# print(dict_a)
# del dict_a['name']
# dict_a.clear()
# print(dict_a)



# -------------------------------------------------------------------------
# 문제02. 다음 빈칸을 채워서 numbers 내부에 들어있는 숫자가
#     몇 번 등장하는지를 출력하는 코드를 작성해보세요.
# -------------------------------------------------------------------------
# numbers = ['a','c','a','d','a','b','d']
# numbers = ['apple', 'banana', 'banana', 'apple']
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}
# # -------------------------------------------------------------------------
# # 밑의 코드와 같은 결과가 나온다. Counter Class 사용
# # import collections
# # print(collections.Counter(numbers))
# # -------------------------------------------------------------------------

for number in numbers:
    if bool(counter) == False :        
        counter[number] = 1        
    else :         
        if number in counter.keys():                 
            counter[number] += 1   
        else :
            counter[number] = 1 
print(counter)




# -------------------------------------------------------------------------
# 순서 정렬하기
# -------------------------------------------------------------------------
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}
for number in numbers:
    if bool(counter) == False :        
        counter[number] = 1        
    else :         
        if number in counter.keys():                 
            counter[number] += 1   
        else :
            counter[number] = 1 

li = list(counter)
li.sort() 
print("정렬 전:", counter)
result=dict(sorted(counter.items()))
print("정렬 후:", result)








# -------------------------------------------------------------------------
# 문제 03. 파이썬은 다음과 같은 방법으로 특정 값이 어떤 자료형인지 확인할 수 있습니다.
# -------------------------------------------------------------------------
character = {
    "name"  :"기사",
    "level" : 12,
    "items"  : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill"  : ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character: 
    if str(type(character[key])).find('dict') > -1: 
        for i in character[key]:
            print(f"{i} : {character[key][i]}") 
    elif str(type(character[key])).find('list') > -1:  
        for i in range(len(character[key])):
            print(f"{key} : {character[key][i]}")
    else :
        print(f"{key} : {character[key]}") 

