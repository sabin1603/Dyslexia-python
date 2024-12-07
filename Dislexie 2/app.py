from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/learn-vowels')
def learn_vowels():
    return render_template('learn_vowels.html')

@app.route('/play-game')
def play_game():
    return render_template('play_game.html')

@app.route('/play-matching-game')
def play_matching_game():
    return render_template('play_matching_game.html')

@app.route('/read-vowel')
def read_vowel():
    return render_template('read_vowel.html')

@app.route('/drag-and-drop')
def drag_and_drop():
    return render_template('drag_and_drop.html')

@app.route('/get-random-vowel', methods=['GET'])
def get_random_vowel():
    vowels = [('A', 'a'), ('E', 'e'), ('I', 'i'), ('O', 'o'), ('U', 'u')]
    selected_pair = random.choice(vowels)
    correct_vowel = random.choice(selected_pair)
    return jsonify(correct_vowel=correct_vowel)

if __name__ == '__main__':
    app.run(debug=True)
