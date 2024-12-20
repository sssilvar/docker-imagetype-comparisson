"""Simple flask app"""

import os
from flask import Flask

PORT = os.getenv("PORT", 8080)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return f"Hello, World from port {PORT}!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
