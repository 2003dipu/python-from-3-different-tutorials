
# Python inheritance
class Animal:
    alive = True

    def eat(self):
        print("This animal is eating.")
    def sleep(self):
        print("This animal is sleeping.")

class Rabbit(Animal):
    def run(self):
        print("This Rabbit is running. ")
class Fish(Animal):
    def swim(self):
        print("This fish is swimming.")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying.")
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

#print(rabbit.alive)
#fish.eat()
#hawk.sleep()
rabbit.run()
fish.swim()
hawk.fly()

# Python Multilevel Inheritance = when a derived (child) class inherits another derived(child) class
class Organism():
    alive = True

class Animal(Organism):
    def eat(self):
        print("This animal is eating.")

class Dog(Animal):
    def bark(self):
        print("This dog is barking.")
dog = Dog()
print(dog.alive) # inherited form the Organism class
dog.eat()        # inherited from the Animal class
dog.bark()       # defined in dog class  

# Muitiple inheritance = when a child class is derived from more than one parent class

class Prey():

    def flee(self):
        print("This animal flees")

class Predator():

    def hunt(self):
        print("This animal is hunting.")

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

#rabbit.flee()
#hawk.hunt()
fish.flee()
fish.hunt()


