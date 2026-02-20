
"""
    DJANGO > DUNDER METHODS: __INIT__

    This dunder method is called 'constructor' that runs automatically when a class instance is created.

    More about Python Dunder methods:
        /Python/python-knowledge/classes/1-using-magic-dunder-methods.py
"""

# models.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class Order(models.Model):
    order_number = ...
    status = ...
    
    def __init__(self, *args, **kwargs):
        """Dunder method called 'constructor' that runs automatically when a class instance is created."""
        super().__init__(*args, **kwargs)

        # Store original state for tracking changes:
        self._original_status = self.status



# admin.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class ProductAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        """Dunder method called 'constructor' that runs automatically when a class instance is created."""
        super().__init__(model, admin_site)

        # Common uses:
        # 1. Dynamically modify list_display
        # 2. Change admin behavior based on model attributes
        # 3. Set up conditional admin configurations
        
        # Dynamically add all fields to list_display except certain ones
        exclude_fields = ['id', 'description', 'internal_notes']
        self.list_display = [
            field.name for field in model._meta.fields 
            if field.name not in exclude_fields
        ]
        
        # Make all fields searchable
        self.search_fields = self.list_display

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    
    def __init__(self, parent_model, admin_site):
        """Dunder method called 'constructor' that runs automatically when a class instance is created."""
        super().__init__(parent_model, admin_site)
        # Configure inline based on parent:
        if parent_model.__name__ == 'PremiumOrder':
            self.extra = 5  # Show more empty forms!!
            self.fields = ['product', 'quantity', 'price']
        else:
            self.extra = 2
            self.fields = ['product', 'quantity']



# forms.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class MyForm(forms.Form):
    name = forms.CharField()
    
    def __init__(self, *args, **kwargs):
        """Dunder method called 'constructor' that runs automatically when a class instance is created."""
        super().__init__(*args, **kwargs)

        # Common uses:
        # 1. Modify form fields dynamically:
        self.fields['name'].widget.attrs.update({'class': 'special'})
        
        # 2. Remove fields based on conditions:
        if not user_can_edit:
            del self.fields['name']
        
        # 3. Set initial values dynamically:
        self.initial['name'] = get_default_name()



# serializers.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        """Dunder method called 'constructor' that runs automatically when a class instance is created."""
        # Remove custom context:
        self.include_price = kwargs.pop('include_price', True)
        
        super().__init__(*args, **kwargs)
        
        # Dynamically modify fields:
        if not self.include_price:
            self.fields.pop('price', None)



# views.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class ProductListView(ListView):
    model = Product
    
    def __init__(self, **kwargs):
        """Dunder method called 'constructor' that runs automatically when a class instance is created."""
        super().__init__(**kwargs)
        # Set default values:
        self.paginate_by = 20
        self.template_name = f"shop/{self.model._meta.model_name}_list.html"

class CustomTemplateView(TemplateView):
    def __init__(self, **kwargs):
        """Dunder method called 'constructor' that runs automatically when a class instance is created."""
        super().__init__(**kwargs)
        # Initialize view-specific attributes:
        self.extra_context = {'site_name': 'My Shop'}



"""- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

XXXXXXXXXXXXX:
    /xxxxxxxxxxxxxxxxxxxx


"""