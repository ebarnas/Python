#Creating a tuple of using programming classes
programming_classes = ('Intro to Python', 'Advanced Python', 'Database Essentials', 'Web Development Basics', 'Data Structures in Python', 'Web Design Fundamentals')

#Using a loop to print each programming class
print("Programming Classes:")
for class_name in programming_classes:
    print(class_name)

#Using a len function to print of how many programming classes there are
num_classes = len(programming_classes)
print(f"\nNumber of classes in the tuple: {num_classes}")