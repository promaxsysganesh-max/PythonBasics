# Ordered

# Changeable (mutable)

# Allows duplicates

# Written using []


numbers = [1, 2, 3, 4]
names = ["Tony", "Steve", "Bruce"]

#accessing element
print(names[0])   # Tony
print(names[1])   # Steve

#updating
names[1] = "Thor"
print(names)

#add elements
names.append("Peter")   # Add at end
names.insert(1, "Loki") # Insert at position


#remove elements
names.remove("Tony")
names.pop()      # removes last element

for name in names:
    print(name)