# app.py
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def initialize_board():
    return [['O' for _ in range(5)] for _ in range(5)]

def place_boats(board):
    boat_positions = []
    for _ in range(3):
        while True:
            row = random.randint(0, 4)
            col = random.randint(0, 4)
            if (row, col) not in boat_positions:
                boat_positions.append((row, col))
                board[row][col] = 'B'
                break

# Other game logic functions here...

@socketio.on('start_game')
def start_game():
    board = initialize_board()
    place_boats(board)
    emit('game_started', board)

if __name__ == '__main__':
    socketio.run(app)
