#### Python > Django > CMS
# Many-To-Many field as an horizontal multi-selection field

---

## What:
![](/python/web-development/django/4-cms-admin/0-basic/detailview-m2m-horizontal-multi-selection.jpg)
   
## In admin.py:

        # from:
            filter_horizontal = ()

        # to:
            filter_horizontal = ("seo_global_tags",)

