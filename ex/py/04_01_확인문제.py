# numbers=[1,2,3,4,5,6,7,8,9]
# output=[[],[],[]]
# for number in numbers:
#     output[(number+2)%3].append(number)

# print(output)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0, len(numbers) // 2):
    j = (2*i) + 1
    print(f"i={i}, j={j}")
    numbers[j] = numbers[j]**2

print(numbers)
