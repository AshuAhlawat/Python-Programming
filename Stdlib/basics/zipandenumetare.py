items = ['kela', 'aloo', 'shimla mirch', 'tamatar', 'khet ke muli']
weight = [12, 14, 50, 32, 22]
print(list(zip(items, weight)))

# name and age of some aerican actresses in zip form
names = ['lisa ann', 'madison ivy', 'romi rain',
         'aletta ocean', 'kendra lust', 'susy gala']
ages = [48, 31, 32, 32, 42, 27]
for name, age in zip(names, ages):
    print("{}:{}".format(name, age))

# unzipping to tuples

random_list = [('a', 1), ('b', 2), ('c', 3)]
alphabets, numbers = zip(*random_list)
print(alphabets, numbers)

# enumerate
alphas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i, alpha in enumerate(alphas):
    print(i, alpha)
