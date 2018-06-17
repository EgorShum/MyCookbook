# The bad way
f = open('pimpin-ant-easy.txt')
text = f.read()
for line in text.split('\n'):
    print(line)
f.close()

print('\n=============1111111111==================\n')

# The better way
f = open('pimpin-ant-easy.txt')
for line in f:
    print(line)
f.close()

print('\n=============222222222==================\n')

# The better way
with open('pimpin-ant-easy.txt') as f: # "with" означает before this executed file open and after this execute file closed
    for line in f:
        print(line)
