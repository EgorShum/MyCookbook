ages = {
    'Mary': 31,
    'Jhonatan': 28,
    # 'Dick':65
    }

# The bad way
if "Dick" in ages:
    age = ages['Dick']
else:
    age = "Unknown"
print("Dick is %s years old" % age)

# The good way
age = ages.get('Dick', 'UnknownX')
print("Dick is %s years old" % age)
