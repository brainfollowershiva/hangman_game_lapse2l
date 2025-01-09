import random

class Hangman:
    def __init__(self):
        self.words = ['PYTHON', 'FLASK', 'JAVASCRIPT', 'HTML', 'CSS']
        self.word = random.choice(self.words)
        self.guesses = []
        self.max_attempts = 6
        self.attempts_left = self.max_attempts

    def display_word(self):
        return ''.join([char if char in self.guesses else '_' for char in self.word])

    def make_guess(self, letter):
        if letter not in self.guesses:
            self.guesses.append(letter)
            if letter not in self.word:
                self.attempts_left -= 1

    def is_won(self):
        return all(char in self.guesses for char in self.word)

    def is_lost(self):
        return self.attempts_left <= 0

    def get_status(self):
        return f'Attempts Left: {self.attempts_left}'

    def get_word(self):
        return self.word
