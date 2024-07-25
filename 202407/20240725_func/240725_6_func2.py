def func1():
    print("안녕")
    
# def func2(gift):
#     print(gift+"을 받았다.") 

def func2(*gift):
    for i in gift:
        print(i, "을 받았습니다.") 

def func3():
    return "현금 50,000,000원" 

def func4(gift):
    print(gift + "을 받았습니다.")
    return "삼선짜장면"

func1()
func2("샤넬가방", "루이비통 지갑", "밍크코트")
ret1 = func3()
print(ret1 , "반환 했습니다.")
ret2=func4("10,000원")
print(ret2 , "배달 되었습니다.")


# >>> def prt_many_times2(prm1, prm2):
# ...     for i in range(prm2):
# ...             print(prm1 * i)
# ...
# >>>
# >>> prt_many_times2("helloworld", 10)

# helloworld
# helloworldhelloworld
# helloworldhelloworldhelloworld
# helloworldhelloworldhelloworldhelloworld
# helloworldhelloworldhelloworldhelloworldhelloworld
# helloworldhelloworldhelloworldhelloworldhelloworldhelloworld
# helloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworld
# helloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworld
# helloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworld