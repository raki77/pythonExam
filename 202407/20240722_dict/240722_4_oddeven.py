
cnt = 1 
sumOdd = 0
sumEven = 0

while cnt < (100+1):      
    # continue test
    if cnt == 5:
        cnt += 1
        continue 
    
    print(f"{cnt}:", "짝수.(even)" if cnt%2 == 0 else "홀수.(odds)")
    if cnt%2 == 0:   
        sumEven += cnt 
    else:
        sumOdd += cnt 
    cnt += 1
 
    # break test
    if cnt == (10+1):
        break

print("practice while keyword sample code.")
print(f"SumOdd : {sumOdd}")
print(f"SumEven : {sumEven}")



# break, continue test
for i in range(1, 10):
    if i == 5:
        # break
        continue
    else :
        print(i)
   
