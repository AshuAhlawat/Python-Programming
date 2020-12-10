from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.5, 0.1], size=(100))
# In the above line p is the probality of the random to be in set of the number like the number to be in set 3 is 0.1
# The above code explain that in 100 inputs the probability of set 3 is 0.1 and so on
print(x)

y = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.5, 0.1], size=(3, 5))
print(y)
