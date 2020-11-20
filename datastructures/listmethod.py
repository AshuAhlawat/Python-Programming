list_of_items = ['aloo', 'bhindi', 'tamatar', 'gajar']

price_of_items = ['10', '8', '16', '20']

print("List of the items in list format: " + str(list_of_items))

print("Price of items in list format: " + str(price_of_items))

# above is just to show the the list

list_of_items_line = "-".join(list_of_items)

price_of_items_line = "- ".join(price_of_items)

print("List of the items in line format: " + str(list_of_items_line))

print("Price of the items in line format: " + str(price_of_items_line))

# making the maximum or minimum from a list

making_a_list = [10, 20, 52, 54, 21, 63, 862, 469]

making_a_list2=[100,200]

making_a_list3=[20,30,50]

maximum_value = max(making_a_list)

minimum_value = min(making_a_list)

sorted_value = sorted(making_a_list)

length_of_a_list = len(making_a_list)

print(maximum_value)

print(minimum_value)

print(sorted_value)

print(length_of_a_list)

print(max([len(making_a_list), len(making_a_list2), len(making_a_list3)]))


print(min([len(making_a_list), len(making_a_list2), len(making_a_list3)]))

# append function
append_list = ['a', 'b', 'c', 'd']

append_list .append('h')

print(append_list)
