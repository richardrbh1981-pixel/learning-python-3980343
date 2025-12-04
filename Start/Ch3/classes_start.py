# LinkedIn Learning Python course by Joe Marini
# Example file for working with classes
class Vehicle:
  def __init__(self, bodystyle):
    self.bodystyle = bodystyle
  def drive(self, speed):
    self.mode = "driving"
    self.speed = speed

class Car(Vehicle):
  def __init__(self, enginetype):
    super().__init__("car")
    self.wheels = 4
    self.doors = 4
    self.engine = enginetype
  def drive(self, speed):
    super().drive(speed)
    print(f"driving my {self.engine} car at {self.speed}")

class Motorcycle(Vehicle):
  def __init__(self, enginetype, hassidecar):
    super().__init__("Motorcycle")
    if (hassidecar):
      self.wheels = 3
    else:
      self.wheels = 2
    self.doors = 0
    self.enginetype = enginetype
  def drive(self, speed):
    super().drive(speed)
    print(f"driving my {self.enginetype} car at {self.speed}")

car1 = Car("gas")
car2 = Car("elecrtric")
mc1 = Motorcycle("gas", True)
print(f"the MC has {mc1.wheels} wheels and engine type is {mc1.enginetype}")
print(f"the car1 has {car1.doors} doors and engine type is {car1.engine}")
car1.drive(20)
car2.drive(40)
mc1.drive(50)