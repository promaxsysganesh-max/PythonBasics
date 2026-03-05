# create a class that takes name and marks of three subjects as a arguments in a constructor.Then create a method to print the average.

class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def print_average(self):
        average = sum(self.marks) / len(self.marks)
        print("Name:", self.name)
        print("Average Marks:", average)


s1 = Student("Ganesh", [85, 90, 80])
s1.print_average()
        