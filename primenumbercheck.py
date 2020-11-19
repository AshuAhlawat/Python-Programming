check_prime = [26, 39, 51, 53, 57, 79, 85]
for number in check_prime:
    for i in range(2, int((number+1)/2)):
        if (number % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(number, i, number))
            break
        if i==number-1:
            print("{} is a prime number".format(number))
