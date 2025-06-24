from game_brain import GameBrain
from game_ui import GameUI

# Game Setup:
words_limiter = 40  # Number of words for each game and match.
time_limiter = 120  # Timeout for each match (in seconds).

# Building the app:
brain = GameBrain(words_limiter, time_limiter)
GameUI(brain)
