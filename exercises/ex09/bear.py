"""File to define Bear class"""

class Bear:

    """Model a bear living by a river."""

    age: int
    hunger_score: int
    
    def __init__(self):
        """Initialize the bear."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Model a day passing."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Model a bear eating a fish."""
        self.hunger_score += num_fish
        return None 