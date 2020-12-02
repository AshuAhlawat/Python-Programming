# basic for loop
game_names = ["Counter Strike Global Offensive", "Rainbow Six Siege","Dota 2", "League Of Legends", "Greatest 'Shit' Of Our Era Pubg"]

for games in game_names:
    print(games)

# for loop using range(start,stop,incriment)
for i in range(0, 36, 5):
    print(i)
# creating an user name using for loop

names = ["Swakshwar Ghosh", "Gaurav Patel", "Ashwani Ahlawat", "Ankit Kumar"]
usernames = []
for name in names:
    usernames.append(name.lower().replace(" ", "_"))
print(usernames)

for i in range(len(names)):
    names[i] = names[i].lower().replace(" ", "_")
print(names)

# converting user names into name
given_username = ["swakshwar_ghosh","ashwani_ahlawat", "gaurav_patel", "ankit_kumar"]
names = []
for name in given_username:
    names.append(name.title().replace("_", " "))
print(names)
# making a word counter in from a name of a book
name_of_the_book = ['the', 'great', 'expidition','of', 'the', 'great', 'alexander']
word_counter = {}
for word in name_of_the_book:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
print(word_counter)

#factorial using for loops
number=6
product=1
for i in range(2,number+1):
    product=product*i
print(product)