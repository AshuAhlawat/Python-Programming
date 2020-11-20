# to make cubic numbers in python within a range
cubes = [x**3 for x in range(0, 9) if x % 2 == 0]
print(cubes)

cities = ['london', 'kolkata', 'jalandhar', 'delhi', 'mumbai']

captalized_city = [city.title() for city in cities]
print(captalized_city)

# using if-else in list comprehension

squares = [x**2 if x % 2 == 0 else x+3 for x in range(11)]
print(squares)
