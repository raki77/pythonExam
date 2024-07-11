

# 리스트를 만들고 출력하세요. movi
# [] 리스트
# {} 딕셔너리 셋
# () 튜플

gList = []
gList.append("닥터 스트레인지")
gList.append("스플릿")
gList.append("럭키")
print(gList)


gDict = {}
gDict["1"] = "닥터스트레인지"
gDict["2"] = "스플릿"
gDict["3"] = "럭키"
print(gDict)


gTuple = ("닥터스트레인지","스플릿","럭키")
print(gTuple)


gDict2 = { 
    "1": "닥터스트레인지",
    "2": "스플릿",
    "3": "럭키"
}
print(gDict2)

# 키와 값을 열로 출력
print("순위", "|", "영화")
print("-------------")
for key, value in gDict2.items():
    print(f"{key:5}| {value}")


print() 
import pandas as pd
gDict3 = [
            {"순위": "1", "영화": "닥터 스트레인지"},
            {"순위": "2", "영화": "스플릿"},
            {"순위": "3", "영화": "럭키"}
        ] 
res = pd.DataFrame(gDict3).to_string(justify="left")
print(res)



print()
gDict4 = {
    '순위' : [1,2,3],
    '영화' : ["닥터 스트레인지","스플릿","럭키"]    
}
res2 = pd.DataFrame(gDict4).to_string(justify="left")
print(res2)

         
print()
movi = ["닥터 스트레인지", "스플릿", "럭키"]
#for i in movi:
for i in range(len(movi)):
    # print("{}".format(i))
    # print(f"{i}")
    print(f"{movi[i]}")
 

# movi2 = ("닥터 스트레인지", "스플릿", "럭키")
# movi2[0] = "파묘"
# TypeError: 'tuple' object does not support item assignment
# print("Tuple : ", movi)




