from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "수강생_정보"

# 열로 입력할 데이터를 리스트로 만들어 'data'에 저장
data = [ '이철수', '김미소', '최학준' ]

# for문으로 'A'열의 각 셀에 순서대로 접근하여 데이터를 입력
for i, value in enumerate(data):
    ws.cell(row = i+1 , column = 1 , value = value)

wb.save("수강생_리스트4.xlsx")
wb.close()