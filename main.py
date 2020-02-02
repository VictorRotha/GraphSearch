from display import Display
from search import Search

d = Display(20,20)
grid, start, target = d.make_grid()

s = Search(grid, start, target)
visited = s.BFS()
path = s.make_path()

d.draw_visited(visited)
d.draw_path(path)



