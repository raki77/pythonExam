

print("나는 %d살입니다." % 20)
print("나는 %s을 좋아합니다." % "파이썬")
print("Apple은 %c로 시작해요." % "A")
print("나는 %s살입니다." % 20)




def deposit(balance, money): # 입금 처리 함수
    print("{0}원을 입금했습니다. 잔액은 {1}원입니다.".format(money, balance + money))
    return balance + money # 입금 후 잔액 정보 반환

balance = 0 # 초기 잔액, balance 변수에 초깃값으로 0 저장
balance = deposit(balance, 1000) # 1,000원 입금, balance 변수에 deposit() 함수의 반환값을 다시 저장
#deposit(balance, 1000)





def deposit(balance, money): # 입금 처리 함수
    print("{0}원을 입금했습니다. 잔액은 {1}원입니다.".format(money, balance + money))
    return balance + money # 입금 후 잔액 정보 반환

def withdraw(balance, money): # 출금 처리 함수
    if balance >= money: # 잔액이 출금액보다 많으면
        print("{0}원을 출금했습니다. 잔액은 {1}원입니다.".format(money, balance - money))
        return balance - money # 출금 후 잔액 반환
    else:
        print("잔액이 부족합니다. 잔액은 {0}원입니다.".format(balance))
        return balance # 기존 잔액 반환




balance = 0 # 초기 잔액
balance = deposit(balance, 1000) # 1,000원 입금 
# 출금
balance = withdraw(balance, 2000) # 2,000원 출금 시도
balance = withdraw(balance, 500) # 500원 출금 시도




def deposit(balance, money): # 입금 처리 함수
    print("{0}원을 입금했습니다. 잔액은 {1}원입니다.".format(money, balance + money))
    return balance + money # 입금 후 잔액 정보 반환 

def withdraw_night(balance, money): # 업무 시간 외 출금
    commission = 100 # 출금 수수료 100원
    print("업무 시간 외에 {}원을 출금했습니다." .format(money))
    return commission, balance - money - commission




balance = 0 # 초기 잔액
balance = deposit(balance, 1000) # 1,000원 입금 
# 업무 시간 외 출금 시도
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))








