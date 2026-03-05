# #average of 3 students

# def avgOfStudents(a,b,c):
#     return (a+b+c)/3

# print(avgOfStudents(77,85,80))


# cities=["Delhi","Gurgaon","Noida","Pune","Mumbai","Chennai"]
# heroes=["Thor","Ironman0","Captain America","Shaktiman"]

# def printList(cities1):
#     print(cities1,end=" ")

# printList(cities)   

# def printCount(cities1):
#     print(len(cities1),end=" ")

# printCount(heroes)



# #factorial
# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact*=i
#     return fact

# print(factorial(5))


#Conver USD to INR

# def usd_to_inr(dollar):
#     return (dollar*87)


# usd=int(input("Enter amount of dollar:"))

# print(usd,"USD =",usd_to_inr(usd),"Rupees")



#print N to 1 backward

# def revesePrint(n):
#     if(n==0):
#         return
    
#     print(n)
#     revesePrint(n-1)

# revesePrint(10)


#factorial using recursion

# def factRecursion(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factRecursion(n-1)

# print(factRecursion(5))


#calculate sum of first n natural numbers
# def sumOfNaturalNumber(n):
#     if(n==0):
#         return 0
#     else:
#         return n+sumOfNaturalNumber(n-1)
    
# print(sumOfNaturalNumber(10))


#write a recursive function to print all elements in the list

def printList(lst, index=0):
    if index == len(lst):
        return
    
    print(lst[index])
    
    printList(lst, index + 1)


numbers = [10, 20, 30, 40, 50]
printList(numbers)    