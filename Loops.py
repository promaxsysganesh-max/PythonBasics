#for loop
names = ["Tony", "Steve", "Bruce"]

for name in names:
    print(name)

for i in range(5):
    print(i)


#while loop
count = 1

while count <= 5:
    print(count)
    count += 1

#break pass continue
for i in range(10):
    if i == 5:
        break
    print(i)


for i in range(5):
    if i == 2:
        continue
    print(i)

for i in range(5):
    if i == 3:
        pass
    print(i)

