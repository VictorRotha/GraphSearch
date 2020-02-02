from display import Display
from search import Search

d = Display(20,20)
grid, start, target = d.make_grid()

s = Search(grid, start, target)
visited = s.BFS()

d.draw_visited(visited)



