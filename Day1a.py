#puzzle input into usable data 
txt = open('Day1.txt').read()
data = txt.split(", ")


NS = True       #boolean for walking north/south
x = True        #boolean for walking positive x (East)
y = True        #boolean for walking positive y (North)

xDist = 0
yDist = 0


for dir in data:
    turnL = dir[0] == "L"
    blocks = int(dir[1:])

    if NS:
        if y == turnL:      #walking North and turn left or walking South and turn right (going West)
            x = False
            xDist -= blocks
        else:               #going East
            x = True
            xDist += blocks

    else:
        if x == turnL:      #walking East and turn left or walking West and turn right (going North)
            y = True
            yDist += blocks
        else:               #going South
            y = False
            yDist -= blocks
    
    NS = not NS             #Switches walking N/S to E/W and reverse each turn

    #print(dir[0]+":", (xDist,yDist)) # test output


blocksAway = abs(xDist)+abs(yDist)

print(blocksAway)
