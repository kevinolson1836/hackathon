# app.py
from flask import Flask, render_template, Response, request  # importing the render_template function


# TODO
#       we have a 13X13 init to 0's
#       find a location for the word to fit
#       check if it doesnt overlap with other words
#       fill in the locations with letters
#       repeat 6 times 
#       after all words inserted, fill in 0's with random chars
#       use flask to send data to the html 

app = Flask(__name__)

grid_size = 13

# home route
@app.route("/",  methods=['POST', 'GET'])
def hello():
    # init the grid to grid_size
    grid = init_grid(size=grid_size)
    print("grid has been init")


# must be words under size 13
    word_list = [
        "Intelligence"
        "dogs"
        "far"
        "jack"
        "poops"
        "fenced"
        ]

    return render_template('index.html', data=grid)

def init_grid(size):
    grid = []
    for _ in range(size):
        grid.append([0]*size)
    return(grid)

app.run(debug = True) 
#iloveukevinnbrad