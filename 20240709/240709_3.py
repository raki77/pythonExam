# 구구단 출력 프로그램 
def gugudan(dan):
    #print(f"--- {dan}단 ---")    
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")
    print("")


for i in range(2, 10):
    gugudan(i)

# 사용자로부터 단수를 입력받음
# try:
#     dan = int(input("출력할 단수를 입력하세요 (1-9): "))
#     if 1 <= dan <= 9:
#         gugudan(dan)
#     else:
#         print("1에서 9 사이의 숫자를 입력해주세요.")
# except ValueError:
#     print("유효한 숫자를 입력해주세요.")


