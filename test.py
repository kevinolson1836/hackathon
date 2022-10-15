import random as r
word_list = [
        "Intelligence",
        "dogs",
        "far",
        "jack",
        "poops",
        "fenced"
        ]



word_count = 5
wc = word_count


word1 = word_list[r.randint(0,wc)]
word2 = word_list[r.randint(0,wc)]
word3 = word_list[r.randint(0,wc)]
word4 = word_list[r.randint(0,wc)]
word5 = word_list[r.randint(0,wc)]
word6 = word_list[r.randint(0,wc)]

print(word1)
print(len(word1))

startingPoint = (r.randint(0,12), r.randint(0,12))
#def UpOrientation(word):
    #if len(word) >=

wordDirection = ['down', 'up', 'right', 'left', 'diagDownRight', 'diagUpLeft', 'diagDownLeft', 'DiagUpRight']

def downSP(word):
    x = r.randint(0, 13)
    y = r.randint(0,13 - len(word))
    d = 0
    cord = [x,y,d]
    return (cord)

def upSP(word):
    x = r.randint(0, 13)
    y = r.randint(len(word), 13)
    d = 1
    cord = [x,y,d]
    return (cord)

def rightSP(word):
    y = r.randint(0, 13)
    x = r.randint(0,13 - len(word))
    d = 2
    cord = [x,y,d]
    return (cord)

def leftSP(word):
    y = r.randint(0, 13)
    x = r.randint(len(word), 13)
    d = 3
    cord = [x,y,d]
    return(cord)

def diagonalDownRight(word):
    y = r.randint(0,13 - len(word))
    x = r.randint(0,13 - len(word))
    d = 4
    cord = [x,y,d]
    return (cord)

def diagonalUpLeft(word):
    y = r.randint(len(word), 13)
    x = r.randint(len(word), 13)
    d = 5
    cord = [x,y,d]
    return (cord)

def diagonalDownLeft(word):
    x = r.randint(len(word), 13)
    y = r.randint(0,13 - len(word))
    d = 6
    cord = [x,y,d]
    return (cord)

def diagonalUpRight(word):
    x = r.randint(0,13 - len(word))
    y = r.randint(len(word), 13)
    d = 7
    cord = [x,y,d]
    return (cord)


def wordStartingpoint(word):
    g = r.randint(0,7)
    if g == 0:
        downSP(word)
    elif g == 1:
        upSP(word)
    elif g == 2:
        rightSP(word)
    elif g == 3:
        leftSP(word)
    elif g == 4:
        diagonalDownRight(word)
    elif g == 5:
        diagonalUpLeft(word)
    elif g == 6:
        diagonalDownLeft(word)
    elif g == 7:
        diagonalUpRight(word)
    
    
    
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

print(rightSP(word))