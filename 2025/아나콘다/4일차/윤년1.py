
# 윤년이냐 아니냐? 
# 4로 나누어서 나머지가 0 이고 100으로 나누어서 나머지가 0이 아니어야 한다.
# 400년에 한번씩 윤년
# 함수가 윤년이면 True를 반환, 아니면 False를 반환
def isLeap(year):
    if( year%4 == 0 and year%100 != 0 or year%400 == 0):
        return True
    return False

X = []
y = []
for i in range(1, 2024):
    X.append(i)
    if( isLeap(i)):
        y.append(1)
    else:
        y.append(0)

print(X[:10])
print(y[:10])

# ndarray 타입으로 전환
import numpy as np

X = np.array(X)
y = np.array(y)
print(X.shape)
print(y.shape)

# reshape -> 차원변경함수
# X -> 2차원으로 변경
X = X.reshape(-1, 1)
print(X.shape)
print(y.shape)


########################################################################
# 1. data 나누기
########################################################################
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=3
) 
print(X_train.shape)
print(X_test.shape)
print("="*60)

########################################################################
# 로지스틱 회귀 (분류)
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

# 학습하기
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("로지스틱 회귀 (분류)")
print(model.score(X_train, y_train))
print(model.score(X_test, y_test))
print("="*60)

########################################################################
# KNN 이웃
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=5)

# 학습하기
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("KNN 이웃")
print(model.score(X_train, y_train))
print(model.score(X_test, y_test))
print("="*60)

########################################################################
# 의사결정트리 (항상 과대적합 문제가 있다.)
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()

# 학습하기
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("의사결정트리 (항상 과대적합 문제가 있다.)")
print(model.score(X_train, y_train))
print(model.score(X_test, y_test))
print("="*60)

########################################################################
# 렌덤 포레스트 (과대적합 막기위한 랜덤하게 여러 개의 트리 만들기)
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(max_depth=4)
 
# 학습하기
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("렌덤 포레스트 (과대적합 막기위한)")
print(model.score(X_train, y_train))
print(model.score(X_test, y_test))
print("="*60)


########################################################################
# 그라디언트 부스팅 
from sklearn.ensemble import GradientBoostingClassifier

model = GradientBoostingClassifier()
 
# 학습하기
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("그라디언트 부스팅")
print(model.score(X_train, y_train))
print(model.score(X_test, y_test))
print("="*60)


########################################################################
# 서포트벡터머신
# 차원을 분리해서 (평면을 나누는데 공간을 나눈다.)
# 특징 : 특성 들의 단위가 크게 차이가 나면, 성능이 나빠진다.
# 단위 맞추기 : 정규화, 표준화(normalization)를 반드시 해줘야 한다.
# 딥러닝도 필요하다. 정규화나 표준화를 해야 한다.
def normalize(data):
    return (data - data.min(axis=0)) / (data.max(axis=0) - data.min(axis=0))

from sklearn.svm import SVC

model = SVC()

X_train = normalize(X_train)
X_test = normalize(X_test)
# 학습하기
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("서포트벡터머신")
print(model.score(X_train, y_train))
print(model.score(X_test, y_test))
print("="*60)


