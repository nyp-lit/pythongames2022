from flask import Flask, render_template, request
from uuid import uuid4


app = Flask(__name__)
app.config['SECRET_KEY'] = uuid4().hex    # random 32-character lowercase hexadecimal string


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
