import sys

def findStart(arr,row,col):#returns start points
    print("ROW: ",row)
    print("COL: ",col)
    for i in range(row):
        for j in range(col):
            if(arr[j][i] == "@"):
                print("x: ",i)
                print("y: ",j)
                return i,j
            
def getNeighbors(rows,cols, x,y):
    neighbors = []
    if(0<= x < cols and 0<= y-1 < rows):#North
        neighbors.append((x,y-1,"N"))
    if(0<= x < cols and 0<= y+1 < rows):#South
        neighbors.append((x,y+1,"S"))

    if(0<= x+1 < cols and 0<= y < rows):#East
        neighbors.append((x+1,y,"E"))

    if(0<= x-1 < cols and 0<= y < rows):#West
        neighbors.append((x-1,y,"W"))

    #print("NEIGHBORS: (",x,",",y,"): ",neighbors)
    return neighbors


def dfs(grid, x,y, visited,seen,rows,cols):
    if(len(visited) == rows*cols):
        return
    #if dirty clean it up and print V
    print("(",x,",",y,"): ",grid[x][y])
    if(grid[x][y] == dirtyCell):
        print("V")
    neighbors = getNeighbors(rows,cols,x,y)
    for n in neighbors:#go through the neighbors
        if grid[n[0]][n[1]] != blockedCell and (n[0],n[1]) not in visited:#dfs if we havent visited it and its not blocked
            visited.append((n[0],n[1]))
            print(n[2])#print which way we are going
            dfs(grid, n[0],n[1], visited, seen, rows, cols)
            if n[2] == "N":#print reverse
                print("S")
            elif n[2] == "N":
                print("S")
            elif n[2] == "E":
                print("W")
            elif n[2] == "W":
                print("E")
        elif grid[n[1]][n[0]] == blockedCell:#if its blocked
            visited.append((n[1],n[0]))
        
    
    



    
    

if len(sys.argv) == 3:
    algo = sys.argv[1]
    fileName = sys.argv[2]#check its txt

    # Opening a file in read mode
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
        n =1
        for line in file:
            if (n == 1):
                col = int(line.strip())-1
            elif (n == 2):
                row = int(line.strip())-1
            else:
                lines.append(line.strip())
            n+=1

    startY,startX = findStart(lines,row,col)
    print(lines)
    print("#######################")
    dfs(lines,startX,startY,[],[],row,col)
    




else: 
    raise Exception("Wrong number of input args")



    
                

