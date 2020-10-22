number = float(input('Enter a number: '))
count = 0
if number > 0:
    number /= 10
    count +=1
    while number > 1:
        number /= 10
        count +=1
        if 0 < number < 1:
            number +=0
            count +=0
print(count)