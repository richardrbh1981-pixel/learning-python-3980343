# LinkedIn Learning Python course by Joe Marini
# Example file for working with classes
#

class Vehicle:
  def __init__(self, body_style):
    self.body_style = body_style
    pass

  def drive(self, speed):
    self.mode = "driving"
    self.speed = speed

class Car(Vehicle):
  def __init__(self, engine_type):
    super().__init__("Car")
    self.wheels = 4
    self.doors = 4
    self.engine_type = engine_type

  def drive(self, speed):
    super().drive(speed)
    print("Driving my", self.engine_type, "car at", self.speed)

class Motorcycle(Vehicle):
  def __init__(self, engine_type, has_sidecar):
    super().__init__("Motorcycle")
    if has_sidecar:
      self.wheels = 3
    else:
      self.wheels = 2
    self.doors = 0
    self.engine_type = engine_type
  
  def drive(self, speed):
    super().drive(speed)
    print("Driving my", self.engine_type, "motorcycle at", self.speed)

car1 = Car("Gass")
car2 = Car("Electric")
bike1 = Motorcycle("Gas", False)

car1.drive(30)
car2.drive(60)

bike1.drive(80)

print(bike1.wheels)
print(car1.body_style)
print(car2.engine_type)