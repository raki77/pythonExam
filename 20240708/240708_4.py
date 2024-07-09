

# weather = "비"
weather = "눈"
if weather == "비": # 대입 연산자(=)가 아닌 비교 연산자(==) 사용
    print("우산을 챙기세요.")




weather = "맑음"
if weather == "비":
    print("우산을 챙기세요.")
elif weather == "맑음":
    print("날씨가 맑으니, 썬크림을 바르세요.")
    print("하지만, 외출은 자제 하세요.")


weather = "미세먼지"
if weather == "비":
    print("우산을 챙기세요.") # 1번
elif weather == "미세먼지":
    print("마스크를 챙기세요.") # 2번
else:
    print("준비물이 필요 없어요.")    
    
    
    
    
weather = "맑음"
if weather == "비":
    print("우산을 챙기세요.")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요.")
else:
    print("준비물이 필요 없어요.")
    
    