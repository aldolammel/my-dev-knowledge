

DJANGO > CMS: WAGTAIL

    
    PRE) Assuming you already installed the Wagtail:
        ./_installation.txt

    
    1) First, in Wagtail Home app, go to the models.py and edit that:

        from django.db import models  # keep this even without use now!

        from wagtail.models import Page
        from wagtail.fields import RichTextField

        class HomePage(Page):
            body = RichTextField(blank=True)
            content_panels = Page.content_panels + ["body"]


    2) Make migrations of the model changes:
        $ python manage.py makemigrations
        $ python manage.py migrate


    3) Go to Wagtail Home app, and edit the /my_wagtail_test/home/templates/home/home_page.html:

        {% extends "base.html" %}
        {% load wagtailcore_tags %}
        {% block body_class %}template-blogindexpage{% endblock %}
        {% block content %}
            <h1>{{ page.title }}</h1>
            <div class="intro">{{ page.intro|richtext }}</div>
            {% for post in page.get_children %}
                <h2><a href="{% pageurl post %}">{{ post.title }}</a></h2>
                {{ post.specific.intro }}
                {{ post.specific.body|richtext }}
            {% endfor %}
        {% endblock %}  


    4) Run the Wagtail server and create a Home just with some simple text to test the front-end:

        $ uv run manage.py runserver
            # Go to the browser, create the home and set a 'hello world'. Publish it!
                # In front-end of your wagtail site, you must see your hello word in a blank screen.

    5) Let's install and set an app (sub-app) called, e.g., 'blog':
        
        5.1) Create the app in Django:
            $ python manage.py startapp blog
        
        5.2) Add 'blog' in the INSTALLED_APPS of the <my_wagtail_folder>/settings/base.py!

        5.3) Create each page of this new app where each page is represented by a model. That said, go to the new app models.py file:

            from django.db import models  # keep this even without use now!

            from wagtail.models import Page
            from wagtail.fields import RichTextField

            class BlogIndexPage(Page):   # Wagtail will automatically look for blog_index_page.html!
                intro = RichTextField(blank=True)
                content_panels = Page.content_panels + ["intro"]

            class BlogPage(Page):        # Wagtail will automatically look for blog_page.html!
                date = models.DateField("Post date")
                intro = models.CharField(max_length=250)
                body = RichTextField(blank=True)
                content_panels = Page.content_panels + ["date", "intro", "body"]

        5.4) Make migrations of the model changes:
            $ python manage.py makemigrations
            $ python manage.py migrate

        5.5) In the 'blog' app folder, create folders and file, e.g.:
            # The path and file name:
                .../my_wagtail_folder/blog/templates/blog/blog_index_page.html

                # Its content:
                    {% extends "base.html" %}
                    {% load wagtailcore_tags %}
                    {% block body_class %}template-blogindexpage{% endblock %}
                    {% block content %}
                        <h1>{{ page.title }}</h1>
                        <div class="intro">{{ page.intro|richtext }}</div>
                        {% for post in page.get_children %}
                            <h2><a href="{% pageurl post %}">{{ post.title }}</a></h2>
                            {{ post.specific.intro }}
                            {{ post.specific.body|richtext }}
                        {% endfor %}
                    {% endblock %}

            # The path and file name:
                .../my_wagtail_folder/blog/templates/blog/blog_page.html

                # Its content:
                    {% extends "base.html" %}
                    {% load wagtailcore_tags %}
                    {% block body_class %}template-blogpage{% endblock %}
                    {% block content %}
                        <h1>{{ page.title }}</h1>
                        <p class="meta">{{ page.date }}</p>
                        <div class="intro">{{ page.intro }}</div>
                        {{ page.body|richtext }}
                        <p><a href="{{ page.get_parent.url }}">Return to blog</a></p>
                    {% endblock %}

        5.6) Now, in the Wagtail CMS, lets create the pages of the new app:
            
            x.x.1) Go to http://127.0.0.1:8000/admin and sign in with your admin user details.

            >> Blog home page:
                x.x.2) In the Wagtail admin interface, go to Pages, then click 'Home'.
                x.x.3) Add a child page to the 'Home' page by clicking the + icon (Add child page) at the top of the screen.
                x.x.4) Choose 'Blog index' page from the list of the page types.
                x.x.5) Use “Blog” as your page title, make sure it has the slug “blog” on the Promote tab, and publish it.

            >> Blog post page:
                x.x.6) In the Wagtail admin interface, go to 'Pages', then click 'Home'.
                x.x.7) Hover on 'Blog' and click 'Add child page'.
                x.x.8) Select the page type 'Blog page'.
                x.x.9) Create your first blog post, and publish it!
            
            x.x.X) Test your new app and its pages through the app front-end:
                http://localhost:8000/blog

    x) xxxxx


    x) xxxxx


    x) xxxxx



    x) xxxxx




    x) xxxxx