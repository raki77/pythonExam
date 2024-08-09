# numbers=[1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
# numbers=['a','c','a','d','a','b', 'd']
import collections

numbers=['apple','banana','banana','banana','apple']
# counter={}

# # counter[1]=1
# # print(counter)

# for i in numbers:
#     if i in counter:
#         counter[i]=counter[i]+1
#     else:
#         counter[i]=1
    
# print(counter)
print(collections.Counter(numbers))




