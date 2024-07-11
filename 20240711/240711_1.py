
print("-"* 80)
numb = 5
numb += 2
print(numb)
numb = numb + 2
print(numb)



print("-"* 80) 
from math import * # math 모듈의 모든 기능을 가져다 쓰겠다는 의미 
result = floor(4.99)
print(result) # 4.99의 내림
result = ceil(3.14)
print(result) # 3.14의 올림
result = sqrt(16)
print(result) # 16의 제곱근



print("-"* 80) 
from random import * # random 모듈의 모든 기능을 가져다 쓰겠다는 의미 
print(random())
print(random())
print(random())
print(random() * 10)                     # 0.0 이상 10.0 미만에서 난수 생성
print(int(random() * 10))                 # 0이상 10 미만에서 난수 생성
print(int(random() * 10) + 1)           # 1이상 11미만에서 난수생성
print(int(random() * 45) + 1)           # 1이상 46미만에서 난수 생성
