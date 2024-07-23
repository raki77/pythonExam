# --------------------------------------------------------------
# ppt 04-03
# --------------------------------------------------------------

# 1. 다음 표를 채워 보세요.
#   코드가 여러 개 나올 수 있는 경우 가장 간단한 형태를 넣어 주세요.
li1 = [0,1,2,3,4]
list(range(4, 6))
# [4, 5]
list(range(7, 0, -1))
# [7, 6, 5, 4, 3, 2, 1]
# [3,6,9]
list(range(3, 10, 3))


# 2.빈칸을 채워 키와 값으로 이루어진 각 리스트를 조합해
#   하나의 딕셔너리를 만들어 보세요.
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}
for i in range(len(key_list)) :
    character[key_list[i]] = value_list[i]
print(character)


# 3. 1부터 숫자를 하나씩 증가시키면서 더하는 경우를 생각해 봅시다.
#    몇을 더할 때 10000을 넘는지 구해 보세요. 그리고 그때의 값도
#    출력해 보세요. 다음은 10000이 넘는 경우를 구한 예입니다.

limit = 10000
i = 1
# sum_value 변수 사용
sum_value = 0
while sum_value < limit:    
    sum_value += i
    i += 1 
print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i, limit, sum_value))


sum_value = 0
for x in range(1, limit+1):
    if sum_value > limit:
        i = x
        break
    else :
        sum_value += x  
print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i, limit, sum_value))



# 4. 
# 1부터 100까지의 숫자가 있다고 합시다. 
# 이를 다음과 같이 계산한다고 했을 때, 
# 최대가 되는 경우는 어떤 숫자를 곱했을 때인지를 찾아 주세요. 

max_value = 0
a = 0
b = 0

for i in range(1, 99+1):
    j = 100 - i 
    
    # 최대값 구하기
    if max_value < (i*j) :
        max_value = (i*j)
        a = i
        b = j

print("최대가 되는 경우 : {} * {} = {}".format(a, b, max_value))