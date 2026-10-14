#### Python > Django > Forms
# Common attribute-types (form field classes)

---

Most common form field classes used to define attributes in `forms.py`. They validate user input and use a **widget** to determine the HTML element rendered in the template.

| Field Classes on Forms.py                                                                     | Default HTML representation                |
| --------------------------------------------------------------------------------------------- | ------------------------------------------ |
| CharField(max_length=40)                                                                      | `<input type="text">`                      |
| CharField(widget=forms.Textarea)                                                              | `<textarea>`                               |
| ChoiceField(choices=(('v1', 'V 1'), ('v2', 'V 2')))                                           | `<select>`                                 |
| ChoiceField(choices=(('v1', 'V 1'), ('v2', 'V 2')), widget=forms.RadioSelect)                 | `<input type="radio">` (one per choice)    |
| TypedChoiceField(choices=((1, 'V 1'), (2, 'V 2')), coerce=int)                                | `<select>`                                 |
| BooleanField(required=False)                                                                  | `<input type="checkbox">`                  |
| NullBooleanField()                                                                            | `<select>`                                 |
| MultipleChoiceField(choices=(('v1', 'V 1'), ('v2', 'V 2')))                                   | `<select multiple>`                        |
| MultipleChoiceField(choices=..., widget=forms.CheckboxSelectMultiple)                         | `<input type="checkbox">` (one per choice) |
| TypedMultipleChoiceField(choices=..., coerce=int)                                             | `<select multiple>`                        |
| DateField()                                                                                   | `<input type="text">`                      |
| DateField(widget=forms.DateInput(attrs={'type': 'date'}))                                     | `<input type="date">`                      |
| DateTimeField()                                                                               | `<input type="text">`                      |
| DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))                   | `<input type="datetime-local">`            |
| TimeField()                                                                                   | `<input type="text">`                      |
| TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))                                     | `<input type="time">`                      |
| DurationField()                                                                               | `<input type="text">`                      |
| EmailField()                                                                                  | `<input type="email">`                     |
| URLField()                                                                                    | `<input type="url">`                       |
| RegexField(regex=...)                                                                         | `<input type="text">`                      |
| SlugField()                                                                                   | `<input type="text">`                      |
| IntegerField()                                                                                | `<input type="number">`                    |
| FloatField()                                                                                  | `<input type="number">`                    |
| DecimalField(max_digits=6, decimal_places=2)                                                  | `<input type="number">`                    |
| FileField()                                                                                   | `<input type="file">`                      |
| ImageField()                                                                                  | `<input type="file">`                      |
| UUIDField()                                                                                   | `<input type="text">`                      |
| JSONField()                                                                                   | `<textarea>`                               |
| IPAddressField()                                                                              | `<input type="text">`                      |
| GenericIPAddressField()                                                                       | `<input type="text">`                      |
| FilePathField(path='/path/to/files')                                                          | `<select>`                                 |
| ModelChoiceField(queryset=MyModel.objects.all())                                              | `<select>`                                 |
| ModelChoiceField(queryset=MyModel.objects.all(), widget=forms.RadioSelect)                    | `<input type="radio">` (one per choice)    |
| ModelMultipleChoiceField(queryset=MyModel.objects.all())                                      | `<select multiple>`                        |
| ModelMultipleChoiceField(queryset=MyModel.objects.all(), widget=forms.CheckboxSelectMultiple) | `<input type="checkbox">` (one per choice) |
| ComboField(fields=[forms.CharField(), forms.EmailField()])                                    | `<input type="text">`                      |
| MultiValueField(fields=[...])                                                                 | Depends on its widget                      |
| SplitDateTimeField()                                                                          | Depends on its widget                      |
| Field()                                                                                       | No default widget; base class              |
| RegexField(regex=..., widget=forms.PasswordInput)                                             | `<input type="password">`                  |
| CharField(widget=forms.HiddenInput)                                                           | `<input type="hidden">`                    |
==Be aware==
One important distinction for your notes: `forms.py` defines field classes, but `forms.widgets` defines widgets. For example, `forms.DateField()` validates a date, while `forms.DateInput(attrs={'type': 'date'})` controls how the date input is rendered in HTML.

---
## Common attribute-types (field classes):
[/python/web-development/django/3-1-models-database/model-attr-field_all](/python/web-development/django/3-1-models-database/model-attr-field_all.md)


