

NAMING CONVENTIONS: POSTGRESQL


    >> Naming a database:

        <Cliente>_<Product_type>_<Release_year>_db
                
        E.g.
            Abcoo_b2b_2030_db
            Abican_portal_2023_db
            Aldolammel_ecommerce_2020_db
            Ammana_b2b_2019_db


    
    >> Naming tables & columns:
    
        PostgreSQL stores all the table and column names in lowercase. If we run a select query with uppercase against Postgres, the query will fail saying the column or the table doesn’t exist.

        E.g.

            my_table_a
                this_is_my_column_1
                this_is_my_column_2
                this_is_my_column_3
            my_table_b
                this_is_my_column_4
                this_is_my_column_5

