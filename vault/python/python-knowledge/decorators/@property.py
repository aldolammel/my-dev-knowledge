
"""
    PYTHON > DECORATOR: @PROPERTY

    The @property is designed for use inside classes, turning a method into an attribute-style access — so instead of calling obj.get_pagex_stgs(), you simply access obj.get_pagex_stgs.
    Note the required self parameter; @property only works on instance methods within a class.

    >> WHAT IT DOES:
        - xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx;

    >> REASON TO USE IT:
        - xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx;
"""

# Example 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

class BlogPost(models.Model):
    is_highlighted = ...
    is_published = ...

    @property
    def is_for_home(self):
        return self.is_highlighted and self.is_published
        

post = BlogPost.objects.get(id=1)
post.is_for_home  # instead of post.is_for_home()


# Example 2 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class xxxxxxxxxxx(models.Model):
    xxxxxxxxxxx