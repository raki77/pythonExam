def add(a, b):
    return a + b

def sub(a, b): 
    return a-b


if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))
    

# 엉뚱하게도 import mod1을 수행하는 순간 mod1.py 파일이 실행되어 결과값을 출력한다. 
# 우리는 단지 mod1.py 파일의 add와 sub 함수만 사용하려고 했는데 말이다.
# 이러한 문제를 방지하려면 mod1.py 파일을 다음처럼 수정해야 한다.

# if __name__ == "__main__"을 사용하면 C:\doit>python mod1.py처럼 직접 이 파일을 실행했을 때는__name__ == "__main__"이 참이 되어 
# if 문 다음 문장이 수행된다. 

# 이와 반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러 사용할 때는 __name__ == "__main__"이 거짓이 되어 
# if 문 다음 문장이 수행되지 않는다.

 