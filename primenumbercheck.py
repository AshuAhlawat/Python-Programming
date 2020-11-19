check_prime = [11,13,45,59,66,22,10]
for number in check_prime:
    for i in range(2, int((number+1)/2)):
        if (number % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(number, i, number))
            break
        elif i==(number+1)/2:
            print("{} is a prime number".format(number))
        