#### Database > PostgreSQL
# Creating a db locally

---

## Before:

1. Assuming you got already the *PostgreSQL* installed locally: [1-installing-and-integrating](/database/PostgreSQL/0-basic/1-installing-and-integrating.md)
2. Make sure the db is running: [starting-and-stopping](/database/PostgreSQL/0-basic/starting-and-stopping.md)

---
## Which db creation method to use:

- 1A) By pgAdmin;
- 1B) By terminal;

### 1A) Using PgAdmin

1A.PRE) Make sure you've done the "INTEGRATION" step at once in the current machine:
[1-installing-and-integrating](/database/PostgreSQL/0-basic/1-installing-and-integrating.md)

            1A.1) In the server tree (sidebar-left), also open the 'Databases';

==ATTENTION:==
Never use the database called "postgres". This is the default db and it cannot be delete!

            1A.2) Create the new database:

                1A.2.PRE) By convention, check how to named your db:
[naming-conventions](/database/PostgreSQL/naming-conventions.md)

                1A.2.1) How do you wanna create your db:

                    G) By PostgreSQL prompt;
                    H) By PgAdmin;

                    - - - -

                    G) By PostgreSQL prompt - - - - - - - - - - - - - - - - - - - - - - - - - -

                        xxxxxxxxxxxxxxxxxxxxxxxxx

                    H) By PgAdmin - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

                        H.1) Right-click on "Databases" and select "Create" > "Database...";

                        H.2) In the "Database" field, enter the name;

                        H.3) And then save it! If no error, it's done! Otherwise:

                            ATTENTION:
                                If an error message says "Collation version mismatch" it's because your OS has been updated but PostgreSQL db cluster hasn't! Solution:

                                H.3.1) Close the PgAdmin, and stop the Postgres service:
[starting-and-stopping](/database/PostgreSQL/0-basic/starting-and-stopping.md)

                                H.3.2) Update and upgrade your PostgreSQL and OS;

                                    UBUNTU:
                                        >> Add the PostgreSQL repo locally:
[updating](/database/PostgreSQL/0-basic/updating.md)

                                        >> Update the entire system:
[/os/linux/distros/debian/2-updates/update](/os/linux/distros/debian/2-updates/update.md)

                                    WINDOWS:
                                        >> xxxxxxxxxxxxxxx

                                        >> xxxxxxxxxxxxxxx

                                H.3.3) Start the Postgres again:
[starting-and-stopping](/database/PostgreSQL/0-basic/starting-and-stopping.md)

                                H.3.4) Update the collation version:
[collation-updating](/database/PostgreSQL/collation-updating.md)

                                H.3.5) Open again the PgAdmin, and now you should be able to create a new db!

### 1B) Using Terminal

            1B.PRE) Update the collation version:
[collation-updating](database/PostgreSQL/collation-updating.md)


            1B.1) Define with encoding for your project db:

                1B.1.PRE) By convention, check how to named your db:
[naming-conventions](/database/PostgreSQL/naming-conventions.md)

                1B.1.1) Which encoding to use:

                    PRE) Keep it in mind:
                        project_db_name = it's the db name!
                        django_db_user = probably is the root user = postgres

                    >> Using English language based:
```
CREATE DATABASE project_db_name OWNER django_db_user ENCODING UTF8 LC_COLLATE 'en_US.UTF-8' LC_CTYPE 'en_US.UTF-8' TEMPLATE template0;
```

                    >> Or using Brazilian Portuguese language based:
```
CREATE DATABASE project_db_name OWNER django_db_user ENCODING UTF8 LC_COLLATE 'pt_BR.UTF-8' LC_CTYPE 'pt_BR.UTF-8' TEMPLATE template0;
```


                CASE OF ERROR:
                    Facing collation error?
[collation-updating](/database/PostgreSQL/collation-updating.md)


            1B.2) Exit Postgres shell:
```
\q
```



---
