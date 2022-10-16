import random as r
from re import X
word_list = [
        "Intelligence",
        "dogs",
        "far",
        "jack",
        "poops",
        "fenced",
        "cream",
        "aorta",
        "donkeykong",
        "hacker",
        "donut",
        "cheeze",
        "lightness",
        "mediterranean",
        "jumbo",
        "ryan",
        "consume"
        ]



word_count = len(word_list) - 1
wc = word_count


word1 = word_list[r.randint(0,wc)]
word2 = word_list[r.randint(0,wc)]
word3 = word_list[r.randint(0,wc)]
word4 = word_list[r.randint(0,wc)]
word5 = word_list[r.randint(0,wc)]
word6 = word_list[r.randint(0,wc)]


startingPoint = (r.randint(0,12), r.randint(0,12))
#def UpOrientation(word):
    #if len(word) >=

wordDirection = ['down', 'up', 'right', 'left', 'diagDownRight', 'diagUpLeft', 'diagDownLeft', 'DiagUpRight']

def downSP(word):
    y = r.randint(0, 13)
    x = r.randint(0,13 - len(word))
    d = "down"
    cord = [[x,y,d], word]
    return (cord)

def upSP(word):
    y = r.randint(0, 13)
    x = r.randint(len(word), 13)
    d = "up"
    cord = [[x,y,d], word]
    return (cord)

def rightSP(word):
    y = r.randint(0, 13)
    x = r.randint(0,13 - len(word))
    d = "right"
    cord = [[x,y,d], word]
    return (cord)

def leftSP(word):
    y = r.randint(0, 13)
    x = r.randint(len(word), 13)
    d = "left"
    cord = [[x,y,d], word]
    return(cord)

def diagonalDownRight(word):
    y = r.randint(0,13 - len(word))
    x = r.randint(0,13 - len(word))
    d = "diagDownRight"
    cord = [[x,y,d], word]
    return (cord)

def diagonalUpLeft(word):
    y = r.randint(len(word), 13)
    x = r.randint(len(word), 13)
    d = "diagUpLeft"
    cord = [[x,y,d], word]
    return (cord)

def diagonalDownLeft(word):
    y = r.randint(len(word), 13)
    x = r.randint(0,13 - len(word))
    d = "diagDownLeft"
    cord = [[x,y,d], word]
    return (cord)

def diagonalUpRight(word):
    y = r.randint(0,13 - len(word))
    x = r.randint(len(word), 13)
    d = "DiagUpRight"
    cord = [[x,y,d], word]
    return (cord)


def wordStartingpoint(word):
    g = r.randint(0,7)
    if g == 0:
        return(downSP(word))
    elif g == 1:
        return(upSP(word))
    elif g == 2:
        return(rightSP(word))
    elif g == 3:
        return(leftSP(word))
    elif g == 4:
        return(diagonalDownRight(word))
    elif g == 5:
        return(diagonalUpLeft(word))
    elif g == 6:
        return(diagonalDownLeft(word))
    elif g == 7:
        return(diagonalUpRight(word))
    
    
    
word1SP = wordStartingpoint(word1)  
word2SP = wordStartingpoint(word2)
word3SP = wordStartingpoint(word3)
word4SP = wordStartingpoint(word4)
word5SP = wordStartingpoint(word5) 

print(word1SP)
print(word2SP)
print(word3SP)
print(word4SP)
print(word5SP)
