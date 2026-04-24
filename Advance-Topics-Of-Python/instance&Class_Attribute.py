class Dog:
    Species = "Dog"

    def __init__(self,dog_name,breed,age,color,Species):
        self.Species = Species
        self.dog_name = dog_name
        self.breed = breed
        self.age = age
        self.color = color
    
    def dog_info(self):
        print(f"So This dog name is {self.dog_name}, and this dog is of {self.breed} breed. So, {self.dog_name} age is {self.age}, and it is of {self.color}.")


dog1 = Dog("bruno","Labrador",2,"Golden Brown","dog")

print(dog1.Species) # so this is instance attribute
print(Dog.Species) # And this is Class attribute


# Object Introspection
print(dir(dog1))

