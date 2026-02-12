

DJANGO MODEL CLASS > ARGUMENT: ON_DELETE

    The 'on_delete' is an argument to be use with one-to-one and one-to-many (ForeignKey) models where you define what happen with the entire instance if the foreign key is deleted:

        E.g.

            class Director(models.Model):
                ...
            class Movie(models.Model):
                ...
                director = models.ForeignKey(Director, on_delete=..., null=True)


                    >> on_delete=models.CASCADE
                        
                        If the director is deleted, movies linked with them will be deleted.


                    >> on_delete=models.PROTECT

                        If the director is deleted, Django will block the go to preserve
                        the relation.


                    >> on_delete=models.SET_NULL

                        If the director is deleted, movies linked with them will get their
                        director field as 'null'.