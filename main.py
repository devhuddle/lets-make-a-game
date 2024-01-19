# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for
import random

# Create a Flask application
app = Flask(__name__)

# Define the Wordle word list
word_list = ["hello", "world", "apple", "banana", "cherry"]

# Define the maximum number of guesses
max_guesses = 6

# Define the current guess
current_guess = 0

# Define the current word
current_word = random.choice(word_list)

# Define the list of guesses
guesses = []

# Define the list of results
results = []

# Define the route for the home page
@app.route("/")
def home():
    """
    Render the home page.

    Returns:
        The home page.
    """
    return render_template("home.html")

# Define the route for handling a guess
@app.route("/guess", methods=["POST"])
def guess():
    """
    Handle a guess.

    Returns:
        The home page with the updated guess and result.
    """
    # Get the guess from the request
    guess = request.form["guess"]

    # Add the guess to the list of guesses
    guesses.append(guess)

    # Check if the guess is correct
    if guess == current_word:
        # The guess is correct, so redirect to the success page
        return redirect(url_for("success"))

    # The guess is incorrect, so add the result to the list of results
    result = ""
    for i in range(len(guess)):
        if guess[i] in current_word and guess[i] == current_word[i]:
            result += "🟩"
        elif guess[i] in current_word:
            result += "🟨"
        else:
            result += "⬛"
    results.append(result)

    # Increment the current guess
    current_guess += 1

    # Check if the maximum number of guesses has been reached
    if current_guess == max_guesses:
        # The maximum number of guesses has been reached, so redirect to the failure page
        return redirect(url_for("failure"))

    # The maximum number of guesses has not been reached, so return to the home page
    return redirect(url_for("home"))

# Define the route for the success page
@app.route("/success")
def success():
    """
    Render the success page.

    Returns:
        The success page.
    """
    return render_template("success.html", word=current_word, guesses=guesses, results=results)

# Define the route for the failure page
@app.route("/failure")
def failure():
    """
    Render the failure page.

    Returns:
        The failure page.
    """
    return render_template("failure.html", word=current_word, guesses=guesses, results=results)

# Run the application
if __name__ == "__main__":
    app.run()
