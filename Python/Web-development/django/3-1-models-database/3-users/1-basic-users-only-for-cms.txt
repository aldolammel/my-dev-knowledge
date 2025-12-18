

VERY BASIC USER SOLUTION:

    If you need user registration through CMS/ADMIN only, without the necessity of creating or updating users from app front-end, so use this simplest default solution:


    PRE) Make sure you understand this:
        ./0-users-setup.txt


    1) Let's explicity define who is the AUTH_USER_MODEL for the app through Core settings.py file:

        # Authentication
        AUTH_USER_MODEL = 'auth.User'  # Addressing the Django default solution.
        # OR if you have a custom user model in apps/accounts/models.py:
        # AUTH_USER_MODEL = 'accounts.CustomUser'  # Format: 'app_label.ModelName'
    
    
    2) Calling the AUTH_USER_MODEL wherever you want, e.g. apps/your_app/models.py:

        E.g.    
            from django.conf import settings as stgs

            class AuditBase(models.Model):
                """Stores who and when things were changed."""

                created_at = models.DateTimeField(
                    auto_now_add=True,
                    verbose_name="Instalado em",
                )
                updated_at = models.DateTimeField(
                    auto_now=True,
                    verbose_name="Atualizado em",
                )
                updated_by = models.ForeignKey(
                    stgs.AUTH_USER_MODEL,
                    editable=False,
                    related_name="%(app_label)s_%(class)s_updated_by",
                    on_delete=models.SET_NULL,
                    null=True,
                    verbose_name="Atualizado por",
                )

                class Meta:
                    abstract = True  # Flags the db to don't create this table!


    3) Making CMS record who has created and/or updated something in CMS:

        E.g.

            >> Asking to the CMS who is the current user using the CMS (in admin.py):

                PageAdmin(admin.ModelAdmin):
                    ...

                    def save_model(self, request, obj, form, change):
                        """Built-in CMS method that allows you to customize what happens when a model is saved through the Django CMS interface."""
                        # Sending to models.py the current user in CMS:
                        obj.save(user=request.user)


            >> Now, tell to the database who is using the CMS (in models.py):

                    class Page(models.Model):
                        ...

                        def save(self, *args, **kwargs):
                            '''Built-in method that's executed when the entry saving runs.'''
                            # Runs full validation before saving:
                            self.full_clean()
                            # Retrieve the user from kwargs, default to None if not passed:
                            user = kwargs.pop("user", None)
                            # Set created_by if this is a new object:
                            if not self.pk and user:
                                self.created_by = user
                            # Otherwise, set updated_by:
                            elif user and user.is_authenticated and user != self.updated_by:
                                self.updated_by = user
                            super().save(*args, **kwargs)

