
# 다중 선형 회귀
x1 <- c(2,4,6,8)
x2 <- c(0,4,2,3)
y <- c(81,93,91,97)

linear_model2 <- lm(y ~ x1+x2)
linear_model2


# 교호작용, 다중공선성