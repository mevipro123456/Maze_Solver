# To familiarize with pyamaze parameters

from pyamaze import maze, COLOR, agent, textLabel
m=maze()                # Default is 10x10, can change
m.CreateMaze(loopPercent=100)          # Customizable

a=agent(m, footprints=True, filled=True)
b=agent(m, 5, 5, footprints=True,color='red')
c=agent(m, 4, 1, footprints=True,color='green',shape='arrow')

path2=[(5,4),(5,3),(4,3),(3,3),(3,4),(4,4)]
path3='WWNNES'

l1=textLabel(m,'Total Cells', m.rows*m.cols)

m.tracePath({a:m.path}, delay=100)
m.tracePath({b:path2}, delay=200)
m.tracePath({c:path3}, delay=300)

m.run()