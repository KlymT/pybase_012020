a = int(input('Input a  '))

b = str(a)
c = complex(a)
d = bool(a)
e = float(a)
print('str(a) = ', b, ',', 'complex(a) = ', c, ',', 'bool(a) = ', d, ',', 'float(a) = ', e, '.')

f = int(input('Input f  '))
g1 = f + a
g2 = str(f) + b
g3 = f + c
g4 = f + d
g5 = f + e

k1 = f*a
k2 = f*b
k3 = f*c
k4 = f*d
k5 = f*e

print('a + f = ', g1, 'str(a) + str(f) = ', g2, ',',
      'complex(a) + f = ', g3, ',', 'bool(a) + f = ', g4, ',', 'float(a) + f = ', g5, '.')

print('a * f = ', k1, 'str(a) * f = ', k2, ',',
      'complex(a) * f = ', k3, ',', 'bool(a) * f = ', k4, ',', 'float(a) * f = ', k5, '.')