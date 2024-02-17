class Schedule:
    """
    Manages the scheduling of games, including assigning players and teachers to games
    across multiple slots.
    
    Attributes:
        games (list[Game]): List of games available for scheduling.
        players (list[Player]): List of players participating in the games.
        num_simultaneous_games (int): Number of games that can be played simultaneously in each slot.
        num_game_slots (int): Total number of game slots available.
        schedule (list): The schedule, organized by slots, each containing scheduled games and their players.
    """
    def __init__(self, games, players, num_simultaneous_games, num_game_slots):
        self.games = games
        self.players = players
        self.num_simultaneous_games = num_simultaneous_games
        self.num_game_slots = num_game_slots
        self.schedule = [[] for _ in range(num_game_slots)]

    def schedule_games(self):
        """
        Schedules games across available slots, assigning teachers and players to each game.
        """
        for slot in range(self.num_game_slots):
            available_teachers = [player.name for player in self.players]
            selected_games = self.select_games_for_slot(slot, available_teachers)
            self.assign_players_to_games(selected_games, slot)

    def select_games_for_slot(self, slot, available_teachers):
        """
        Selects and schedules games for a specific slot based on teacher availability.
        
        Parameters:
            slot (int): The current slot being scheduled.
            available_teachers (list[str]): Teachers available for this slot.
        
        Returns:
            list[Game]: Selected games for the slot.
        """
        selected_games = []
        for game in self.games:
            if len(selected_games) < self.num_simultaneous_games:
                game.assign_teacher(available_teachers)
                if game.assigned_players:  # If a teacher was successfully assigned
                    selected_games.append(game)
        return selected_games

    def assign_players_to_games(self, selected_games, slot):
        """
        Assigns players to the selected games for a specific slot.
        
        Parameters:
            selected_games (list[Game]): Games selected for the slot.
            slot (int): The current slot being scheduled.
        """
        for game in selected_games:
            interested_players = [p for p in self.players if game.name in p.preferences]
            for player in interested_players:
                if len(game.assigned_players) < game.max_players and player.name not in game.assigned_players:
                    game.assigned_players.append(player.name)
            self.schedule[slot].append((game.name, game.assigned_players))

    def print_schedule(self):
        """
        Prints the detailed schedule of games, including slot information, games scheduled, 
        assigned teachers (indicating if an alternate teacher is used), and the list of players 
        for each game.
        """
        for slot_index, slot in enumerate(self.schedule, start=1):
            print(f"Slot {slot_index}:")
            for game, players in slot:
                game_instance = self.find_game_by_name(game)
                teacher = game_instance.assigned_players[0]  # The first assigned player is the teacher
                # Check if the assigned teacher is an alternate
                teacher_label = "Alternate Teacher" if teacher in game_instance.alternate_teachers else "Teacher"
                players_without_teacher = [p for p in players if p != teacher]
                print(f"  Game: {game}")
                print(f"    {teacher_label}: {teacher}")
                print(f"    Players: {', '.join(players_without_teacher)}\n")

    def find_game_by_name(self, game_name):
        """
        Finds a game instance by its name.
        
        Parameters:
            game_name (str): The name of the game to find.
        
        Returns:
            Game: The game instance with the matching name, or None if not found.
        """
        for game in self.games:
            if game.name == game_name:
                return game
        return None
