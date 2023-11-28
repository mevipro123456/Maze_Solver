from pyamaze import maze, agent, textLabel, COLOR
from collections import deque           # double-ended queue, same to linked list but allow append or pop on both heads

def BFS(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    frontier=deque()
    frontier.append(start)
    explored=[start]
    bfsPath={}
    bSearch=[]          # List all Cells it searched to reach goal

    while len(frontier)>0:
        currCell=frontier.popleft()
        if currCell==m._goal:
            break
        for d in 'ESNW':        # Try with WNSE
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)       # childCell is on the right of currCell
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in explored:       # If childCell found in explored, do nothing
                    continue
                explored.append(childCell)
                frontier.append(childCell)
                bfsPath[childCell]=currCell
                bSearch.append(childCell)
    fwdPath={}
    cell=m._goal
    while cell!=(m.rows,m.cols):
        fwdPath[bfsPath[cell]]=cell     # Pick value in bfsPath as key of fwdPath, value key of fwdPath as key of bfsPath
        cell=bfsPath[cell]              # Next cell will be start cell  
    return bSearch,bfsPath,fwdPath   
                
# if __name__=='__main__':
#     m=maze(10,10)
#     m.CreateMaze(1,1,loopPercent=100)       # (1,1) is goal cell, (10,10) is start cell

#     l=textLabel(m,'BFS Search',1)

#     bSearch,bfsPath,fwdPath=BFS(m,(10,10))

#     a=agent(m,10,10,goal=(1,1),footprints=True,shape='square',color=COLOR.green)
#     b=agent(m,1,1,goal=(10,10),footprints=True,filled=True)
#     c=agent(m,footprints=True,color=COLOR.yellow)

#     m.tracePath({a:bSearch},showMarked=True,delay=100)
#     m.tracePath({b:bfsPath},delay=100)
#     m.tracePath({c:fwdPath},delay=100)

#     m.run()
