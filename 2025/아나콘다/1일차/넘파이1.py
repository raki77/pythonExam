# java 의  import 는 클래스명이 길때 귀찮아서 java.lang.String
# import java.lang String
# numpy 라는 모듈을 가지고 와서 이름을 np라는 이름으로 별명을 붙여서 사용하겠다.

import numpy as np

a = [1,2,3,4,5]
b = [2,4,6,8,10]

a1 = np.array(a)
b1 = np.array(b)

print(a1)
print(b1)

c = a + b
c1= a1 + b1

print(type(c), c)
print(type(c1), c1)
 
# list는 추가의 개념 // numpy는 연산의 개념이다.