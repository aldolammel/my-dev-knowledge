#### Python > Django > Views & Serializers
# Converting `QuerySet` to a list

---

xxxxxxxxxxxxxxxx

```python
class SomethingSerializer(...):
	# ...
	def get_sections(self, obj):
		qs = models.ProcSection.objects.filter(procedure=obj.pk)
		if qs.exists():
			return list(qs.values())
		return None
```
Output:
```json
{
	//...,
	"sections":[
		{
			"updated_at":"2026-11-06T20:01:01.819629Z",
			"updated_by_id":1,
			"id":2,
			"procedure_id":1,
			"name":"Warming Up"
		},
		{
			"updated_at":"2026-11-08T15:57:15.874000Z",
			"updated_by_id":1,
			"id":3,
			"procedure_id":1,
			"name":"Fuel"
		},
		//...,
	]
}
```

---



