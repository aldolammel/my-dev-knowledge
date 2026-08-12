#### Python > Django > Pagex
# Installing Pagex System Elements

---

==DEPRECATED==
Pagex is using signals automatically today!
Currently, this is the solution: [/python/web-development/django/7-middlewares-and-signals/signals/auto-instance-creation-after-migration](/python/web-development/django/7-middlewares-and-signals/signals/auto-instance-creation-after-migration.md)

---

1. Django folder with Pagex already installed;
2. Run basic: `$ uv run manage.py makemigrations`
3. After that, create the empty new migration file for system elements be declared: `$ uv run manage.py makemigrations pagex --empty --name create_system_elements`
4. Do this step detailed below;

## Step 4:

1. Open the generated migration file for create_system_elements (e.g. /apps/pagex/migrations/0002_create_system_elements.py);
2. Add the function below before the `class Migration(migrations.Migration)` declaration;
```
def create_system_elements(apps, schema_editor):
	PagexElmLinkIntPage = apps.get_model(
		"pagex",
		"PagexElmLinkIntPage",
	)
	PagexElmLinkIntCat = apps.get_model(
		"pagex",
		"PagexElmLinkIntCat",
	)
	PagexElmLinkIntTag = apps.get_model(
		"pagex",
		"PagexElmLinkIntTag",
	)
	PagexElmLinkIntPage.objects.get_or_create(
		name="Link Int Page",
		slug="link_int_page",
		css_class="",
	)
	PagexElmLinkIntCat.objects.get_or_create(
		name="Link Int Cat",
		slug="link_int_cat",
		css_class="",
	)
	PagexElmLinkIntTag.objects.get_or_create(
		name="Link Int Tag",
		slug="link_int_tag",
		css_class="",
	)
```
3. Edit the `operations` list in the `Migration` class, asking that to run the System Element creation function:
```
operations = [
	migrations.RunPython(create_system_elements),
]
```
4. Execute the migration: `$ uv run manage.py migrate`
