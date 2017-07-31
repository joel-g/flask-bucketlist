from flask import flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Stormy"

if __name__ == "__main__":
    app.run()
