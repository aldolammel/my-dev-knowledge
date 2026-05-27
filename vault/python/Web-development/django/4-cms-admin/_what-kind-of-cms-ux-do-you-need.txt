

DJANGO > CMS: WHAT KIND OF FORM DO YOU NEED


    A list of different approaches to list and/or visualize existing entries in the database. Below, you see a title, a description about the desired UX in CMS, and then the step-by-step to build up that.


    - - - - -


    A) Regular Django behavior:
    
        For new objects, click add button, and then, in the adding detail-view, you add the new object data; for existing objects, you access the object list-view and see all its entries listed where each of them are linked for its existing object detail-view;

            A1. Create the model class in models.py;
            A2. Register the model class as admin class in admin.py;
            A3. Access the CMS, and test it.

    
    B) Adding form based in a pre-option-selection / Existing form based on entry type selected:
    
        For new objects, through the adding detail-view, select an option first (using a radio or dropdown menu), and then Django loads the specific form (still in detail-view) based on the previous selection. For existing entries through the list-view, each listed entry, if clicked, loads its specific form based in a specific model (with its unique fields);

            ./1-customizing/cms-views-based-on-selection.txt


    C) xxxxxxxxxxxxxxxxxxxxxxxxxxxx

        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

            C1. xxxxxxxxxxx
            C1. xxxxxxxxxxx
            C1. xxxxxxxxxxx
            C1. xxxxxxxxxxx
            C1. xxxxxxxxxxx
            C1. xxxxxxxxxxx


    D) xxxxxxxxxxxxxxxxxxxxxxxxxxxx

        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

            D1. xxxxxxxxxxx
            D1. xxxxxxxxxxx
            D1. xxxxxxxxxxx
            D1. xxxxxxxxxxx
            D1. xxxxxxxxxxx