from openpyxl import load_workbook

# 엑셀 파일 불러오기
wb = load_workbook(filename = "월별구매고객리스트.xlsx")

# '10월' 시트 불러오기
ws = wb['10월']

# 전체 데이터를 순회하며 읽기
for row in ws.rows:    
    row_values = [cell.value for cell in row]
    print(row_values)

