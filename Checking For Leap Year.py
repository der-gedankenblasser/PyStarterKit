#Checking For Leap Year

year = int(input('Enter a Year To Check For Leap Year: '))
if ((year % 400) == 0 or (year % 100) != 0 and (year % 4) == 0):
    print('Entered Year', year , 'Is A Leap Year')
else:
    print('Entered Year', year , 'Is Not A Leap Year')
