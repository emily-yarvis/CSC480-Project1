from collections import deque
import sys

def findStart(arr, row, col):  
    print("ROW: ", row)
    print("COL: ", col)
    for y in range(row):
        for x in range(col):
            print(arr[y][x])
            if arr[y][x] == "@":
                print("x: ", x)
                print("y: ", y)
                return x, y
            
def getNeighbors(rows, cols, x, y):
    neighbors = []
    if 0 <= x < cols and 0 <= y - 1 < rows:  # North
        neighbors.append((x, y - 1, "N"))
        
    if 0 <= x < cols and 0 <= y + 1 < rows:  # South
        neighbors.append((x, y + 1, "S"))
        
    if 0 <= x + 1 < cols and 0 <= y < rows:  # East
        neighbors.append((x + 1, y, "E"))
    if 0 <= x - 1 < cols and 0 <= y < rows:  # West
        neighbors.append((x - 1, y, "W"))

    return neighbors

def buildPath(arr,newDirection):
    if(arr):
        return arr.append(newDirection)
    else:
        return [newDirection]
from collections import deque

def buildPath(path, direction):
    return path + [direction]





def bfs(grid, startX, startY, rows, cols, dirty, nodesGenerated, nodesExpanded):
    
    q = deque()
    visited = set()

    visited.add((startX,startY))
    q.append((startX,startY,[]))

    

    while(q):
        node = q.popleft()
        
        x = node[0]
        y = node[1]
        path = node[2]
        
        nodesExpanded += 1

        

        if grid[y][x] == dirtyCell and (x,y) not in dirty:
            if(path):
                for p in path:
                    print(p)
            print("V")
            dirty.add((x,y))
            return bfs(grid,x,y,rows,cols,dirty, nodesGenerated,nodesExpanded)
            

        neighbors = getNeighbors(rows, cols, x, y)
        for n in neighbors:
            nodesGenerated += 1
            if grid[n[1]][n[0]] != blockedCell and (n[0], n[1]) not in visited:
                visited.add((n[0],n[1]))
                q.append((n[0],n[1],buildPath(path,n[2])))
            
    print("Nodes generated:", nodesGenerated)
    print("Nodes expanded:", nodesExpanded)



    

def dfs(grid, x, y, visited, rows, cols, generated, expanded):
    expanded += 1  

    if grid[y][x] == dirtyCell:
        print("V")

    neighbors = getNeighbors(rows, cols, x, y)
    generated += len(neighbors)  

    for n in neighbors:
        if grid[n[1]][n[0]] != blockedCell and (n[0], n[1]) not in visited:
            visited.append((n[0], n[1]))
            print(n[2])
            generated, expanded = dfs(grid, n[0], n[1], visited, rows, cols, generated, expanded)
            if n[2] == "N":
                print("S")
            elif n[2] == "S":
                print("N")
            elif n[2] == "E":
                print("W")
            elif n[2] == "W":
                print("E")
        elif grid[n[1]][n[0]] == blockedCell:
            visited.append((n[0], n[1]))

    return generated, expanded


if len(sys.argv) == 3:
    algo = sys.argv[1]
    fileName = sys.argv[2]  

    lines = []
    row = 0
    col = 0
    emptyCell = "_"
    blockedCell = "#"
    dirtyCell = "*"
    start = "@"
    startX = 0
    startY = 0

    with open(fileName, 'r') as file:
        n = 1
        for line in file:
            if n == 1:
                col = int(line.strip())
            elif n == 2:
                row = int(line.strip())
            else:
                lines.append(line.strip())
            n += 1

    startX, startY = findStart(lines, row, col)
   
    if(algo == "dfs"):
        dfs = dfs(lines, startX, startY, [(startX, startY)],  row, col,0,0)
        print("Generated Nodes: ", dfs[0])
        print("Expanded Nodes: ", dfs[1])
    elif(algo == "bfs"):
        bfs(lines, startX, startY,  row, col,set(),0,0)
    else:
        raise Exception("Invalid Traversal Algo try again later")

else:
    raise Exception("Wrong number of input args")