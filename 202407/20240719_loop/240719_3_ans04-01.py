# list_a = [0, 1, 2, 3, 4, 5, 6, 7]
# 다음 표의 함수들을 실행했을 때 list_a의 결과가 어떻게 나오는지 적어보세요

# 1. [0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7]
# 2. [0, 1, 2, 3, 4, 5, 6, 7, 10]
# 3. [0, 1, 2, 0, 3, 4, 5, 6, 7]
# 4. [0, 1, 2, 4, 5, 6, 7]
# 5. [0, 1, 2, 4, 5, 6, 7]
# 6. []

# list_a.extend(list_a)
# list_a.append(10)
# list_a.insert(3, 0)
# list_a.remove(3) # 값 : 3을제거
# list_a.pop(3)
# list_a.clear()
# print(list_a)
 
#  다음 반복문 내부에 if 조건문의 조건식을 채워서 
#  100 이상의 숫자만 출력하게 만들어보세요. 

# numbers = [273,103,5,32,65,9,72,800,99]
# for number in numbers:
#     if number >= 100:
#         print("- 100 이상의 수:" , number)

        
# 빈칸을 채워서 실행 결과에 해당하는 프로그램들을 완성하세요
# numbers = [273,103,5,32,65,9,72,800,99]

# for i in numbers:
#     print(i,"는 짝수입니다." if i%2 == 0 else "홀수입니다.")

# print("-"*60)
# for i in numbers:
#     print(i, "는", len(str(i)), "자릿수입니다.")
    
# print("-"*60)
# for i in numbers:
#     print("{}는 {} 자리수입니다.".format(i, len(str(i))))

# print("-"*60)
# for i in numbers:
#     print(f"{i}는 {len(str(i))} 자리수입니다.")
  
# 다음 코드의 빈칸을 채워서 실행 결과처럼 출력되도록 완성해 보세요
# numbers = [1,2,3,4,5,6,7,8,9]
# output = [[],[],[]]

# for number in numbers: 
#      output[(number-1)%3].append(number)       
# print(output)



# 다음 코드의 빈칸을 채워서 실행 결과처럼 출력되도록 완성해 보세요. 짝수 번째 요소를 제곱하는 것입니다. 
# numbers = [1,2,3,4,5,6,7,8,9]
# for i in range(0, len(numbers)// 2):
#     j = i*2+1
#     print(f"i = {i}, j = {j}")
#     numbers[j] = numbers[j]**2
# print(numbers)





# --------------------------------------------------
# 수업시간 문제
# --------------------------------------------------
# 빈칸을 채워서 실행 결과에 해당하는 프로그램들을 완성하세요
# numbers = [273,103,5,32,65,9,72,800,99]
# odds = []
# result = []
# sum = 0

# for i in numbers:      
#     if i%2 != 0:
#         odds.append(i)    
#     if i%3 == 0:
#         result.append(i)
#         sum += i

# print("홀수:" , odds)
# print("3의 배수:" ,result) 
# print("누적합:", sum)
    