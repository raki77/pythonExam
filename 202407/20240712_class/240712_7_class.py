# TEST 클래스 기초문제2
# 은행계좌 클래스 작성
# 1. 클래스 명: Account
# 2. 내용 : 은행명/ 예금주/ 계좌번호/ 잔고
# 3. bank, name, accountNumber, balance
# 4. 저금하는 멤버함수 : deposit
# 5. 인출하는 멤버함수 : withdraw
# 6. 계좌정보 출력 멤버 함수 : display_info

# 우리은행 박위비 74857-993-0029 200000 wori
# 신한은행 김영호 94833-003399 170000 shin


class Account():
    bankInfo = []       
    def __init__(self, *prm1): 
        self.bankInfo.append(list(prm1))  
    def create(self, *prm):        
        self.bankInfo.append(list(prm))
    def deposit(self, *prm):
        for i in range(len(self.bankInfo)):
            if self.bankInfo[i][1] == prm[0] and self.bankInfo[i][2] == prm[1]:
                self.bankInfo[i][3] += prm[2]
                break
    def withdraw(self, *prm):
        for i in range(len(self.bankInfo)):
            if self.bankInfo[i][1] == prm[0] and self.bankInfo[i][2] == prm[1]:
                if self.bankInfo[i][3] <= prm[2]:
                    print("Not enough asset, no balance.")
                else:
                    self.bankInfo[i][3] -= prm[2]
                break
    def display_info(self, prm): 
        for key in self.bankInfo:
            if key[1] == prm :
                print(key)
                break  
    def closeAccount(self, *prm):
        for i in range(len(self.bankInfo)):
            if self.bankInfo[i][1] == prm[0] and self.bankInfo[i][2] == prm[1]:
                del self.bankInfo[i]
                break      

            
mBankInfo = Account("우리은행", "박위비", "74857-993-0029", 200000, "wori")
mBankInfo.create("신한은행", "김영호", "94833-003399", 170000, "shin")
mBankInfo.create("농협", "테스트", "111111-22222", 100000, "nh")

print("-"*60)
print("deposit name : 박위비")
print("-"*60)
mBankInfo.deposit("박위비", "74857-993-0029", 2000)
mBankInfo.display_info("박위비")

print("-"*60)
print("withdraw name : 박위비")
print("-"*60)
mBankInfo.withdraw("박위비", "74857-993-0029", 1000)
mBankInfo.display_info("박위비")
mBankInfo.display_info("김영호")
mBankInfo.display_info("테스트")

mBankInfo.closeAccount("테스트", "111111-22222")
print("-"*60)
print("closeAccount name : 테스트")
print("-"*60)
mBankInfo.display_info("테스트")
print(mBankInfo.bankInfo)