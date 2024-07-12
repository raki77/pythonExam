 
import pandas as pd

# 샘플 데이터프레임 생성
data = {
    'Name': ['John', 'Anna', 'Mike', 'Sara'],
    'Age': [30, 22, 32, 28],
    'City': ['New York', 'London', 'San Francisco', 'Tokyo']
}
df = pd.DataFrame(data)

# 'Age' 열을 기준으로 오름차순 정렬
df_sorted = df.sort_values(by='Age')

print("Age 기준 오름차순 정렬:")
print(df_sorted)

# 'Age' 열을 기준으로 내림차순 정렬
df_sorted_desc = df.sort_values(by='Age', ascending=False)

print("\nAge 기준 내림차순 정렬:")
print(df_sorted_desc)



# 여러 열을 기준으로 정렬
df_sorted_multiple = df.sort_values(by=['City', 'Age'], ascending=[True, False])

print("\nCity 기준 오름차순 및 Age 기준 내림차순 정렬:")
print(df_sorted_multiple)






import pandas as pd

# 샘플 데이터프레임 생성
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=['a', 'b', 'c'])

df2 = pd.DataFrame({
    'B': [7, 8, 9],
    'C': [10, 11, 12]
}, index=['b', 'c', 'd'])

# 두 데이터프레임을 인덱스와 열을 기준으로 정렬 및 맞춤
df1_aligned, df2_aligned = df1.align(df2, join='outer', axis=0, fill_value=0)

print("df1_aligned:")
print(df1_aligned)
print("\ndf2_aligned:")
print(df2_aligned)






# 샘플 데이터프레임 생성
df = pd.DataFrame({
    'Name': ['John', 'Anna', 'Mike', 'Sara'],
    'Age': [30, 22, 32, 28],
    'City': ['New York', 'London', 'San Francisco', 'Tokyo']
})

# to_string 메소드로 정렬된 출력
print(df)
print(df.to_string(justify='left'))





