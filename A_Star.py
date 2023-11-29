from pyamaze import maze, agent, COLOR, textLabel
from queue import PriorityQueue     # Value append and pop based on their priority

def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return (abs(x1 - x2) + abs(y1 - y2))
    
def aStar(m,start=None):
    if start is None:
        start=(m.start_x,m.start_y)
    open = PriorityQueue()
    open.put((h(start, m._goal), h(start, m._goal), start))
    aPath = {}
    g_score = {row: float("inf") for row in m.grid}
    g_score[start] = 0
    f_score = {row: float("inf") for row in m.grid}
    f_score[start] = h(start, m._goal)
    searchPath=[start]
    while not open.empty():
        currCell = open.get()[2]
        searchPath.append(currCell)
        if currCell == m._goal:
            break        
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + h(childCell, m._goal)

                if temp_f_score < f_score[childCell]:   
                    aPath[childCell] = currCell
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_g_score + h(childCell, m._goal)
                    open.put((f_score[childCell], h(childCell, m._goal), childCell))


    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return searchPath,aPath,fwdPath

# if __name__=='__main__':
#     m=maze(10,10)
#     m.CreateMaze(1,1,loopPercent=100)       # (1,1) is goal cell, (10,10) is start cell


#     searchPath,aPath,fwdPath=aStar(m)

#     a=agent(m,10,10,goal=(1,1),footprints=True,shape='square',color=COLOR.green)
#     b=agent(m,1,1,goal=(10,10),footprints=True,filled=True)
#     c=agent(m,footprints=True,color=COLOR.yellow)

#     m.tracePath({a:searchPath},showMarked=True,delay=100)
#     m.tracePath({b:aPath},delay=100)
#     m.tracePath({c:fwdPath},delay=100)

#     l=textLabel(m,'A Star Path Length',len(fwdPath)+1)
#     l=textLabel(m,'A Star Search Length',len(searchPath))
#     m.run()