from openpyxl import Workbook
  
wb = Workbook()
ws = wb.active
ws.title = "수강생_정보" 
# 열로 입력할 데이터를 리스트로 만들어 'data'에 저장
data = [ '이철수', '김미소', '최학준' ]
 
# A열의 셀을 순회할 수 있는 iterator를 가져오는데, 여기서 최대 행을 'data'의 원소 갯수로 지정
col_cells = ws.iter_cols(min_col=1, max_col=1, max_row=len(data))

# 이중for문으로 B열의 각 셀을 순환하며 'data' 리스트의 원소를 차례대로 입력
for col in col_cells:
    for i, cell in enumerate(col):
        cell.value = data[i]

wb.save("수강생_리스트6.xlsx")
wb.close()