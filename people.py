class Person:
    def __init__(self, name, address, age, phone_number):
        self._name = name
        self._address = address
        self._age = age
        self._phone_number = phone_number

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

# Creating instances of the Person class
person1 = Person("Eric", "11435 Chilling St", 20, "224-253-7842")
person2 = Person("Holly", "45613 Depressed St", 20, "224-543-7659")
person3 = Person("Tre", "78921 Homie St", 45, "112-252-3332")

# Displaying information stored in each instance
print("Person 1:")
print("Name:", person1.get_name())
print("Address:", person1.get_address())
print("Age:", person1.get_age())
print("Phone Number:", person1.get_phone_number())


print("Person 2:")
print("Name:", person2.get_name())
print("Address:", person2.get_address())
print("Age:", person2.get_age())
print("Phone Number:", person2.get_phone_number())


print("Person 3:")
print("Name:", person3.get_name())
print("Address:", person3.get_address())
print("Age:", person3.get_age())
print("Phone Number:", person3.get_phone_number())