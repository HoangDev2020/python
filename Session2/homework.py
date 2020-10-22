# number = int(input('Hay nhap so N: '))
# result = 0
# for i in range(1, number+1, 1):
#     result += i
# print(result)

# factorial = int(input('Hay nhap  so N: '))
# result = 1
# for i in range(1, factorial+1, 1):
#     result *= i
# print(result)

# fibonacci = int(input('Hay nhap so N: '))
# prev = 1
# curr = 1
# for i in range(fibonacci-1):
#     curr = temp
#     curr = prev + curr
#     prev = curr
# print(curr)


number = int(input('Enter a number: '))
count = 0
# if number > 0:
#     number /= 10
#     count +=1
while number >= 1:
    number /= 10
    count +=1
    # if 0 < number < 1:
    #     number +=0
    #     count +=0
print(count)

