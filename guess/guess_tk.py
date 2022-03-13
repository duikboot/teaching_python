#!/usr/bin/env python

from tkinter import (
    Tk,
    Label,
    Button,
    Entry,
    StringVar,
    DISABLED,
    NORMAL,
    END,
    W,
    E)

from guess_term import create_number, validate_quess


class GuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Guessing Game")

        self.secret_number = create_number()
        self.guess = None
        self.num_guesses = 0

        self.message = "Guess a number from 1 to 100"
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, textvariable=self.label_text)

        # we have to wrap the command
        vcmd = master.register(self.validate)
        self.entry = Entry(master, validate="key",
                           validatecommand=(vcmd, '%P'))

        self.guess_button = Button(
            master, text="Guess", command=self.guess_number)
        self.reset_button = Button(
            master, text="Play again", command=self.reset, state=DISABLED)
        self.quit_button = Button(
            master, text="Quit", command=self.quit)

        self.label.grid(row=0, column=0, columnspan=2, sticky=W+E)
        self.entry.grid(row=1, column=0, columnspan=2, sticky=W+E)
        self.guess_button.grid(row=2, column=0)
        self.reset_button.grid(row=2, column=1)
        self.quit_button.grid(row=3, column=0, columnspan=2)

    def validate(self, new_text):
        if not new_text:  # the field is being cleared
            self.guess = None
            return True

        try:
            guess = int(new_text)
            if 1 <= guess <= 100:
                self.guess = guess
                return True
            else:
                return False
        except ValueError:
            return False

    def guess_number(self):
        self.num_guesses += 1

        if self.guess is None:
            self.message = "Guess a number from 1 to 100"

        correct, self.message = validate_quess(
            self.secret_number,
            self.guess
        )
        if correct:
            self.guess_button.configure(state=DISABLED)
            self.reset_button.configure(state=NORMAL)
            self.message = (
                f"{self.message}, you guessed it in {self.num_guesses} guesses"
            )

        self.label_text.set(self.message)

    def quit(self):
        self.master.destroy()

    def reset(self):
        self.entry.delete(0, END)
        self.secret_number = create_number()
        self.guess = 0
        self.num_guesses = 0

        self.message = "Guess a number from 1 to 100"
        self.label_text.set(self.message)

        self.guess_button.configure(state=NORMAL)
        self.reset_button.configure(state=DISABLED)


root = Tk()
my_gui = GuessingGame(root)
root.mainloop()
