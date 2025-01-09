from flask import Flask, render_template, request, redirect, url_for
import random
from game import Hangman  # Assuming you have a Hangman class in game.py

app = Flask(__name__)

# Initialize the Hangman game
game = Hangman()

@app.route('/')
def index():
    return render_template('index.html', game=game)

@app.route('/guess', methods=['POST'])
def guess():
    letter = request.form['letter'].upper()
    game.make_guess(letter)
    if game.is_won() or game.is_lost():
        return redirect(url_for('result'))
    return redirect(url_for('index'))

@app.route('/result')
def result():
    return render_template('result.html', game=game)

if __name__ == '__main__':
    app.run(debug=True)
