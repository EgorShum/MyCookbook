x_list = [1, 2, 3]
y_list = [2, 4, 6]

# The bad way
for i in range (len(x_list)):
    x = x_list[i]
    y = y_list[i]
    print(x,y)

print('===========')

# The good way
for x, y in zip(x_list, y_list):
    print(x,y)
