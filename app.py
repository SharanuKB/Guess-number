from flask import Flask, render_template, request
import random
import webbrowser

app = Flask(__name__)

# Random Number
number = random.randint(1, 100)
# Attempts
attempts = 0
max_attempts = 3

@app.route("/", methods=["GET", "POST"])
def home():

    global attempts
    global number

    message = ""

    if request.method == "POST":

        guess = int(request.form["guess"])

        attempts += 1

        # Correct Guess
        if guess == number:
            message = f" Correct! You Won! Number was {number}"

            # Reset Game
            attempts = 0
            number = random.randint(1, 100)

        # Attempts Finished
        elif attempts >= max_attempts:
            message = f" Game Over! Your guessing number was \n{number}.try again!"
            

            # Reset Game
            attempts = 0
            number = random.randint(1, 100)

        # Too Low
        elif guess < number:
            left = max_attempts - attempts
            message = f" Too Low! Attempts Left: {left}"

        # Too High
        else:
            left = max_attempts - attempts
            message = f" Too High! Attempts Left: {left}"

    return render_template("index.html", message=message)

if __name__ == "__main__":

    webbrowser.open("http://127.0.0.1:5000")

    app.run(debug=True)