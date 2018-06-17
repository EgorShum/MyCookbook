print("Converting!")
try:
    print(int('x'))
except:
    print("conversion failed!")
else: # if no-except
    print("Convertion seccessful!")
finally: # Always
    print('Well Done')
print('Done')

# пояснение по finally statement
print("Converting2!")
try:
    print(int('x'))
finally: # Always перед тем как програма крашится мы всеравно запускаем "finally statement"
    print('Well Done2')
print('Done')