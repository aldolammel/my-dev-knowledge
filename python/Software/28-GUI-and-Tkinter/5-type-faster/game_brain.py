import db
from random import sample, shuffle


class GameBrain:
    def __init__(self, words_limiter, time_limiter):
        # Initial values:
        self.lang = "English"  # default value
        self.wrds = list()
        self.w_selected = "Select a language and, after that, click 'New Game' to receive the words."
        self.w_selected_bkp = list()
        self.last_display_num = ""
        # Global definitions:
        self.w_limiter = words_limiter
        self.t_limiter = time_limiter
        # Managers:
        self.was_played = False
        self.is_t_running = False
        self.was_restarted = False
        self.was_timeout = False

    def error_handler_db(self):
        # Length global limiters:
        w_min = 5
        w_max = len(self.wrds)
        # Check the current db length:
        if w_min > self.w_limiter:
            self.w_limiter = w_min
            print(f"\nDEBUG >> You're playing with the minimum words amount: {self.w_limiter}\n")
        elif w_max < self.w_limiter:
            self.w_limiter = w_max
            print(f"\nDEBUG >> You're playing with all available {self.lang} words: {self.w_limiter}\n")
        # Check the time limiter:
        t_min = self.w_limiter * 0.5
        if t_min > self.t_limiter:
            self.t_limiter = t_min
            print(f"\nDEBUG >> Your timeout's too low, so it was reset to the minimum duration based on words number: "
                  f"{self.t_limiter} secs.\n")

    def select_language(self):
        # Through the dictionary (db.lang) with all available languages, select the user choices:
        self.wrds = db.lang[self.lang]

    def select_new_wrds(self):
        self.error_handler_db()
        w_selected = sample(self.wrds, self.w_limiter)
        shuffle(w_selected)
        self.w_selected = w_selected.copy()
        self.w_selected_bkp = w_selected.copy()

    def should_play(self):
        if len(self.w_selected) > 0:
            return True
        return False
