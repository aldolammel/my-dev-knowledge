

DJANGO ADMIN (CMS)

    The admin.py is an empty file automatically created by Django. It customize the logic to be used on CMS through its list-views and detail-views.

    >> The CMS is divided by this areas:

        1) Home: 

            It's a page where you get a resume of the CMS options:
            
                http://localhost:8000/admin/



        2) List view: 
        
            When you click on a CMS menu option, you'll be taken to a list page where 
            all entries of one type of data in the database is shown. 
            
                >> URL examples:
            
                    # Users list:
                    http://localhost:8000/admin/auth/user/

                    # Pages list:
                    http://localhost:8000/admin/pagex/pagexpage/


        3) Detail view:

            When you click on an options listed in some List view, you'll be taken to a page with
            all data about that specific listed entry you previously have clicked.

            3.1) Detail view > Existing object:
                
                >> E.g. how to check:
                    if obj:
                        pass

                >> URL examples:
                
                    # A specific User (obj) detail:
                    http://localhost:8000/admin/auth/user/3/change/

                    # A specific Page (obj) detail:
                    http://localhost:8000/admin/pagex/pagexpage/16/change/
                    

            3.2) Detail view > New object:

                >> E.g. how to check:
                    if not obj:
                        pass

                >> URL examples:
                
                    # A new user (ojb) detail:
                    http://localhost:8000/admin/auth/user/add/

                    # A new page (ojb) detail:
                    http://localhost:8000/admin/pagex/pagexpage/add/
    

    >> How looks an Admin Class:
        ./_admin-class-model.py



    >> What kind of CMS UX you need:
        ./_what-kind-of-cms-ux-do-you-need.txt