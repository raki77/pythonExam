
# static method는 객체나 클래스에 영향을 미치지 않는 독립적 메소드.
# 메소드 정의할 때 첫번째 인수에 "self"를 기술하지 않는다.
# 메소드 정의 위에 데코레이터 "@staticmethod" 를 기술한다.
# 객체 생성하지 않고, 클래스 이름으로 메소드 실행 시킬 수 있다.
# 객체 생성 후, 객체명으로 메소드 실행 시킬 수도 있다.


class MyClass() :
    total = 0
    
    @staticmethod
    def status():
        print("현재 객체 개수 :", MyClass.total)
        
    def  __init__(self, name):
        self.name = name
        print(self.name + " 객체 생성 됨.")
        MyClass.total += 1
        
MyClass.status()
print()

c1 = MyClass("class 1")
c2 = MyClass("class 2")
c3 = MyClass("class 3")
print()

MyClass.status()
print()

print("<객체로 실행>")
c1.status()
c2.status()
c3.status()





