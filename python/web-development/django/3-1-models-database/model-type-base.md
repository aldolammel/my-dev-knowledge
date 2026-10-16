[model-type-mixin](python/web-development/django/3-1-models-database/model-type-mixin.md)Use a concrete base model ONLY when the base entity is meaningful on its own and you need to query it independently. Use an abstract base model when you only want to reuse fields and methods across child models.

```python
class Vehicle(models.Model):  # Concrete model
    brand = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()


class Car(Vehicle):  # Concrete model
    number_of_doors = models.PositiveSmallIntegerField()


class Motorcycle(Vehicle):  # Concrete model
    engine_capacity = models.PositiveSmallIntegerField()
```

Django creates three tables: `Vehicle`, `Car`, and `Motorcycle`. The child tables reference their corresponding `Vehicle` records.
## Why use a concrete base model?
Suppose your inventory contains 100 cars and 50 motorcycles. You want to manage all 150 vehicles through a single model.
```python
# Create a car:
Car.objects.create(
    brand="Skoda",
    year=2025,
    number_of_doors=4,
)

# Create a bike:
Bike.objects.create(
    brand="Agrale",
    year=1984,
    engine_capacity=750,
)

# Query all vehicles, regardless of their type:
vehicles = Vehicle.objects.all()
# Limitation: Vehicle.objects.all() returns Vehicle instances, not automatically downcast Car and Bike instances.

# Query vehicles from a specific brand
i_love_czech_veh = Vehicle.objects.filter(brand="Skoda")
```
The last two queries are the key benefit: you can query the common vehicle data through `Vehicle` without needing to combine separate `Car` and `Bike` queries manually.

---
## Probably, the best solution would be to use Mixin (Abstract model):
[/python/web-development/django/3-1-models-database/model-type-mixin](/python/web-development/django/3-1-models-database/model-type-mixin.md)

