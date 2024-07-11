

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


print()
ice = {"월드콘":700, "메로나":300, "죠스바":250}
print(ice["월드콘"])
print(type(ice["월드콘"]))
print(ice.keys())
print(ice.values())



ipt = int(input("score:"))
score = {81:"A", 61:"B", 41:"C", 21:"D", 0:"E"} 

for key, value in score.items():
    if ipt < 21:
        ipt = 0
    elif ipt < 41:
        ipt = 21
    elif ipt < 61:
        ipt = 41
    elif ipt < 81:
        ipt = 61
    elif ipt < 101:
        ipt = 81
    else:
        print("Out of lange score")   
    if ipt == key :
        print(f"{value}")
 
 
#딕셔너리 환율 정보를 구성하고 원을 입력받아 4개의 통화로 계산하세요.
currencyDict = {
    "달러" : 1167,
    "엔": 1096,
    "유로" : 1268,
    "위안" : 171
}
resultDict = {}
ipt2 = int(input("단위변환 원하는 금액을 입력하세요(원화단위):"))
for key, value in currencyDict.items():
    if key == "달러" :
        resultDict["달러"] = round(ipt2 / value, 2)
    if key == "엔" :
        resultDict["엔"] = round((ipt2*100) / value, 2)
    if key == "유로" :
        resultDict["유로"] = round(ipt2 / value, 2)
    if key == "위안" :
        resultDict["위안"] = round(ipt2 / value, 2)        
print(resultDict)
