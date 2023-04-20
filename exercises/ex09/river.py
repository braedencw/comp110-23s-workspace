"""File to define River class"""

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear

class River:

    """Model a river environment."""

    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove animal based on age."""
        alive_fish: list[Fish] = []
        alive_bears: list[Bear] = []
        for fish in self.fish:
            if fish.age < 4:
                alive_fish.append(fish)
        for bear in self.bears:
            if bear.age < 6:
                alive_bears.append(bear)
        self.fish == alive_fish
        self.bears == alive_bears
        return None

    def remove_fish(self, amount: int):
        """Remove FRONTMOST fish."""
        idx: int = 0
        while idx <= amount - 1:
            self.fish.pop(0)
            idx += 1
        return None

    def bears_eating(self):
        """Show Bears' Eating Method."""
        idx: int = 0
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat()
                self.remove_fish(3)
                idx += 1 
        return None
    
    def check_hunger(self):
        """Check how hungry bears are."""
        alive_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                alive_bears.append(bear)
        self.bears == alive_bears
        return None
        
    def repopulate_fish(self):
        """Model Fish Reproduction"""
        for x in range(0, len(self.fish)//2 * 4):
            self.fish.append(Fish())

        return None
    
    def repopulate_bears(self):
        """Model Bear Reproduction"""
        for x in range(0, len(self.bears)//2):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Check populations in the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish Population: {len(self.fish)}")
        print(f"Bear Population: {len(self.bears)}")

        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Check the populations in the river every day for a week."""
        idx: int = 0
        while idx < 7:
            self.one_river_day()
            idx += 1
            
