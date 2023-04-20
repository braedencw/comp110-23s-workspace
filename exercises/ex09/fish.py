"""File to define Fish class"""

class Fish:
    
    """Model a fish living in the river"""

    age: int

    def __init__(self):
        """Initialize the fish."""
        self.age = 0
        return None
    
    def one_day(self):
        """Model a day passing."""
        self.age += 1
        return None