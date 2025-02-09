from sklearn.model_selection import train_test_split
import seaborn as sns
import pandas as pd

# 데이터 로드
df = sns.load_dataset("penguins")
print(df.head())

# dataframe을 numpy로 바꾸기 위해서 데이터를 입력데이터와 결과데이터로 나눈다.
print(df.keys)

# 결측치 제거 - NA 이걸 없애야 한다.
# 결측치 있는지? 확인부터 해야 한다.
print("결측치 확인:", df.isna().sum())

# dropna 함수는 1,2,3 특정 축을 기준으로 데이터 삭제시키고 원본은 유지하고
# 삭제된 데이터만 반환한다.
# axis = 0 행, 1 이면 열
df = df.dropna(axis=0)

# 결측치가 남아 있는지 확인한다.
# 결측치 값이 너무 많을 때는 중간 값이나 평균값으로 대체한다.
print("결측치 제거 후:", df.isna().sum())

##############################################################
# 입력 데이터와 출력 데이터 분리

X = df.iloc[:, 2:6]
y = df.iloc[:, 0]

print("입력 데이터(X):")
print(X.head())
print("출력 데이터(y):")
print(y.head())

# 문자열 -> 숫자 인코딩
# 문자열 -> factor 숫자로 바꾸는 작업
# print(y[y=="adel"])

# Name: species, dtype: object
# species
# Adelie       152
# Gentoo       124
# Chinstrap     68
# Name: count, dtype: int64

# 아델에 대한 데이터만 가져와라.
print( y[ y=="Adelie" ]) # true or false
y.iloc[ y == "Adelie"] = 0
y.iloc[ y == "Gentoo"] = 1
y.iloc[ y == "Chinstrap"] = 2
# print(y)
# y = y.replace({"Adelie": 0, "Gentoo": 1, "Chinstrap": 2})
print(y.dtype)
# 정수로 바꾸기
y = y.astype(int)

print("인코딩된 y:", y)
print(y.value_counts())

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=3, test_size=0.4)

print(f"훈련 데이터 크기: X_train {X_train.shape}, y_train {y_train.shape}")
print(f"테스트 데이터 크기: X_test {X_test.shape}, y_test {y_test.shape}")


##################################################################
# KNN 모델 생성 및 훈련
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=9)
model.fit(X_train, y_train)

# 예측 및 결과 출력
pred = model.predict(X_test)
print("예측값:", pred)
print("실제값:", list(y_test))

# 정확도 출력
print("train score:", model.score(X_train, y_train))
print("test score:", model.score(X_test, y_test))
 
print(list(df['species']))
# class_names = list(df['species']) 
# for i, j in zip( pred, y_test) :
#     print("예측 : {:20d} 실제: {:20d}".format(class_names[i], class_names[j])) 



