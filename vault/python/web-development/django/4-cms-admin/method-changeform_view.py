
"""
    DJANGO CMS > METHODS: CHANGEFORM_VIEW()

    Exclusive to Django Admin, the changeform_view() handles the "add" and "change" form pages in CMS. It's responsible for:
    
    - Displaying forms for creating new objects or editing existing ones
    - Processing form submissions (validation, saving)
    - Handling related inlines
    - Managing permissions and form validation

    >> If you need a method just for "add" handling, use chage_view():
        ./method-change_view.py
"""

# Common example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class ProductAdmin(admin.ModelAdmin):
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        """This build-in method handles the "add" and "change" form pages in CMS."""
        # Call the parent method but add custom logic
        response = super().changeform_view(request, object_id, form_url, extra_context)
        
        # Custom logic after saving
        if request.method == 'POST' and response.status_code == 302:  # Successful save
            if object_id:  # Editing existing product
                product = self.get_object(request, object_id)
                self._check_low_inventory(request, product)
            else:  # Adding new product
                self._log_new_product_addition(request)
        
        return response
    
    def _check_low_inventory(self, request, product):
        """Check if inventory is below threshold after saving"""
        if product.stock_quantity < product.low_stock_threshold:
            messages.warning(
                request, 
                f"Warning: {product.name} has low inventory ({product.stock_quantity} units)"
            )
    
    def _log_new_product_addition(self, request):
        """Log when new products are added via admin"""
        # Could integrate with auditing systems, analytics, etc.
        print(f"New product added by {request.user}")


# Another example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
    """This build-in method handles the "add" and "change" form pages in CMS."""
    # Intercept _add_section and _remove_section before Django Admin tries to validate inlines (which causes ManagementForm errors, blocking the update of page's sections amount):
    if request.method == "POST" and object_id is not None:
        obj = self.get_object(request, object_id)
        if obj:
            if "_remove_section" in request.POST:
                return self._remove_section_from_page(request, obj)
            if "_add_section" in request.POST:
                return self._add_section_to_page(request, obj)
    return super().changeform_view(request, object_id, form_url, extra_context=extra_context)