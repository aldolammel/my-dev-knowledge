

DJANGO MODEL > META CLASS: 

    class Meta inside a model is an inner class used to provide metadata about the model beyond its database fields. It lets you configure various aspects of the model’s behavior without adding actual database columns.

        E.g.

            class MyExample (models.Model):
                attr_1 = ...
                ...

                class Meta:
                    db_table = 'my_customized_example'
                    ...

    
    >> Meta configurations available - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        >> Abstract (avoid the table creation on db):

            ./meta-abstract.txt


        >> Managed (turn off the table management by db):

            ./meta-managed.txt


        >> xxxxxxxx

            ./xxxxxxxxxxxxxxxxxxx


        >> xxxxxxxx

            ./xxxxxxxxxxxxxxxxxxx

        
        >> xxxxxxxx

            ./xxxxxxxxxxxxxxxxxxx