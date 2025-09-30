

DJANGO MODEL CLASS > ATTRIBUTE TYPE: UUID FIELD

    Common Usage:
        Storing Universally Unique Identifiers (UUIDs). Often used as a primary key (primary_key=True) for distributed systems or to obscure object IDs in URLs instead of using sequential integers, like a primary key for an API that might sync data across multiple databases, an identifier for a file upload that needs a unique, non-sequential name, a public-facing ID in a URL (e.g., /order/550e8400-e29b-41d4-a716-446655440000/) that is harder to guess than a simple integer.

    Field look-like on front-end:
        Only the value.

    Example:
        
        import uuid

        class Book(models.Model):
        # Define a UUID field as the primary key
        id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4, # The function to generate a UUID
            editable=False,     # Makes the field not editable in forms/admin
            unique=True
        )

        # When you create a new Book object, you don't need to specify the ID.
        # It will be automatically generated, e.g.:
        # book1.id -> UUID('c9f5c5b0-7b7a-4b4a-9b9c-0a1b2c3d4e5f')

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

>> Other related options:
    
    >> xxxxxxxxxxxxx Field:
        /xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

