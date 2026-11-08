#### Python > Django > Router
# Path converters

---
## Before:
- Using path converters: [/python/web-development/django/3-2-views-and-API/2-building-urls/3-urls-from-subapp](/python/web-development/django/3-2-views-and-API/2-building-urls/3-urls-from-subapp.md)

---

The following path converters are available by default:
## str:
Matches any non-empty string, excluding the path separator, '/'. 
This is the default if a converter isn’t included in the expression.
## int:
Matches zero or any positive integer. Returns an int.
## slug:
Matches any slug string consisting of ASCII letters or numbers, plus the hyphen 
and underscore characters. For example, building-your-1st-django-site.
## uuid:
Matches a formatted UUID. To prevent multiple URLs from mapping to the same page, 
dashes must be included and letters must be lowercase. 
For example, 075194d3-6885-417e-a8a8-6c931e272f00. Returns a UUID instance.
## path:
Matches any non-empty string, including the path separator, '/'. 
This allows you to match against a complete URL path rather than a segment of a
URL path as with str.


