from flask import Flask, render_template

app = Flask(__name__)


# ------------------------------ Inizio Routes --------------------------

# home page
@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/sium')
def sium():
    return render_template('sium.html')


# ------------------------------ Fine Routes --------------------------

if __name__ == '__main__':
    app.run()
