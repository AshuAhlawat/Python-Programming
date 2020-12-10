# wap to define a function
def population_density(population, land_area):
    return population/land_area


# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))

# wap that takes  days as input and defines it has how many weeks and howmany days

days=int(input("Enter your  number here: "))
def readable_timedelta(days):
    weeks=int(days/7)
    remianing_days=days%7
    return "in {} days there are {} week(s) and {} day(s)".format(days,weeks,remianing_days)
print(readable_timedelta(days))