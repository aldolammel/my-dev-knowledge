#### Python > Django > CMS customizations
# Creating a field select menu single

---
## Make a decision:

- A) Field: Select menu (dynamic options, but only one to return)
- B) Field: Select menu (static options, but only one to return)

### A) Field: Select menu (dynamic options, but only one to return)

You want your CMS page to show a SELECT MENU with some dynamic options to select just one of them.

Let's build a class/table where you select week by week an 'Artist of the week', and you got new artists to consider always, you should create an Artist() class/table to save all artists you want as option. In the sub-app 'models.py' file, do it:

A.1) In models.py file, create both model classes:
```
class Artist(models.Model):
	name = ...
	is_listed = ...
	
class ArtistOfWeek(models.Model):
	week = ...
	artist_selected = ...
	is_published = ...
```

A.2) In the same code snippet, lets create a relationship between both classes through a foreign key:
```
class ArtistOfWeek(models.Model):
	week = ...
	artist_selected = models.ForeignKey(
		Artist,  # or "Artist" for self-reference
		on_delete=models.CASCADE,
	)
	is_published = ...
```

A.3) In `admin.py` file:
```
from . import models


@admin.register(models.Artist)
class ArtistAdmin(admin.ModelAdmin):
	list_display = ('name', )


@admin.register(models.ArtistOfWeek)
class ArtistOfWeekAdmin(admin.ModelAdmin):
	list_display = ('week', 'artist_selected',)

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		"""Built-in method that allows to override the default formfield for a foreignkeys field."""
		if db_field.name == 'artist_selected':
			# Filter queryset:
			kwargs['queryset'] = models.Artist.objects.filter(is_listed=True)
		return super().formfield_for_foreignkey(db_field, request, **kwargs)

```

A.4) (Optional)

Remove the adding and deleting buttons of Artists ForeignKey field in ArtisOfWeekAdmin:

[/python/web-development/django/4-cms-admin/1-customizing/removing-cms-permission-to-add-for-foreignKey](/python/web-development/django/4-cms-admin/1-customizing/removing-cms-permission-to-add-for-foreignKey.md)

A.5) Only to make sure everything will be ready to test, execute the migration:

```
python manage.py makemigrations <subapp_name>
python manage.py migrate
python manage.py runserver
```

---
### B) Field: Select menu (static options, but only one to return)

    >> You want to show in your CMS a select menu with only with the same options, e.g. a
        select menu called 'status' where the two options always will be 'active' and 'archived':


        B.1) In sub-app models.py, into the class you want apply the select-menu 'status' as attribute:

                class Example(models.Model):
                    status = models.CharField(
                        max_length=10,
                        choices=CHOICES_STATUS,
                        default=VALUE_ACTIVE,
                    )

                # More about:
                    ./model-attr-field-char.txt


        B.2) In the sub-app consts.py (or in the models.py if you prefer), define them:

                # CONSTANTS:
                VALUE_ACTIVE = 'on'       # In postgreSQL 'on' and 'off' are 1/true and 0/false too;
                VALUE_ARCHIVED = 'off'
                CHOICES_STATUS = (
                    (VALUE_ACTIVE, 'Active'),
                    (VALUE_ARCHIVED, 'Archived')
                )


        B.3) Only to make sure everything will be ready to test, execute the migration:

                $ python manage.py makemigrations <subapp_name>
                $ python manage.py migrate
                $ python manage.py runserver
