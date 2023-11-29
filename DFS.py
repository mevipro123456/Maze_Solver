from pyamaze import maze, agent, textLabel, COLOR

def DFS(m,start=(None)):
    if start is None:
        start=(m.start_x,m._start_y)
    explored=[start]
    frontier=[start]
    dfsPath={}
    dSearch=[]          # List all Cells it searched to reach goal

    while len(frontier)>0:
        currCell=frontier.pop()
        dSearch.append(currCell)
        if currCell==m._goal:
            break
        poss=0
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
                poss+=1
                explored.append(childCell)
                frontier.append(childCell)
                dfsPath[childCell]=currCell

    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell     # Pick value in dfsPath as key of fwdPath, value key of fwdPath as key of dfsPath
        cell=dfsPath[cell]              # Next cell will be start cell  
    return dSearch,dfsPath,fwdPath   
                
# if __name__=='__main__':
#     m=maze(10,10)
#     m.CreateMaze(1,1,loopPercent=100)       # (1,1) is goal cell, (10,10) is start cell
    
#     l=textLabel(m,'DFS Search',1)

#     dSeacrh,dfsPath,fwdPath=DFS(m,(10,10))

#     a=agent(m,10,10,goal=(1,1),footprints=True,shape='square',color=COLOR.green)
#     b=agent(m,1,1,goal=(10,10),footprints=True,filled=True)
#     c=agent(m,footprints=True,color=COLOR.yellow)

#     m.tracePath({a:dSeacrh},showMarked=True,delay=100)
#     m.tracePath({b:dfsPath},delay=100)
#     m.tracePath({c:fwdPath},delay=100)

#     m.run()
