from flask import Flask, render_template
import requests
import os

# create an instance of the class
# first arg = name of the app's module/package. Since we're only using one module, use '__name__'
# this is needed so that Flask knows where to look for templates, static files, and so on.
app = Flask(__name__)


@app.route('/')  # tells Flask what URL should trigger our function
def index():
    return render_template('index.html', word=get_random_word())


def get_random_word():
    return requests.get('https://wikiluke.herokuapp.com/words/random').json()


if __name__ == "__main__":
    app.run(debug=os.environ.get('DEBUG', False),
            host=os.environ.get('HOST', '0.0.0.0'),
            port=os.environ.get('PORT', 8080))

# to enable Debug Mode (among other dev features - ex. auto-reload), run the following:
    # $ export FLASK_ENV=development
    # $ flask run

# OR
# python app.py
