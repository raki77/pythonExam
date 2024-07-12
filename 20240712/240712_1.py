# import random

# student = []  
# info = { "num" : 0 , "score" : { "korean" : 0,"english" : 0,"math" : 0},"total" : 0,"avg" : 0 }
# for i in range(9):    
#     student.append(info)   
#     tmp = student[i] 
#     tmp["num"] = i+1 
#     score = tmp["score"]
#     score["korean"] = random.randint(1, 100)             
#     score["english"] = random.randint(1, 100) 
#     score["math"] = random.randint(1, 100) 
#     tmp["total"] = score["math"] + score["english"] + score["korean"]
#     tmp["avg"] = round(tmp["total"]/3, 1)             
#     print(tmp)         
    

# 형설고등학교 3학년 기말고사 수학, 영어, 국어의 성적을 딕셔너리로 구축하고
# 각 개인의 평균과 총점을 구하세요.
# 1. 키로 학번을 사용 하는데, 1번 ~ 9번까지 있슴
# 2. 수학, 영어, 국어 순으로 점수 값만 딕셔너리로 구성하라
# 3. 평균은 소수점 1자리에서, 반올림하셔서 정수로 출력하라
# 4. 총점도 표시하고, 실행하면 1번~ 9번까지 성적 목록을 출력하라.
# 5. 학번, 국어, 영어, 수학, 총점, 평균 순으로 목록을 출력하라.


import random
import numpy

student = []  
info = {"num":0, "score":[], "total":0, "avg":0} 
for i in range(9):   
    student.append(info)
    tmp = student[i]
    tmp["num"] = i + 1
    tmp["score"] = random.sample(range(0, 100), 3)        
    tmp["total"] = numpy.sum(tmp["score"]) 
    tmp["avg"] = round(numpy.average(tmp["score"]), 1)
    print(tmp) 


 
import random
import numpy

gimal = {i : random.sample(range(60, 100), 3) for i in range(1,10)}
print(gimal)

# print('학번', '국어', '영어', '수학', '총점', '평균')
# for item in gimal.items() :    
#     print(f'{item[0]:2} {item[1][0]:4} {item[1][1]:4} {item[1][2]:4} {numpy.sum(item[1]):4} {int(round(numpy.average(item[1]),0)):3} ')

def scor(hakbun):
    print("="*60)
    print('학번', '국어', '영어', '수학', '총점', '평균')
    print("-"*60)
    for i in range(1, hakbun+1):
        sList = gimal[i]
        tot = sList[0] + sList[1] + sList[2]
        ave = round(tot/3, 1)        
        print(f" {i},  {sList[0]},  {sList[1]},  {sList[2]},  {tot},  {ave} ")  #print(f"수학 : {sList[0]}, 영어 : {sList[1]}, 국어 : {sList[2]}, 합계 : {tot}, 평균 : {ave}")
scor(5)

