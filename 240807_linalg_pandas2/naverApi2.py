# *-- Geocoding 활용 코드 --*
import json
import urllib
from urllib.request import Request, urlopen

# *-- 3개의 주소 geocoding으로 변환한다.(출발지, 도착지, 경유지) --*
# start = '서울특별시 강남역'
# goal = '서울특별시 구로구'
start = '127.1054328,37.3595963'  # 예: 경도,위도 (판교역)
goal = '129.0756416,35.1795543'  # 예: 경도,위도 (부산역)
waypoint = ''
option = ''

# 네이버 API 인증 정보
client_id = 'jlg1umeqa8'  # 네이버 클라이언트 ID
client_secret = 'ZQYodd1zWEP1Zku4O17TaPMyb66CsK59XgFUzOMC'  # 네이버 클라이언트 시크릿

# 주소에 geocoding 적용하는 함수를 작성.
def get_location(loc) :  
    # url = f"https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query=" + urllib.parse.quote(loc)
    # https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving?start=127.1058342,37.359708&goal=129.075986,35.179470
    url = f"https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving?start={start.split(',')[0]},{start.split(',')[1]}&goal={goal.split(',')[0]},{goal.split(',')[1]}"
    print(url)
    # 주소 변환
    request = urllib.request.Request(url)
    request.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
    request.add_header('X-NCP-APIGW-API-KEY', client_secret) 
    response = urlopen(request)
    res = response.getcode()
    print(res)
    # 응답이 정상적으로 완료되면 200을 return한다
    if (res == 200) : 
        print(res)
        # response_body = response.read().decode('utf-8')
        # response_body = json.loads(response_body)
        # print(response_body)
        # # 주소가 존재할 경우 total count == 1이 반환됨.
        # if response_body['meta']['totalCount'] == 1 : 
        	
        #     # 위도, 경도 좌표를 받아와서 return해 줌.
        #     lat = response_body['addresses'][0]['y']
        #     lon = response_body['addresses'][0]['x']
        #     return (lon, lat)
        # else :
        #     print('location not exist')
        
    else :
        print('ERROR')
        
#  함수 적용
get_location(start)
# goal = get_location(goal)
# waypoint = get_location(waypoint)