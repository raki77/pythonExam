#< 국가별 환율 정보 >

import requests
from bs4 import BeautifulSoup # ver 4

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}

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
    # 환율 변동 아이콘 찾기
    change_icon = soup.find('span', class_='ico')
 
    # if문으로 전일 대비 환율 변동 기호 확인하기
    if change_icon:
        if 'up' in change_icon['class']:
            change_sign = '▲' # 환율이 상승했을 때
        elif 'down' in change_icon['class']:
            change_sign = '▼' # 환율이 하락했을 때
        elif 'same' in change_icon['class']:
            change_sign = '' # 환율이 변동 없을 때 
 
    # 전일 대비 정보 추출 및 문자열 정리
    exday_info = soup.find('p', class_='no_exday').get_text().replace('\n', '').replace('전일대비', '')
    # 결과 출력
    print(country, currency_code, "실시간 환율", rate_info, '｜ 전일대비', change_sign, exday_info)    
    
# USD, HKD, THB 환율 확인하기
get_exchange_rate('USD')
get_exchange_rate('JPY')
get_exchange_rate('CNY')
get_exchange_rate('EUR')
get_exchange_rate('GBP')
get_exchange_rate('HKD')
get_exchange_rate('THB')
