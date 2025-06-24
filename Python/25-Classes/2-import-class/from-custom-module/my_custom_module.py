class MyOwnPlanet:
    def __init__(self, name):  # 'name' here is an argument/parameter.
        self.name = name  # this is an attribute.

    def rename(self, new_name):
        self.name = new_name  # I'm redefining the class attribute called 'name'. It's because I'm using 'self.'.
