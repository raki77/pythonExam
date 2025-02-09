
# 공부시간과 성적을 맞춘다.
# 특성이 하나 - 공부시간 
X = [ [20], [19], [17], [18], [12], [14], [10], [9], [16], [6] ]
y = [ 100, 100, 90, 90, 60, 70, 40, 40, 70, 30 ]

import numpy as np
X = np.array(X)
y = np.array(y)
print( X.shape )
print( y.shape )

# 1. data 나누기
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=3
) 
print(X_train.shape)
print(X_test.shape)


# 선형회귀 분석
from sklearn.linear_model import LinearRegression

# 모델 만들기
model = LinearRegression() 
# 학습하기
model.fit(X_train, y_train)
print("기울기(가중치)", model.coef_)
print("절편", model.intercept_)

# y = model.coef_ * X + model.intercept_

y_pred = model.coef_ * X_test + model.intercept_
y_pred2 = model.predict( X_test)

print( y_test)
print( y_pred)
print( y_pred2)


print("훈련셋", model.score(X_train, y_train))
print("테스트셋", model.score(X_test, y_test))


