class Pet:
    def __init__(self, kind, breed, name):
        self._kind = kind
        self._breed = breed
        self._name = name

    def get_kind(self):
        return self._kind

    def set_kind(self, kind):
        self._kind = kind

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        self._breed = breed

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def print_details(self):
        print(f"Kind: {self._kind}, Breed: {self._breed}, Name: {self._name}")


#This creates the groupings for the pets
pet1 = Pet("Dog", "Golden Retriever", "Sarge")
pet2 = Pet("Cat", "Oreo", "Sebastian")
pet3 = Pet("Lizard", "Salamander", "Leo")

#This creates the details for the pet groupings
pet1.print_details()
pet2.print_details()
pet3.print_details()

#Three of the special functions
print(Pet.__name__)

print(type(pet1))

print(Pet.__module__)
