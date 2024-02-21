from flask import Flask, render_template

from battleships import main

app = Flask(__name__)

@app.route('/')
def index():
    main()  # Run the battleships game
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
