# Step 1: pip install flask and import the following modules
from flask import Flask, render_template, url_for, jsonify, request
# Step 6: Import logic.py into app.py
from logic import Easy, Medium, Hard

# Step 2: Create app with flask(__name__)
app = Flask(__name__)

# Step 3: Add a new folder called templates and 
# add a new html file called index.html into the folder
# Step 4: Create route for index.html
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move',methods=['POST'])
def move():
    state = request.get_json()
    
    difficulty = state.get('difficulty')
    
    # Choose game mode based on difficulty
    if (difficulty == 0):
        game = Easy()
    elif (difficulty == 1):
        game = Medium()
    elif (difficulty == 2):
        game = Hard()
        
    game.board = state.get('board')
    game.player = state.get('player')
    game.computer = state.get('computer')
    
    # Calculate computer move
    move = game.calculate_move()
    
    # Response sent with calculated move
    return jsonify(computerMove = move)
    
    
# Step 5: Add app.run with debug = true to run app.py
if __name__ == "__main__":
    app.run(debug=True)