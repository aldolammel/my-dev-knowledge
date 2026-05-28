

DJANGO MODEL CLASS > ATTRIBUTE TYPE: SLUG FIELD

    Common Usage:
        A specialized CharField for storing URL-friendly slugs. A slug typically contains only letters, numbers, underscores, or hyphens. It's primarily used for creating clean, readable URLs for objects. It enforces this format with a default validator and is often used with prepopulate_from in the admin to auto-generate from another field (like a title). 

    Field look-like on front-end:
        Generating URLs for blog posts: /blog/my-awesome-post-title/ where my-awesome-post-title is the slug.

    Example:
        
        class Movie(models.Model):
            title = models.CharField(
                max_length=40, 
                blank=False, 
                unique=True,
            )
            slug = models.SlugField(
                unique=True, 
                max_length=200, 
                default='', 
                editable=False,  # Auto-generated in save().
                blank=True,  # Once it's auto-generated in save(), it'll pass empty for clean().
                null=False, 
                db_index=True,
            )

            def save(self, *args, **kwargs):
                """Built-in Model method that's executed when the db entry saving runs."""
                # Runs full validation before saving:
                self.full_clean()
                # Defining the slug based on SEO Title:
                self.slug = slugify(self.title)
                super().save(*args, **kwargs)


        
        In admin.py:

            E.g. 
                class MovieCMS(admin.MovelAdmin):
                    prepopulated_fields = {'slug': ('title',)}

                admin.site.register(Movie, MovieCMS)


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
