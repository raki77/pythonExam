# 클래스를 사용하는 이유
# 같은 작업 반복 시 가독성 향상
# 코드 유지관리 편의성 향상

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator() 
cal2 = Calculator() 

print(cal1.add(3)) 
print(cal1.add(4)) 
print(cal2.add(3))                                         
# 인스턴스 : 클래스로 만든 객체를 인스턴스라고 한다.
print(cal2.add(7))


class FourCal:                                                              # 계산기 클래스   self.first, self.second 멤버변수
    def __init__(self, first, second):                                      # add, sub 멤버함수
         self.first = first
         self.second = second
    def setdata(self, first, second):
         self.first = first
         self.second = second
    def add(self):
         result = self.first + self.second
         return result
    def sub(self):
         result = self.first - self.second
         return result
    def div(self):
         result = self.first / self.second
         return result



# 계산기 클래스 사용하기
a = FourCal(4, 2)
res = a.add()
print(f"{a.first} 과 {a.second}을 더하면 {res}입니다.") 
res = a.sub()
print(f"{a.first} 에서 {a.second}를 빼면 {res}입니다.") 



# 상속 : 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용한다.

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
res = a.pow()
print(f"{a.first} ** {a.second}는 {res}입니다.") 



# Method overriding : 부모클래스를 사용하지 않고, 다시 만들어서 사용
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0 :
            return 0
        else :
            return self.first / self.second

#a = SafeFourCal(4, 0)
a = SafeFourCal(4, 2)
res = a.div()
print(f"{int(res)}")


