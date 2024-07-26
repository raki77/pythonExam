# li=[1,2,3,4,1,2,3,1,4,1,2,3]

# print(len(list(set(li))))


# dna='ctacaatgtcagtatacccattgcattagccgg'
# counter={}
# for i in dna:
#     if i in counter:
#         counter[i]=counter[i]+1
#     else:
#         counter[i]=1


# print(counter)

print("=============================================")

# dna='ctacaatgtcagtatacccattgcattagccgg'

# for i in range(len(dna)):
#     # first_idx=i
#     # last_idx=first_idx+3    
#     if i%3==0:
#         first_idx=i
#         last_idx=first_idx+3
#         print()
#         print(dna[first_idx:last_idx])
#     # print(dna[first_idx:last_idx])
        

# print(dna[0:3])

print("=============================================")

# dna='ctacaatgtcagtatacccattgcattagccgg'

# counter={}
# for i in range(len(dna)):
#     # first_idx=i
#     # last_idx=first_idx+3    
#     if i%3==0:
#         first_idx=i
#         last_idx=first_idx+3
#         # print()
#         # print(dna[first_idx:last_idx])
#         k=dna[first_idx:last_idx]
#         if dna[first_idx:last_idx] in counter:           
#             counter[k]=counter[k]+1
#         else:
#             counter[k]=1
#     # print(dna[first_idx:last_idx])

# print(counter)

# print("================최종1======================")

# dna=input("염기 서열을 입력해주세요");

# counter={}
# for i in range(len(dna)):
#     # first_idx=i
#     # last_idx=first_idx+3    
#     if i%3==0:
#         first_idx=i
#         last_idx=first_idx+3
#         # print()
#         # print(dna[first_idx:last_idx])
#         k=dna[first_idx:last_idx]
#         if dna[first_idx:last_idx] in counter:           
#             counter[k]=counter[k]+1
#         else:
#             counter[k]=1
#     # print(dna[first_idx:last_idx])

# print(counter)


print("================최종2======================")

# dna=input("염기 서열을 입력해주세요");

# counter={}
# for i in range(len(dna)):
#     # first_idx=i
#     # last_idx=first_idx+3    
#     if i%3==0:
#         first_idx=i
#         last_idx=first_idx+3
#         # print()
#         # print(dna[first_idx:last_idx])
#         k=dna[first_idx:last_idx]
#         print(len(k), len(k)==3)
#         if dna[first_idx:last_idx] in counter and len(k)==3:
#             counter[k]=counter[k]+1            
#         else:
#             counter[k]=1    

# print(counter)

print("================최종3======================")

dna=input("염기 서열을 입력해주세요");

counter={}
for i in range(0,len(dna), 3):
    codon=dna[i:i+3]
    if len(codon) ==3:
        if codon in counter:
            counter[codon]=1
        else:
            counter[codon]=1
    
    

print(counter)