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
    

dt1 = float(get_exchange_rate('USD'))  
dt2 = float(get_exchange_rate('JPY'))  
dt3 = float(get_exchange_rate('CNY'))  
dt4 = float(get_exchange_rate('EUR')) 

 
# 데이터 준비
# x = [1, 2, 3, 4]
x = ['USD', 'JPY', 'CNY', 'EUR']
#y = [1, 4, 9, 16]
y = [dt1, dt2, dt3, dt4] 

print(y)

# 선 그래프 그리기(label 설정 추가하기)
plt.plot(x, y, label = 'graph1')
 

# 범례 표시
plt.legend()



# 제목 및 축 레이블 추가
plt.title("Graph1")
plt.xlabel("x")
plt.ylabel("y")




# 그래프 보여주기
plt.show()
