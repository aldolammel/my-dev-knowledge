#### Python > Django > Signals
# Basic of signals

---

## Move signals to a dedicated `signals.py` and connect them in `AppConfig.ready()`:

Signal handlers are a classic source of circularity because they often need to import models from other apps. Isolating them avoids polluting `models.py`:

E.g.
```
# /apps/my_subapp/apps.py
from django.apps import AppConfig

class MySubappConfig(AppConfig):
	...
	name = 'apps.my_subapp'

	def ready(self):
		import apps.my_subapp.signals
```