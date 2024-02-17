class Game:
    """
    Represents a board game, including its player count limits, designated teacher,
    and potential alternate teachers.
    
    Attributes:
        name (str): The name of the game.
        min_players (int): Minimum required number of players.
        max_players (int): Maximum allowed number of players.
        teacher (str): The primary teacher for the game.
        alternate_teachers (list[str]): List of alternate teachers.
        assigned_players (list[str]): Players assigned to this game, including the teacher.
    """
    def __init__(self, name, min_players, max_players, teacher, alternate_teachers):
        self.name = name
        self.min_players = min_players
        self.max_players = max_players
        self.teacher = teacher
        self.alternate_teachers = alternate_teachers
        self.assigned_players = []

    def assign_teacher(self, available_teachers):
        """
        Assigns a teacher to the game, preferring the primary teacher but using alternates if necessary.
        
        Parameters:
            available_teachers (list[str]): List of teachers available for assignment.
        """
        if self.teacher in available_teachers:
            self.assigned_players.append(self.teacher)
            available_teachers.remove(self.teacher)
        else:
            for alt_teacher in self.alternate_teachers:
                if alt_teacher in available_teachers:
                    self.assigned_players.append(alt_teacher)
                    available_teachers.remove(alt_teacher)
                    break