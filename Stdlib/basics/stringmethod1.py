# there are many methods to do work in python like .format .capitalize .islower .count .title .split
# the given link has the all methods in python : https://docs.python.org/3/library/stdtypes.html#string-methods

my_string = "a quick lazy fox  jumps over the lazy dog"

print(my_string .title())

print(my_string .capitalize())

print(my_string .islower())

my_string1 = "Guys rush {},Cyka {}"

print(my_string1 .format("B", "bliad"))

my_string2 = " pistol round, eco round , buy round, force buy round"

print(my_string2 .count("round"))

x= my_string .find("fox") +1

print(my_string .slice(x))

print(my_string .split('  ',1))

y=my_string .split()
#y.append('@',x)
b=y .index('fox')
print(b)
a=str (y[0:b])
c=str(y[b:])
d=a.split("\', \'")
my_list=[d,c]
print(my_list)

#below is a practice of strings in .format method
# Write two lines of code below, each assigning a value to a variable
value_1="ezz"
value_2="lemon"
# Now write a print statement using .format() to print out a sentence and the 
#   values of both of the variables
print("{} pezzy {} squeezy" .format(value_1,value_2))

