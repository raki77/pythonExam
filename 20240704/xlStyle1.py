from openpyxl import Workbook
from openpyxl.styles import Font

wb = Workbook()
ws = wb.active
cell = ws['A1']
cell.value = "Hello World"

# 폰트 스타일 설정: 빨간색, 이탤릭체, 볼드체, 20포인트 사이즈로 설정
cell.font = Font(color='FF0000', 
                 italic=True, 
                 bold=True, 
                 size=20)
wb.save('엑셀 서식.xlsx')


