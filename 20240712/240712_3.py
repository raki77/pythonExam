
# - 가변 인자 (variable argument) 
def profile(name, age, *language):
    print("-"*60)
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    print(f"언어 : {len(language)}")
    # print(language, type(language))
    # for lang in language:
    #     print(lang, end=" ") # 언어를 모두 한 줄에 표시        
    
    # for i in range(len(language)):
    #     print(language[i]) 
    print(" | ".join(list(language)))
    print("-"*60) 
    print() # 줄 바꿈 목적

profile("찰리", 20, "파이썬", "자바", "C", "C++", "C#", "자바스크립트")
profile("루시", 25, "코틀린", "스위프트")


# 기초문제 함수1
# 두 개의 인수를 입력받아 
# 더하는 함수를 작성하시오.

# 1. 함수명 sum
# 2. 매개변수는 2개의 int 값으로 한다.
# 3. 함수는 2개의 매개변수를 더해서 반환한다.
# 4. 반환된 값을 출력하시오.

def sum(*_param): 
    result = 0 
    string_list = ", ".join(list(map(str,_param)))
    print(f"입력값은? {string_list} 이고," )
    for i in range(len(_param)):
        result += _param[i]    
    return result 

valSum = sum(100, 150)
print(f"반환된 값은? {valSum} 입니다.")


# 기초문제 함수2
# 사이드 URL 출력하는 함수를 만들어라.
# (닷컴 사이트)
# 1. 함수명은 make_url 입니다.
# 2. URL 출력 하시오.
# 3. 사용은 다음과 같이 할 예정 입니다.

# def make_url(_param):
#     return _param

# url = make_url("naver")
# print(f"URL은 {url} 입니다.")


def make_url(input_string):    
    url_map = {
        "naver": "http://www.naver.com",
        "google": "http://www.google.com",
        "youtube": "http://www.youtube.com"        
    }        
    return url_map.get(input_string.lower(), "Invalid input")
 
url = make_url("naver")
print(url)
url = make_url("google")
print(url)
url = make_url("youtube")
print(url)
url = make_url("xxxxxxxx")
print(url)

