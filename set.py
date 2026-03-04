# Stores unique values

# No duplicates allowed

# Unordered
numbers = {1, 2, 3, 4}

#no duplicates
nums = {1, 2, 2, 3, 3, 4}
print(nums)


numbers.add(5) #add

numbers.remove(2) #remove

a = {1, 2, 3}
b = {3, 4, 5}

#set operations
print(a | b)   # Union → {1,2,3,4,5}
print(a & b)   # Intersection → {3}
print(a - b)   # Difference → {1,2}