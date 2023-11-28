#%%
from BFS import BFS
from DFS import DFS
from A_Star import aStar
from Dijkstra import dijkstra
from pyamaze import maze, agent, textLabel, COLOR

def main():
    print("welcome to maze solver!")
    height=int(input("Input the height of the maze: "))
    width=int(input("Input the width of the maze: "))
    m=maze(height,width)

    loops=int(input("Input the percentage of loops (0 - 100): "))

    m.CreateMaze(1,1,loopPercent=loops)

    print("\nYour height and width value will be the starting cell")
    print("\nAnd the goal will be (1,1) by default")

    print("\nChoose your algorithm:")
    print("1. BFS (Breadth-First Search)")
    print("2. DFS (Depth-First Search)")
    print("3. A*")
    print("4. Dijkstra")

    choice=int(input("Input the number according to the algorithm you want to use: "))

    # As default: (1,1) is goal cell, (10,10) is start cell
    if choice == 1:
        bSearch,bfsPath,fwdPath=BFS(m,(height,width))

        a=agent(m,height,width,goal=(1,1),footprints=True,shape='square',color=COLOR.green)
        b=agent(m,1,1,goal=(height,width),footprints=True,filled=True)
        c=agent(m,footprints=True,color=COLOR.yellow)

        m.tracePath({a:bSearch},showMarked=True,delay=100)
        m.tracePath({b:bfsPath},delay=50)
        m.tracePath({c:fwdPath},delay=50)

        m.run()
    elif choice == 2:
        dSeacrh,dfsPath,fwdPath=DFS(m,(height,width))

        a=agent(m,height,width,goal=(1,1),footprints=True,shape='square',color=COLOR.green)
        b=agent(m,1,1,goal=(height,width),footprints=True,filled=True)
        c=agent(m,footprints=True,color=COLOR.yellow)

        m.tracePath({a:dSeacrh},showMarked=True,delay=100)
        m.tracePath({b:dfsPath},delay=50)
        m.tracePath({c:fwdPath},delay=50)

        m.run()
    elif choice == 3:
        searchPath,aPath,fwdPath=aStar(m)

        a=agent(m,height,width,goal=(1,1),footprints=True,shape='square',color=COLOR.green)
        b=agent(m,1,1,goal=(height,width),footprints=True,filled=True)
        c=agent(m,footprints=True,color=COLOR.yellow)

        m.tracePath({a:searchPath},showMarked=True,delay=100)
        m.tracePath({b:aPath},delay=50)
        m.tracePath({c:fwdPath},delay=50)

        l=textLabel(m,'A Star Path Length',len(fwdPath)+1)
        l=textLabel(m,'A Star Search Length',len(searchPath))
        m.run() 
    elif choice == 4:
        h1=agent(m,4,4,color=COLOR.red)
        h2=agent(m,4,6,color=COLOR.red)
        h3=agent(m,4,1,color=COLOR.red)
        h4=agent(m,4,2,color=COLOR.red)
        h5=agent(m,4,3,color=COLOR.red)

        h1.cost=100
        h2.cost=100
        h3.cost=100
        h4.cost=100
        h5.cost=100

        path,c=dijkstra(m,h1,h2,h3,h4,h5,start=(height,width))
        textLabel(m,'Total Cost',c)

        a=agent(m,height,width,color=COLOR.cyan,filled=True,footprints=True)
        m.tracePath({a:path},delay=50)

        m.run()
    else:
        print("Not a valid choice")


if __name__ == "__main__":
    main()
# %%