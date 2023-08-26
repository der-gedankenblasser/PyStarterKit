#Area of Triangle

a = float(input('Length Of First Side Of Triangle: '))
b = float(input('Length Of Second Side Of Triangle: '))
c = float(input('Length Of Third Side Of Triangle: '))
if (a + b) > c:
    s = (a + b + c)/2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print(' Perimeter of Triangle With Given Sides Is: ', s)
    print(' Area of Triangle With Given Sides Is: ', area)
else:
    print('Invalid Input')
