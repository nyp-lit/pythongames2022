# Step 1: pip install flask and import the following modules
from flask import Flask, render_template, url_for, jsonify, request

# Step 2: Create app with flask(__name__)
app = Flask(__name__)

# Step 3: Add a new folder called templates and add a new html file called index.html into the folder
# Step 4: Create route for index.html
@app.route('/')
def index():
    return render_template('index.html')

# Step 5: Add app.run with debug = true to run app.py
if __name__ == "__main__":
    app.run(debug=True)

