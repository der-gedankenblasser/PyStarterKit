#Prime Numbers 

num = int(input('Enter a Number: '))
if num > 1:
    for i in range(2, int(num/2) + 1):
        if (num % i) == 0:
            print(num, 'is Not a Prime Number')
            break
        else:
            print(num, 'is a Prime Number')
            break
else:
    print(num, 'is Not a Prime Number')