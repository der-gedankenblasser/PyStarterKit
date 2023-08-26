#Multiplication Table

num = float(input('Enter A Number: '))
print('Multiplication Table Of ', num , 'Is : ')
for a in range(1, 11):
    print(num, 'x' , a , '=' , num * a)
