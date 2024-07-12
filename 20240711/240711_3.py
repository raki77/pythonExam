

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


import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup # ver 4

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
rate_info = 0

# 개별 통화 환율 정보 가져오는 함수 만들기
def get_exchange_rate(currency_code):
    url = 'https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_' + currency_code + 'KRW'
        
    # 웹페이지 요청 및 HTML 내용 가져오기
    response = requests.get(url, headers=headers) 
    html_content = response.text
    
    # Beautiful Soup을 사용하여 HTML 내용 파싱
    soup = BeautifulSoup(html_content, 'html.parser')
    # 국가명 추출 및 공백 제거
    country = soup.find('h2').get_text().replace(' ', '')
    # 환율 정보 추출 및 줄바꿈 문자 제거
    rate_info = soup.find('p', class_='no_today').get_text().replace('\n', '')
    rate_info = rate_info.replace('원','').replace(',','')
    return rate_info
    
 

print()
ice = {"월드콘":700, "메로나":300, "죠스바":250}
print(ice["월드콘"])
print(type(ice["월드콘"]))
print(ice.keys())
print(ice.values())



ipt = int(input("score : "))
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
        break  
    if ipt == key :
        print(f"result : {value}")
 


#딕셔너리 환율 정보를 구성하고 원을 입력받아 4개의 통화로 계산하세요.
# currencyDict = { "달러" : 1167, "엔": 1096, "유로" : 1268, "위안" : 171 } 
currencyDict = {
    "달러" : float(get_exchange_rate('USD')),
    "엔": float(get_exchange_rate('JPY')),
    "유로" : float(get_exchange_rate('EUR')),
    "위안" : float(get_exchange_rate('CNY'))
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



# 우편번호는 5자리 입니다. 앞의 3자리가 011부터 019 시작되면 서울 입니다.
# 아래표를 보고 어느 구의 우편 번호 인지 알려주는 프로그램을 작성 하시오.
# 딕셔너리 명은 pos라는 이름으로 구성해서 작성하시오.
# 추가설명 : 010 강북구, 011 강북구, 012강북구, 013 도봉구..)

# 사용자는 01035 입력 # print("안녕하세요? 강북구 주민이시군요") inum = "01035"
sNum = input("우편번호를 입력하시오 : ")
pos = {"01" : ["강북구","강북구","강북구","도봉구","도봉구","도봉구","노원구","노원구","노원구","노원구"]}
tmpLst = []
for key, value in pos.items(): 
    if key == sNum[0:2]:
        tmpLst = value  
try:
    print("안녕하세요?", tmpLst[int(sNum[2:3])] ,"주민이시군요")
except:
    if len(sNum) != 5 :
        print("우편번호 양식에 맞지 않습니다. [Error]")
    else:
        print("포함되지 않는 우편번호 입니다. ["+ sNum +"]")


