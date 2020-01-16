a, b = input('What is your Name?'), input('and Surname?')
print('Hello,', a, b, '!',
      'What is your birthday date (dd mm yyyy)?')
a, b, c = int(input('Date')), int(input('Month')), int(input('Year'))
print('Your birthday date is (dd mm yyyy)', a, b, c)
d, m, y = 30, 12, 365
f = d*a+m*b+y*c
