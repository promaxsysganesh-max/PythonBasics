
#list methods
lst=[10,20,15,12,25]
print("Original List:",lst)

lst.append(22)
print("Append:",lst)

lst.sort()
print("Sort:",lst)

lst.sort(reverse=True)
print("Sort desc:",lst)

lst.reverse()
print("Revesrse:",lst)

lst.insert(3,22)
print("Insert at idx 3:",lst)

lst.remove(22)
print("Removed 22:",lst)

lst.pop(2)
print("Pop 2:",lst)
