# to make cubic numbers in python within a range
cubes = [x**3 for x in range(0, 9) if x % 2 == 0]
print(cubes)

cities = ['london', 'kolkata', 'jalandhar', 'delhi', 'mumbai']

captalized_city = [city.title() for city in cities]
print(captalized_city)

# using if-else in list comprehension

squares = [x**2 if x % 2 == 0 else x+3 for x in range(11)]
print(squares)

# some practise problems

names = ["Rick Sanchez", "Morty Smith",
         "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.lower()for name in names]
print(first_names)

multiples_3=[x*3 for x in range(21)]
print(multiples_3)

#making a list of passed student

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name,score in scores.items() if score>=65]
print(passed)
