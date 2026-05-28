

    TRANSLATING: MODEL MANAGERS & MODEL QUERYSETS


        >> xxxxxxxxxxxxxxxxxx


            E.g.

                from parler.managers import TranslatableManager, TranslatableQuerySet

                class MyQuerySet(TranslatableQuerySet):
                    pass

                class MyQuerySetManager(TranslatableManager):
                    pass