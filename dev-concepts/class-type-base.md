#### Dev concepts > Object classes
# Base Model class

---

Use a Base Model for shared fields and behavior that define a common foundation for related models.
### Base Model class is not a Mixin class:

| Aspect         | **[Mixin class](/dev-concepts/class-type-mixin.md)** | Base Model class                                                                                            |
| -------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Purpose        | Provides reusable fields or functionality            | Establishes a common foundation for a model hierarchy                                                       |
| Inheritance    | Often shared across unrelated models                 | Usually inherited by models within the same hierarchy                                                       |
| Abstract?      | Typically yes                                        | Can be [abstract](/dev-concepts/class-type-abstract.md) or [concrete](/dev-concepts/class-type-concrete.md) |
| Database table | Usually none                                         | Depends on whether it is abstract                                                                           |
| Example        | `AuditMixin`, `TimestampMixin`                       | `VehicleBase`, `PersonBase`                                                                                 |

---
## Python example:
xxxxxxxxxxxxxxxxxx

---
