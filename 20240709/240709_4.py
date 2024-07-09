# 파이썬으로 LOTTO 추천번호 자동생성 프로그램을 만들어 봅시다.
# 1. random 함수 사용
# 2. 6개 번호 생성 + 1개 번호를 추천. (보너스)
# 3. 번호는 중복되면 안됩니다.
# 4. 1 부터 45 사이의 번호로 추천 되어야 합니다.
# 5. 한번에 5줄 추천 합니다.

import random

def has_duplicates(lst):
    return len(lst) != len(set(lst))

def createNum(cnt):
    idx = 1
    while cnt >= idx:      
        result = [random.randint(1, 46), random.randint(1, 46),random.randint(1, 46),random.randint(1, 46),random.randint(1, 46),random.randint(1, 46), random.randint(1, 46)]        
        while has_duplicates(result) != True:            
            print(result)        
            idx += 1
            break        
        
createNum(5)
    
