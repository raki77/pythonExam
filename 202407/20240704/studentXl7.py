from openpyxl import Workbook
  
wb = Workbook()
ws = wb.active
ws.title = "수강생_정보" 

# A열과 B열에 입력할 데이터를 이중리스트로 만들어 'data'에 저장
data = [[ '이철수', '김미소', '최학준' ], [ '수학', '영어', '컴퓨터' ]]
 
# 이중for문으로 열의 인덱스 번호와 행의 인덱스 번호로 셀에 데이터를 입력
for col_idx, col_data in enumerate(data, start=1): 
    for row_idx, row_data in enumerate(col_data) :
        ws.cell(row= row_idx +1, column= col_idx, value= row_data)

wb.save("수강생_리스트7.xlsx")
wb.close()