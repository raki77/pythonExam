
stu_height <-c(166,168,170,172,174)

m <- mean(stu_height)

# 분산
var(stu_height)

# 표준편차
sd (stu_height)

# 상관과 회귀
# observation : 관측치 : 샘플 : object
df <- read.csv( choose.files(), header = TRUE)

cor(df$adv, df$sales)


?lm
# 광고에 따라 매출액의 변화
linear_model1 <- lm('sales ~ adv', df)
linear_model1

summary(linear_model1)
 

0.8879209^2



