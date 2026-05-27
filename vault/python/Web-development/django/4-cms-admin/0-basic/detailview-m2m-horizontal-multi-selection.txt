

DJANGO > CMS: MANY-TO-MANY FIELD AS AN HORIZONTAL MULTI-SELECTION FIELD

    What:
        ./detailview-m2m-horizontal-listing.jpg
    
    In admin.py:

        # from:
            filter_horizontal = ()

        # to:
            filter_horizontal = ("seo_global_tags",)

