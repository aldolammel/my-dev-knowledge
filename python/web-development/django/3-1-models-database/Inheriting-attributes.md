DJANGO > MODELS: INHERITING ATTRIBUTES

    >> What is attribute:
        /dev-concepts/oop-class-attribute.md


    >> Imagine you re-using common attributes almost are used in all your tables
        like 'created_at', 'updated_at' and 'created_by'. Check this out:


        class CommonBase(models.Model):  # This 'Base' in the name is convention!
            created_at = ...
            created_by = ...
            updated_at = ...
            updated_by = ...

            class Meta:
                abstract = True  # Flags to the db that no tables should be created from this.


        class Post(CommonBase):
            title = ...
            content = ...


        class Comment(CommonBase):
            message = ...


    >> CRITICAL: to avoid errors, remove any foreign key or many-to-many attribute
        from your abstracted/inherited class!

---

MORE ABOUT CLASS META > ABSTRACT:
./meta-abstract.txt

MORE ABOUT INHERITANCE FOR METHODS:
/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
