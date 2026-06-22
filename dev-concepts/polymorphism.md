#### Dev concepts
# Polymorphism / Polymorphic
---
It allows a value or variable to have more than one type and allows a given operation to be performed on values of more than one type. In object-oriented programming, polymorphism is the provision of one interface to entities of different data types. The concept is borrowed from a principle in biology in which an organism or species can have many different forms or stages.

Polymorphism allows you to call the same method on different objects and get different behavior.

E.g. using **Python**:

**Simplest:**
```
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())
```
Output:
```
Woof!
Meow!
```

**Better to get it:**
```
# PARENT CLASS - - - - - - - - - - - - - - -
class Vehicle:
    def move(self):
        print("Moving")

# CHILD CLASSES - - - - - - - - - - - - - - 
class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")
        
class Boat(Vehicle):
	pass

vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()
```
Output:
```
Driving
Flying
Moving
```

---
## Python with Django Polymorphic:
[/python/web-development/django/component-libraries/django-polymorphic/0-djangopolymorphic](/python/web-development/django/component-libraries/django-polymorphic/0-djangopolymorphic.md)
