# print("{:b}".format(10))
# print("{:o}".format(10))
# print("{:x}".format(10))


# print("안녕안녕하세요".count("안"))
tot=0
for i in range(1,100+1):
    # print("{:b}".format(i))
    bi="{:b}".format(i)
    # print(bi)
    if bi.count('0') == 1:
        print(f"{i} : {bi}" )
        tot+=i
    # if '0' in bi:
    #     print(bi, bi.count('0'))


print("합계:",tot)

# output=[i for i in range(1,100+2)]
