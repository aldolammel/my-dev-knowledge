
CUSTOMIZING THE TABLE NAME ON THE CMS:


    >> In the desired class, add the class Meta:

        class Customer(model.Model):
            ...

            class Meta:
                verbose_name = 'Cão'
                verbose_name_plural = 'Alcateia'

        # So on CMS side menu you will see 'Alcateia' and not more 'Clients',
        # in the same way in the customer detail page you'll see 'Cão' and
        # not 'Customer' anymore.
    
    