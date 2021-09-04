import requests

from flask import Flask

app = Flask(__name__)


@app.route("/ping", methods=["GET"])
def test():
    return "pong ball"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=False)


# import requests
# url = "http://127.0.0.1:5000/ping"
# response = requests.get(url=url)
# print(response.text)
