import csv
import os
import glob
from game import Game
from player import Player
from schedule import Schedule

def find_newest_csv(directory="../data"):
    """
    Finds the newest CSV file in the specified directory.
    
    Parameters:
        directory (str): The path to the directory containing CSV files.
        
    Returns:
        str: The path to the newest CSV file in the directory.
    """
    # List all CSV files in the directory
    csv_files = glob.glob(os.path.join(directory, '*.csv'))
    # Sort files by modification time, newest first
    newest_file = max(csv_files, key=os.path.getmtime)
    return newest_file

def load_data_from_csv(filepath):
    """
    Loads games and player data from a CSV file, separating the combined data into
    game objects and player objects.
    
    Parameters:
        filepath (str): The path to the CSV file containing the data.
        
    Returns:
        tuple: A tuple containing a list of Game objects and a list of Player objects.
    """
    games = []
    players_dict = {}  # Dictionary to accumulate player preferences

    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Process game and player data here as previously described
            pass

    # Convert player preferences dictionary into Player objects
    players = [Player(name=key, preferences=value) for key, value in players_dict.items()]
    return games, players

if __name__ == "__main__":
    # Automatically find the newest CSV file in the 'data/' directory
    newest_csv_file = find_newest_csv("data/")
    games, players = load_data_from_csv(newest_csv_file)
    print(games, players)

    scheduler = Schedule(games, players, num_simultaneous_games=2, num_game_slots=3)
    scheduler.schedule_games()
    scheduler.print_schedule()
