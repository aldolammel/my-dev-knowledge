from game_brain import GameBrain
from tkinter import Tk, Canvas, Label, Message, Entry, Button, StringVar, OptionMenu
from time import time


class GameUI:

    def __init__(self, game_brain: GameBrain):
        self.game = game_brain
        # Window:
        self.root = Tk()
        self.root.title("Type Faster by @aldolammel")
        self.root.minsize(width=0, height=0)
        self.root.config(padx=20, pady=20, bg="#F1F1F1")
        # Canvas:
        self.canvas = Canvas(width=400, height=300)
        self.canvas.config(highlightthickness=0, bg="#F1F1F1")
        self.canvas.grid(column=1, row=1, pady=10)
        # Labels:
        self.lb_title = Label(
            text="",
            font=("Arial", 14, 'bold'),
            fg="#000000",
            # bg="#FFFFFF"
        )
        self.lb_title.grid(column=1, row=0)
        # Fields:
        self.field_words = Message(
            width=300,
            text=self.game.w_selected,
            font=("Arial", 12, 'bold'),
            fg="#000000",
            # bg="#FFFFFF"
        )
        self.field_words.grid(column=1, row=1)
        self.user_input = Entry(
            width=20,
            font=("Arial", 12),
            fg="#000000",
            bg="#FFFFFF",
            state="disabled"
        )
        self.user_input.grid(column=1, row=2)
        self.user_input.bind("<Key>", self.start, add="+")  # "<Key>" means any key.
        self.user_input.bind("<space>", self.check_word, add="+")  # this "add='+'" means we're using more 1 key.
        self.user_input.bind("<Return>", self.check_word)  # Crucial it uses 'func' instead of 'func()'.
        # Drop menus:
        lang_options = ["English", "Portuguese", "Spanish", "Czech", "German", "French"]
        self.lang_selected = StringVar()  # used to hold the field_db menu value when some selected.
        self.lang_selected.set(lang_options[lang_options.index(self.game.lang)])  # default language.
        self.lang_selected.trace("w", self.drop_lang_selected)
        self.drop_lang = OptionMenu(self.root, self.lang_selected, *lang_options)
        self.drop_lang.grid(column=1, row=0)
        self.drop_lang.config(pady=10)
        # Buttons:
        self.bt_restart = Button(
            text="Restart",
            command=self.restart,
            state="disabled",
            font=("Arial", 12),
            fg="#000000"
            # bg=""
        )
        self.bt_restart.grid(column=1, row=5)
        self.bt_new_game = Button(
            text="New game",
            command=self.new_game,
            font=("Arial", 12),
            fg="#000000"
            # bg=""
        )
        self.bt_new_game.grid(column=1, row=6)
        # Timer:
        self.display_cleared = "00:00.000"
        self.lb_t_display = Label(
            text=self.display_cleared,
            font=("Arial", 28)
            # fg="",
            # bg="",
        )
        self.lb_t_display.grid(column=1, row=3)
        self.start_t = None
        # keep the Tkinter window on screen:
        self.root.mainloop()

    def drop_lang_selected(self, *args):
        self.game.lang = self.lang_selected.get()

    def new_game(self):
        # Manager flags:
        self.game.was_played = True
        self.game.was_restarted = False
        self.game.was_timeout = False
        # Stop the current match if running, and clear the timer:
        self.stop_and_clear()
        # Selecting the language:
        self.game.select_language()
        # Selecting new words for this match:
        self.game.select_new_wrds()
        # Update the interface labels and fields:
        self.lb_title.config(text="Type these words:")
        self.field_words.config(text=self.game.w_selected)
        # Removing the language drop menu:
        self.drop_lang.grid_forget()
        # Disable the restart button:
        self.bt_restart.config(state="disabled")
        # Player's allowed to start:
        self.user_input.config(state="normal")
        # Debug feedback:
        print(f"\n>> A New Game get ready with new {self.game.w_limiter} {self.game.lang} words. Start to type to go!")

    def restart(self):
        # Manager flags:
        self.game.was_restarted = True
        self.game.was_timeout = False
        # Stop the current counting and clear the timer display:
        self.stop_and_clear()
        # Load again the original selected words:
        self.game.w_selected = self.game.w_selected_bkp.copy()
        self.field_words.config(text=self.game.w_selected)
        # Update the title label:
        self.lb_title.config(text="Try again the same words:")
        # Disable the restart button:
        self.bt_restart.config(state="disabled")
        # Normalized the field if it's disabled:
        self.user_input.config(state="normal")

    def start(self, param=None):  # 'param=None' avoids an error when using command in a Label() before another argument
        if not self.game.is_t_running:
            self.game.is_t_running = True
            self.bt_restart.config(state="normal")
            self.start_t = time()
            self.update_timer()
        elif self.user_input.get() == " ":  # When it uses the space bar to start the word checking,
            # an unwanted space is created. It'll delete that, but other characters:
            self.user_input.delete(0)

    def stop(self):
        self.game.is_t_running = False
        self.user_input.delete(0, len(self.user_input.get()))
        self.user_input.config(state="disabled")

    def stop_and_clear(self):
        # Stop possible current match:
        self.stop()
        # Clear the timer display:
        self.lb_t_display.config(text=self.display_cleared)

    def check_word(self, param=None):
        for word in self.game.w_selected:
            if self.user_input.get() == word:
                # Remove the correct word from the list:
                self.game.w_selected.remove(word)
                print(f"Correct: {word}!")
                # Clean the field:
                self.user_input.delete(0, len(word))
                # Update the board:
                self.field_words.config(text=self.game.w_selected)
        if not self.game.should_play():
            self.stop()
            self.show_result()

    def update_timer(self):
        if not self.game.was_timeout and self.game.is_t_running:
            t_elapsed = int((time() - self.start_t) * 1000)
            t_limiter = self.game.t_limiter * 1000  # X seconds in milliseconds
            # Building current display:
            min_ = (t_elapsed // 60000) % 60
            sec_ = (t_elapsed // 1000) % 60
            mil_ = t_elapsed % 1000
            self.game.last_display_num = f"{min_:02}:{sec_:02}.{mil_:03}"
            self.lb_t_display.config(text=self.game.last_display_num)
            # If timeout:
            if t_elapsed >= t_limiter:
                self.game.was_timeout = True
                self.stop()
                self.show_result()
            # Update again:
            if not self.game.was_timeout and self.game.is_t_running:
                self.root.after(10, self.update_timer)

    def show_result(self):
        if not self.game.was_timeout:
            self.lb_title.config(text="Final result:")
            self.field_words.config(
                text=f"Written words: {self.game.w_limiter - len(self.game.w_selected)}/{self.game.w_limiter}\n"
                     f"Time taken: {self.game.last_display_num}")
            print(
                f"\n>> Written words: {self.game.w_limiter - len(self.game.w_selected)}/{self.game.w_limiter} "
                f"| Time taken: {self.game.last_display_num}")
        else:
            self.lb_title.config(text="Partial result:")
            self.field_words.config(
                text=f"Written words: {self.game.w_limiter - len(self.game.w_selected)}/{self.game.w_limiter}\n"
                     f"Time taken: TIMEOUT ({self.game.t_limiter} secs)")
            print(
                f"\n>> Written words: {self.game.w_limiter - len(self.game.w_selected)}/{self.game.w_limiter} "
                f"| Time taken: TIMEOUT ({self.game.t_limiter} secs)")
