# app.py
import random as r
from turtle import down
import direcrion
from flask import Flask, render_template, Response, request  # importing the render_template function

x = direcrion.wordStartingpoint("bana")

print(x)
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
    new_grid = insert_into_grid([9,9,7], grid, "word")
    print_grid(new_grid)
    # final_grid = fill_random(new_grid)
    # print_grid(final_grid)

# must be words under size 13
    word_list = [
        "Intelligence",
        "dogs",
        "far",
        "jack",
        "poops",
        "fenced"
        ]

    count = 0
    mega_str = ""
    for x in range(grid_size):
        for y in range(grid_size):
            mega_str = mega_str+ str(grid[x][y])
            count = count + 1

    return render_template('index.html', grid=mega_str)

def init_grid(size):
    grid = []
    for _ in range(size):
        grid.append([0]*size)
    return(grid)

def fill_random(grid):
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    for x in range(len(grid)):
        for y in range(13):
            if (grid[x][y] == 0):
                grid[x][y] = r.choice(all_letters)
            else:
                pass
    return(grid)

def print_grid(grid):
    print()
    for x in range(len(grid)):
        print(grid[x])
    print()

def insert_into_grid(cords, grid, word):
    # format: [x,y,direction]
    
    word_len = len(word)

    # up  
    if (cords[2] == 0):
        for x in range(word_len):
            if (grid[cords[0]-x][cords[1]] == 0):
                grid[cords[0]-x][cords[1]] = word[x]
            else:
                return (0) 
        return(grid)

    # down  
    if (cords[2] == 1):
        for x in range(word_len):
            if (grid[cords[0]+x][cords[1]] == 0):
                grid[cords[0]+x][cords[1]] = word[x]
            else:
                return (0)
        return(grid)

    # left  
    if (cords[2] == 2):
        for x in range(word_len):
            if(grid[cords[0]][cords[1]-x] == 0): 
              grid[cords[0]][cords[1]-x] = word[x]
            else:
                return (0)
        return(grid)

    # right  
    if (cords[2] == 3):
        for x in range(word_len):
            if (grid[cords[0]][cords[1]+x] == 0): 
                grid[cords[0]][cords[1]+x] = word[x]
            else:
                return (0)
        return(grid)

    # \ diaginal up 
    if (cords[2] == 4):
        for x in range(word_len):
            grid[cords[0]-x][cords[1]-x] = word[x]
        return(grid)

    # \ diaginal  down
    if (cords[2] == 5):
        for x in range(word_len):
            grid[cords[0]+x][cords[1]+x] = word[x]
        return(grid)

    # / diaginal  up
    if (cords[2] == 6):
        for x in range(word_len):
            grid[cords[0]-x][cords[1]+x] = word[x]
        return(grid)
    
    # / diaginal  down
    if (cords[2] == 7):
        for x in range(word_len):

            grid[cords[0]+x][cords[1]-x] = word[x]
        return(grid)

app.run(debug = True) 
