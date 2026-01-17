# LinkedIn Learning Python course by Joe Marini
# Example file for working with classes
#

# Base (super) class:
class Vehicle: # class names defined by "class" and uppercase format
  def __init__(self, bodystyle): # initialized function in class
    # Defined on self object, which is a reference to the class
    self.bodystyle = bodystyle # property to hold data that is set equal to 2nd param
  
  # Function that operates on the data in the Vehicle class
  def drive(self, speed):
    self.mode = "driving"
    self.speed = speed # set speed property to the Object speed

# Derived class
class Car(Vehicle): # Car has access to (inherits) bodystyle param from Vehicle
  def __init__(self, enginetype):
    # Initializes the properties in the base (super) class Vehicle
    super().__init__("Car")
    # Now set properties specific to Car
    self.wheels = 4
    self.doors = 4
    self.engine = enginetype # passed in from init function parameter list 

  # Because Car inherits from Vehicle,
  # already has a drive function,
  # but here, behavior is customized by overriding the base class's version
  def drive(self, speed):
    super().drive(speed)
    print("Driving my", self.engine, "car at", self.speed)

# Derived class
class Motorcycle(Vehicle):
  def __init__(self, enginetype, hassidecar):
    super().__init__("Motorcycle")
    if (hassidecar):
      self.wheels = 3
    else:
      self.wheels = 2

    self.doors = 0
    self.enginetype = enginetype # passed in from init parameter list

  # Same here in Motorcycle class
  def drive(self, speed):
    super().drive(speed)
    print("Driving my", self.enginetype, "motorcycle at", self.speed)

# Create objects of those class types
# Note that "self" is not referenced, just the other params
car1 = Car("gas") # references "enginetype" param from Car class
car2 = Car("electric") # references "enginetype" param from Car class again
mc1 = Motorcycle("gas", True) # references "enginetype" & "hassidecar"

# Access class properties using dot notation
print(mc1.wheels)
print(car1.engine)
print(car2.doors)

car1.drive(30)
car2.drive(40)
mc1.drive(50)