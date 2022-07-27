#puzzle input into usable data 
txt = open('Day1.txt').read()
data = txt.split(", ")


NS = True       #boolean for walking north/south
x = True        #boolean for walking positive x (East)
y = True        #boolean for walking positive y (North)

xDist = 0
yDist = 0

visited = [(0, 0)]
HQ = ()

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
    

    
    if HQ == ():
        start = visited[-1]
        end = (xDist, yDist)
        
        #NEED TO FIX BLOCK BY BLOCK VISITED LOCATIONS BEING APPENDED PROPERLY

        if NS:              #Change in y
            low = min(start[1],end[1])
            high = max(start[1],end[1])
            for dy in range(low, high+1):
                if (xDist, dy) in visited:
                    HQ = (xDist, dy)
                    break
                else:
                    visited.append((xDist, dy))
        else:               #Change in x
            low = min(start[0],end[0])
            high = max(start[0],end[0])
            for dx in range(low, high+1):
                if (dx, yDist) in visited:
                    HQ = (dx, yDist)
                    break
                else:
                    visited.append((dx, yDist))

    
    NS = not NS             #Switches walking N/S to E/W and reverse each turn

    #print(dir[0]+":", (xDist,yDist)) # test output


blocksAway = abs(HQ[0])+abs(HQ[1])

print(blocksAway)
