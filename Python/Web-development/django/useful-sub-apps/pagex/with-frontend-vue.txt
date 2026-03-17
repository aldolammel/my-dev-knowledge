

DJANGO USEFUL APPS > PAGEX: INTEGRATION WITH VUE


    PRE) Assuming you already installed and integrated Pagex to your Django:
        ._install-and-integration.txt


    1) In core/urls.py:

        Tells Django that Pagex uses Django router-base for its own routes:

            from django.views.generic import TemplateView

            # DJANGO BASIC:
            urlpatterns = [
                ...
                # SUB-APPs, APIs:
                ...
            ]

            # DJANGO > ONLY WHEN DEBUG TRUE:
            ...

            # THIRD-PARTY:
            ...

            # FRONTEND:
            urlpatterns += [
                # This index path's defined in settings > template > dir:
                path("", TemplateView.as_view(template_name="index.html"), name="vue-app"),
                path(
                    "<path:path>",
                    TemplateView.as_view(template_name="index.html"),
                    name="vue-app-paths",
                ),
            ]