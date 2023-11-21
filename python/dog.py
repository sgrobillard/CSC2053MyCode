class Dog:

    #initialize Dog attributes
    def __init__(self,name,tricks,breed,hungry=True):
        self.name = name
        self.tricks = tricks
        self.breed = breed
        self.hungry=hungry

    #to string method returning the name and breed of the dog 
    def __str__(self):
        return self.name + ": " + self.breed
    
    #prints what the dog would "speak"
    def speak(self):
        print("Woof")

    #feeds the dog, therefore changing the hungry attribute
    def feed(self):
        self.hungry = False

    #adds a trick onto the list of tricks the dog can do
    def add_trick(self, trick):
        self.tricks.append(trick)
    
    #returns the name of the dog
    def get_name(self):
        return self.name

    #returns the breed of the dog
    def get_breed(self):
        return self.breed

    #returns a list of the tricks of the dog
    def get_tricks(self):
        return self.tricks
    
    #returns a boolean (true or false) representing if the dog is hungry or not
    def isHungry(self):
        return self.hungry