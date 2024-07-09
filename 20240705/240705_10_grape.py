import matplotlib.pyplot as plt



# 데이터 준비
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]


# 선 그래프 그리기(label 설정 추가하기)
plt.plot(x, y, label = 'graph1')



# 범례 표시
plt.legend()



# 제목 및 축 레이블 추가
plt.title("Graph1")
plt.xlabel("x")
plt.ylabel("y")




# 그래프 보여주기
plt.show()
