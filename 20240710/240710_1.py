try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError as E:
    print("인덱싱 할 수 없습니다.")
    print("ERROR : ", E)


from datetime import datetime
date_str1 = '2024-07-07'
date_str2 = '2024-07-10'

date1 = datetime.strptime(date_str1, '%Y-%m-%d')
date2 = datetime.strptime(date_str2, '%Y-%m-%d')

delta = date2 - date1
print(date1)
print(date2)
print(f"두 날짜의 차이는 {delta.days}일 입니다.")

print(type(3 *(3+1)))