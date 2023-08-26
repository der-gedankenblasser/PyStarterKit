#Area & Circumference Of Circle

radius = int(input('Enter Radius Of Circle: '))
pi = 3.14
area = pi * radius ** 2
circumference = int(2 * pi * radius)
txt = ' Area Of Cicle With Radius {} Is {} '
txt1 = ' Circumference Of Cicle With Radius {} Is {} '
print(txt.format(radius , area ))
print(txt1.format(radius , circumference ))