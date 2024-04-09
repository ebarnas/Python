class Pet:
    
    vet_name = "Your Veterinary Office"

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    #This will collect data of the names and pets
    def get_owner_first_name(self):
        return self.__owner_first_name

    def get_owner_last_name(self):
        return self.__owner_last_name

    def get_pet_id(self):
        return self.__pet_id

    def get_pet_name(self):
        return self.__pet_name

    def get_pet_type(self):
        return self.__pet_type

    #This will set the names and pets
    def set_owner_first_name(self, owner_first_name):
        self.__owner_first_name = owner_first_name

    def set_owner_last_name(self, owner_last_name):
        self.__owner_last_name = owner_last_name

    def set_pet_id(self, pet_id):
        self.__pet_id = pet_id

    def set_pet_name(self, pet_name):
        self.__pet_name = pet_name

    def set_pet_type(self, pet_type):
        self.__pet_type = pet_type

    #This is what will display the owners and pets
    def display_pet_info(self):
        print("Pet Information:")
        print(f"Owner's Name: {self.__owner_first_name} {self.__owner_last_name}")
        print(f"Pet ID: {self.__pet_id}")
        print(f"Pet Name: {self.__pet_name}")
        print(f"Pet Type: {self.__pet_type}")
        print(f"Veterinary Office: {Pet.vet_name}")
        print()

#This will check the property values on certain tags
def check_property(pet, prop):
    if hasattr(pet, prop):
        print(f"{prop} exists in the pet object.")
    else:
        print(f"{prop} does not exist in the pet object.")

#This creates the grouping for the pets and owners
pet1 = Pet("Eric", "Barnas", 1, "Buddy")
pet2 = Pet("Holly", "Smith", 2, "Whiskers", "Cat")
pet3 = Pet("Tre", "Johnson", 3, "Rocky")

#This will change the pet type for the first grouping
pet1.set_pet_type("Bird")

#This displays the pet info in the three groupings
pet1.display_pet_info()
pet2.display_pet_info()
pet3.display_pet_info()

#This will check property values on certain tags
check_property(pet1, "owner_first_name")
check_property(pet2, "pet_type")
check_property(pet3, "age")