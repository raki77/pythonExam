#< User Agent 정보 적용 >

import requests
# requests.get()으로 웹페이지 가져오기

url = 'http://www.google.com'
# 내 브라우져에서 조회하는 거다. 라고 구글에 통보.
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)


# html requst시 오류발생시 프로그램 종료
response.raise_for_status()


with open ('file_google.html','w', encoding='utf8') as f:
    f.write(response.text)