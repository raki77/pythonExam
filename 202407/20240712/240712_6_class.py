
# 클래스 기초문제1

# 전화번호 작성
# 1. 이름, 나이, 전번을 기본적으로 작성
# 2. 클래스 명 telAddr 지정
# 3. telBook 리스트 생성해서 클래스 저장하시오.
# 4. telBook 출력하시오
# 5. 클래스 telAddr에는 이름, 나이, 전번 지정하는 멤버 함수 작성 하시오.
# setName(), setAge(), setTel()
# 추가시 append() 사용

# 순희, 24살, 010-625-9928
# 철수, 36살, 010-536-9019
# 말희, 40살, 010-893-0092
# 순신, 26살, 010-772-9920

# 6. telBook = [] 
# telBook.append(인스턴스)


class telAddr:
    telBook = []         
    def __init__(self, *prm1): 
        self.telBook.append(list(prm1))             
        
    def setTelBook(self, *prm):        
        self.telBook.append(list(prm))
        
    def output(self, prm): 
        for key in self.telBook:
            if key[0] == prm :
                print(key)
                break        
    def updateName(self, _origin, _target):
        for key in self.telBook:
            if key[0] == _origin:
                key[0] = _target
                break
    def updateAge(self, _origin, _target):
        for key in self.telBook:
            if key[0] == _origin:
                key[1] = _target
                break
    def updatePhone(self, _origin, _target):
        for key in self.telBook:
            if key[0] == _origin:
                key[2] = _target
                break 
            
test = telAddr("순희", 24, "010-625-9928")
test.setTelBook("철수", 36, "010-536-9019")
test.setTelBook("말희", 40, "010-893-0092")
test.setTelBook("순신", 26, "010-772-9920")
test.output("철수")
test.output("말희")

test.updateName("철수", "철수2") 
test.updateAge("철수2", 40)
test.updatePhone("철수2", "010-9999-1234")
print(test.telBook)
