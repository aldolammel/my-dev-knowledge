def pagex_forbidden_chars(txt: str, lst: list[str]):
    """Function that check if the string has a forbidden character.
    Return: False if everything's fine. True if the string has a forbidden char."""
    return any(char in lst for char in txt.split())



is_ok = pagex_forbidden_chars("Aldo Lammel", ["!", "$", "%", "&"])