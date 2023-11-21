#import the Dog class
from dog import Dog

#create three dog objects
dog1 = Dog("Otto", ["spin", "sit", "down", "place"],"German Shepherd")
dog2 = Dog("Baker", ["fetch", "sit", "sit pretty","play dead"], "Labrador Retriever")
dog3 = Dog("Luke", ["lay down", "weave", "heal", "come"], "Golden Retriever")

#create a list of dogs and add each dog to the list
dogs = []
dogs.append(dog1)
dogs.append(dog2)
dogs.append(dog3)

#test the speak funciton
print(dogs[0])
dogs[0].speak()

#test the isHungry function
print(dogs[0].isHungry())
dogs[0].feed()
print(dogs[0].isHungry())

#test the get_tricks and add_tricks functions
print(dogs[0].get_tricks())
dogs[0].add_trick("weave")
print(dogs[0].get_tricks())

#test the get_name and the get_breed functions
print(dogs[0].get_name())
print(dogs[0].get_breed())

