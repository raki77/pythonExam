import requests
import json

# 네이버 API 인증 정보
client_id = "jlg1umeqa8"  # 네이버 클라이언트 ID
client_secret = "ZQYodd1zWEP1Zku4O17TaPMyb66CsK59XgFUzOMC"  # 네이버 클라이언트 시크릿

# 출발지 및 도착지 정보
start = '127.1054328,37.3595963'  # 예: 경도,위도 (판교역)
goal = '129.0756416,35.1795543'  # 예: 경도,위도 (부산역)

# 네이버 길찾기 API URL
#url = f"https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving?start={start}&goal={goal}"
url = f"https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving?start={start.split(',')[0]},{start.split(',')[1]}&goal={goal.split(',')[0]},{goal.split(',')[1]}"

# 요청 헤더 설정
headers = {
    'X-NCP-APIGW-API-KEY-ID': client_id,
    'X-NCP-APIGW-API-KEY': client_secret
}

# 요청 보내기
response = requests.get(url, headers=headers)

# 응답 결과 확인
if response.status_code == 200:
    result = response.json()
    print(json.dumps(result, indent=4, ensure_ascii=False))
else:
    print(f"Error: {response.status_code}")
    print(response.text)