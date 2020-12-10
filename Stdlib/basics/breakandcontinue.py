manifest = [("banana", 15), ("mattress", 43), ("dog kennel", 42),("machine", 120), ("cheese", 5)]
print("using if-else loop and break statement")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight{}".format(weight))
    if weight >= 100:
        print("the loop ends here")
        break
    else:
        print("adding {}({})" .format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight
print("final items:{}".format(items))
print("final weight:{}".format(weight))

print("\n\n\nthis is by continue statement")

for cargo_name,cargo_weight in manifest:
    print("current weightis {}".format(weight))
    if weight>=100:
        print("breaking the loop")
        break
    elif weight+cargo_weight > 100:
        print("skipping {}({})".format(cargo_name,cargo_weight))
        continue
    else:
        print("adding {}({})".format(cargo_name,cargo_weight))
        items.append(cargo_name)
        weight+=cargo_weight
print("final items{}".format(items))
print("final weight{}".format(weight))

