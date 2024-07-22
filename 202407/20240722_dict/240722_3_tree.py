str1= ''
for i in range(1, 7):
    for j in range(6, i, -1):
        str1 += ' '
    for k in range(0 , 2*i-1):
        str1 += '*'
    str1 += '\n'
    
for i in range(2):
    for j in range(4):
        str1 += ' '
    for k in range(3):
        str1 += "*"
    str1 += '\n'

print(str1)




##--------------------------------------------------------------
# final count down
# result : 1,3,5,7,9,11
##--------------------------------------------------------------
for i in range(7):    
    result = 2*i+1            
    for j in range(11+1):     
        if j == result:
            space = int((11-result)//2)
            print(" "*space + "*"*j)
        else :
            continue  
for x in range(1, 2+1):    
    print(" "*3, "*"*3)       
    