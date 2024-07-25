import random

minValue = 1
maxValue = 100
targetData = random.randint(1, 100)

i = 1 
while i < 30:     
    guess_number = int(input("1-100 부터 입력하시오:"))
    if targetData > guess_number:
        print("입력한 수 보다 큽니다. [big]")                 
    elif targetData < guess_number:
        print("입력한 수 보다 작습니다. [small]")
        minValue = guess_number  
    else:
        print("good. game end")
        maxValue = guess_number   
        break
    i += 1    
