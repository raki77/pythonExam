# 문제 : 
# 10000시간이 몇년 몇일인지 계산하는 파이썬 프로그램 작성
# 1. 시간을 일로 계산하시오.
# 2. 일을 년으로 계산하시오.
# 3. 시간을 일로 계산하는 함수 작성하시오.
# 4. 일을 년으로 계산하는 함수 작성하시오.
 
# gTime = 10000

# def timeToDay(gTime) :
#     print(gTime, "시간은, ", gTime//24, "일 입니다.", sep="")
#     return gTime/24

# def dayToYear(pDay) :
#     print(int(pDay//365),"년, ", int(pDay % 365), "일 입니다.", sep="")
#     return pDay/365 

# dayToYear(timeToDay(10000))

####################################################
class outPeriod :
    mTime = 0
    mDay = 0
    def __init__(self, prm1):
        self.mTime = prm1
        
    def timeToDay(self, prm2) :
        print(self.mTime, "시간은, ", self.mTime//prm2, "일 입니다.", sep="")
        self.mDay = self.mTime/prm2        
    
    def dayToYear(self) :
        print(int(self.mDay//365),"년, ", end="")
        print(int(self.mDay % 365), "일 입니다.", sep="") 
    
outClass = outPeriod(10000)
outClass.timeToDay(24)
outClass.dayToYear()
 



# def reverse(data):
#     for index in range(len(data)-1, -1, -1):
#         yield data[index]
        
# for char in reverse('golf'):
#     print(char)


# import statistics
# data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
# print(statistics.mean(data))
# print(statistics.median(data))
# print(statistics.variance(data))

