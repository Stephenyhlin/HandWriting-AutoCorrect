from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def check():
    return "We running live bois~\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080, threaded=False)