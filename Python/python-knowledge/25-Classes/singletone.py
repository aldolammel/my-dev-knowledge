'''
    SINGLETON
        Concept: /Programming-Concepts/singleton.txt
'''

# Example of a class designed to restrict more than just one instance creation, and providing a
# global point of access to that unique instance.
class SingletonExample:
    _instance = None
    
    def __new__(cls):
        # If no instance, initialize one and return it:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.initialize()  # Initialize method execution!
        # Otherwise, just return the existent instance:
        return cls._instance
    
    def initialize(self):
        # Initialization code here:
        self.value = 42