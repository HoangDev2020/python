
# arr = []
# result = 0
# number = int(input('Enter n: '))
# result += number
# for i in range(0, number, 1):
#     morenum = int(input('Enter more number: '))
#     arr.append(morenum)
#     result += arr[i]
# print(result)   


result = 0
fib = [1,1]
n = int(input('Enter n: '))
for i in range(n - 1):
    arr = fib[len(fib) - 2] + fib[len(fib) - 1]
    fib.append(arr)
result = fib[n]
print(result)