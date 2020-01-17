a, b = input('What is your Name?'), input('and Surname?')
print('Hello,', a, b, '!',
      'What is your birthday date (dd mm yyyy)?')
a, b, c = int(input('Date')), int(input('Month')), int(input('Year'))
print('Your birthday date is (dd mm yyyy)', a, b, c)
g = 2019 - c
i = (2019 - c)*12 + b
print('You are have been living', g, 'years', 'or', i, 'months')
d = 2019*365 + 10
j = (c - 1)*365 + (b-1)*30 + a
k = d - j
l = int(k/30)
m = int(k/365)
print('Till the date of 10.01.2020 You are have been living', k, 'days', 'or', l, 'months', 'or', m, 'years')
