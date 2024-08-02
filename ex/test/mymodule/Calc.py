# version 3
class Calc:
    # 객체를 초기화 한다.
    # 예약어
    # self : Caculator 있는 애로 초기화하겠다.
    def __init__(self, num1, num2):
        self.num1 = num1    # 인스턴스(=객체) 변수
        self.num2 = num2    # 인스턴스(=객체) 변수
    def add(self): 
        return self.num1 + self.num2
    def subtract(self): 
        return self.num1 - self.num2
    def multiply(self): 
        return self.num1 * self.num2    
    
class SubCalc(Calc):    
    def division(self):        
        if self.num2 == 0:
            print("0으로 나누지 마세요")
        else :
            return self.num1 / self.num2
    def pow(self):         
        return self.num1**self.num2    
