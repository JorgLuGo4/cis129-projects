#Script: Pet Class
#Action: This program asks you abot your pet's name, type and age, then stores and displays the information right back at you.
#Author: Jorge Lucero
#Date: 5/7/25

class Pet:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.age = 0

    def setName(self, name):
        self.name = name

    def setType(self, pet_type):
        self.type = pet_type

    def setAge(self, age):
        self.age = age

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getAge(self):
        return self.age

def main():
    my_pet = Pet()

    name = input("Enter a pet name :\n")
    my_pet.setName(name)

    pet_type = input("Enter a pet type :\n")
    my_pet.setType(pet_type)

    age = int(input("Enter a pet age :\n"))
    my_pet.setAge(age)

    print("The pet name is:", my_pet.getName())
    print("The pet type is:", my_pet.getType())
    print("The pet age is:", my_pet.getAge())

# run the main function
main()
