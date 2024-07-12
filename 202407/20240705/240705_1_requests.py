import requests

# requests.get()으로 웹페이지 가져오기
url = 'http://www.naver.com'

response = requests.get(url)
# 응답코드 확인하기
print(response.status_code)
# html requst시 오류발생시 프로그램 종료

response.raise_for_status()

# print(response.text)






