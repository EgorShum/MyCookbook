cities = ["Marselle", "Amsterdam", 'New York', 'London']

# The bad way
i = 0
for city in cities:
    print(i,city)
    i += 1

print("============")
# the good way
for i, city in enumerate(cities): # enumerate return list of indexes and cities
    print(i,city)


