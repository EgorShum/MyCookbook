needle = 'd'
haystack = ['a', 'b', 'c']

# The bad way
found = False
for letter in haystack:
    if needle == letter:
        print('Found!')
        found = True
        break
if not found:
    print ("Not found!")

# The good way
for letter in haystack:
    if needle == letter:
        print('Found!')
        break
else: # if no-break occurred
    print ("Not found!")
