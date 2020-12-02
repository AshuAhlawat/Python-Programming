x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]
point = []

for point in zip(labels, x_coord, y_coord, z_coord):
    print("{}:{},{},{}".format(*point))

# making a dictionary to create a cast and its height record

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)

# unzipping the tuples

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72),
        ("Lily", 66), ("Marshall", 76))
names, heights = zip(*cast)
print(names)
print(heights)
