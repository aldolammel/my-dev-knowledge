

PROJECT EXAMPLE: HOW TO SAVE THE USER WHO CREATE AN INSTANCE/ENTRY/INPUT IN THE DATABASE

    >> Saving the ID of the authentified user who added data through front-end;

    >> Saving the ID of the authentified user who added data through CMS;





PROMPT TO USE TO BUILD THIS EXAMPLE:

I'm using Python with Django v5 and PostgreSQL. And, please, consider these points before coding:
- Follow the best practices for Python;
- Follow the DRY principles;
- Comment on the code when important.

That said, create an example of a Public Movie List where any registered user can save as many movie titles as the user remembers in a global list. For a user to record a movie in the public list, these fields will be used: 

- movie_title
- created_by
- updated_by

Template/front-end pages needed:

- index.html (public movie list);
- movie.html (to add and edit a movie title to the public movie list);

Business rules of index.html page:

- When the user accesses the public movie list, they can see only the movies (title) they previously added through the 'movie.html' form;
- Each movie title in the public movie list has a hyperlink to its 'movie.html' form;
- In the bottom of the public movie list, there must exist a hyperlink called "Add new movie" to the 'movie.html' form;
- If the user has no movie title recorded yet, instead of an empty public movie list, show the message "No movie recorded yet!"; 
- Only authenticated users can access this page;

Business rules of movie.html page:

- This page is used to add new movie titles and where the user can edit the data as well;
- The 'movie_title' field is mandatory;
- The 'movie_title' field is also unique in the entire recorded movie titles in the database, no matter who added that;
- The 'created_by' and 'updated_by' fields are automatically filled with the username of who is adding/editing the movie; 
- The 'created_by' and 'updated_by' fields are hidden in this form;
- If the submission is successful, send the user to the index.html, showing the public movie list already updated with the new movie title;
- In the case of the 'movie.html' form being used to add a new movie title, the form buttons must be: Save and Cancel;
- But in the case of the 'movie.html' form being used to edit an existent movie title, the form buttons must be: Save, Delete, and Cancel;
- Only authenticated users can access this page;

Business rules for Django Admin (CMS):

- All admin users can see through the Django Admin (CMS) the public movie list, listing all movies saved in the database, no matter who added them;
- The public movie list (list view) must be shown with these columns: id, movie title, created_by, and updated_by;
- When the admin user adds a new movie, the created_by attribute must be automatically filled with the current admin username;
- The 'created_by' and 'updated_by' fields in the detail-view in Admin (CMS) must be only read, where no one through the Admin (CMS) can edit those data;

I need in this example, at least, the following files:

- movie app models.py
- movie app views.py
- movie app urls.py
- movie app forms.py
- movie app admin.py

Abstractions for this example request:

- I don't need an example of how to create a Django Project; 
- I don't need an example of how to create a Django superuser; 
- I don't need an example of how to create a user register form/page;
- I don't need an example of creating a login or logout forms/pages;