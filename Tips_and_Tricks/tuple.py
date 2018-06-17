x = 10
y = -10

#x, y = 10, -10 Можно так обявлять переменные это будет Tuple
print('Befor: x = %d, y = %d' % (x,y))

# the bad way
tmp = y
y = x
x = tmp

print('After: x = %d, y = %d' % (x,y))
print('x = %s' % x)

# the good way
x, y = y, x
print('After: x = %d, y = %d' % (x,y))
print('x = %d' % x)


