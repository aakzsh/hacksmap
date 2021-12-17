from flask import Flask, render_template, request
import urllib.request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/select/<username>')
def select(username):
    try:
        urllib.request.urlopen(f"https://www.devpost.com/{username}")
        return render_template('select.html', username=username)
    except:
        return render_template('404.html')

@app.route('/wrapped/<username>')
def wrapped(username):
    return render_template('wrapped.html')

@app.route('/map/<username>')
def map(username):
    return render_template('map.html')


if __name__ == "__main__":
    app.run(debug=True)