class Dog:
    def __init__(self,name):#can create attribute and self denotes the instance of the class
        self.name= name
        print(name) 
        #prints names of object as immediately after the creation of object the init method is called and the name is printed
        #even without the print statement afterwards.
    def bark(self):
        print("Woof!")
my_dog= Dog("Buddy")#creating an object of the class and passing
# can use function with separate returns, can use print (name ) inside the init method or can use manual print(mydog.name) for each one of them 