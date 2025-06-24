

    MENU: DYNAMIC

    

        1) Create the Section model in the 'general' sub-app, for example:

            E.g.

                class Section(models.Model):
                    id = ...
                    text_name = models.CharField(
                        max_length=30, 
                        unique=True, 
                        blank=False, 
                        null=False,
                        verbose_name='Text Name',
                        help_text='A simple name version to use in the middle of the texts, for example.',
                        
                    )
                    title_name = models.CharField(
                        max_length=80, 
                        unique=True, 
                        blank=False, 
                        null=False,
                        verbose_name='Title Name',
                        help_text='The name that will be available as page titles on browsers, search services, and SEO, for example.',
                    )
                    nav_name = models.CharField(
                        max_length=20, 
                        unique=True, 
                        blank=False, 
                        null=False,
                        verbose_name='Navbar Name',
                        help_text='A short version to be used on the application navegation bar.',
                    )
                    slug = models.SlugField(
                        max_length=255, 
                        unique=True, 
                        blank=False, 
                        null=False,
                    )

                    class Meta:
                        ...

                    def __str__:
                        return self.text_name


                class Page(models.Model):
                    id = ...
                    section = models.ForeignKey(
                        Section, 
                        related_name='pages', 
                        on_delete=models.SET_NULL,
                    )
                    text_name = models.CharField(
                        max_length=30, 
                        unique=True, 
                        blank=False, 
                        null=False,
                        verbose_name='Text Name',
                        help_text='A simple name version to use in the middle of the texts, for example.',
                        
                    )
                    title_name = models.CharField(
                        max_length=80, 
                        unique=True, 
                        blank=False, 
                        null=False,
                        verbose_name='Title Name',
                        help_text='The name that will be available as page titles on browsers, search services, and SEO, for example.',
                    )
                    nav_name = models.CharField(
                        max_length=20, 
                        unique=True, 
                        blank=False, 
                        null=False,
                        verbose_name='Navbar Name',
                        help_text='A short version to be used on the application navegation bar.',
                    )
                    slug = models.SlugField(
                        max_length=255, 
                        unique=True, 
                        blank=False, 
                        null=False,
                    )
                    body = models.TextField(
                        blank=False, 
                        null=False,
                    )

                    class Meta:
                        ...

                    def __str__:
                        if self.section:
                            return f'{self.section} > {self.text_name}'
                        return f'WARNING: {self.text_name} page has no section!'



        2) Create the 'context_processors.py' file in the 'general' sub-app:

            E.g.

                from .models import Section

                def menu_sections(request):
                    sections = Section.objects.all()
                    context = {'menu_sections': sections}
                    return context


        3) Register the context_processors function in the settings.py file:

            TEMPLATES = [
                {
                    ...
                    'OPTIONS': {
                        'context_processors': [
                            # DJANGO DEFAULT GLOBAL CONTEXTS:
                            ...
                            # DJANGO ADDITIONAL GLOBAL CONTEXTS:
                            ...
                            # THIRD-PARTY GLOBAL CONTEXTS:
                            ...
                            # APP CUSTOM GLOBAL CONTEXTS:
                            '<subapp_name>.context_processors.menu_sections',
                        ],
                    },
                },
            ]


        4) Calling the menu in the navegation template/front-ent:

            E.g.

                <div id="main-navbar" class="navbar-menu">
                    <div class="navbar-end">
                        {% for section in menu_sections %}
                            <a href="{% url '<subapp_namespace>:<pattern_name>' <section.slug> %}" class="navbar-item">{{ section.title }}</a>
                        {% endfor %}
                    </div>
                </div>