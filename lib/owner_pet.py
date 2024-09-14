class Owner: 
    def __init__(self, name):
        self.name = name
        

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self ]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else: 
            raise Exception("Not a type of pet")

        
    def get_sorted_pets(self):
        owner_pets = self.pets()
        return sorted(owner_pets, key=Pet.get_name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        if pet_type not in Pet.PET_TYPES:
            raise Exception("No Pets")
        
        Pet.all.append(self)

    def get_name(self):
        return self.name
        
    def pet_has_all(self, pet):
       return pet in Pet.all

    