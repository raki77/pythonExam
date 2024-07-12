#< 구글 페이지 파일로 저장 >

import requests


# requests.get()으로 웹페이지 가져오기
url = 'http://www.google.com'
response = requests.get(url)



# html requst시 오류발생시 프로그램 종료
response.raise_for_status()



with open ('file_google.html','w', encoding='utf8') as f:
    f.write(response.text)

