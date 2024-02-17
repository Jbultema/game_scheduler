class Player:
    """
    Represents a player, including their name and game preferences.
    
    Attributes:
        name (str): The player's name.
        preferences (list[str]): Ordered list of game names by preference.
    """
    def __init__(self, name, preferences):
        self.name = name
        self.preferences = preferences
