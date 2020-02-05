from display import Display
from search import Search

d = Display(20,20)
grid, start, target = d.make_grid(weight=True)

s = Search(grid, start, target)

visited = s.DFS_iterative(branches=False)

path = s.make_path()
d.draw_visited(visited)
d.draw_path(path)

d.reset_grid(weight=False)
s.DFS_recursive(start)
visited = s.visited
path = s.make_path()
d.draw_visited(visited)
d.draw_path(path)

d.reset_grid()
visited = s.BFS()
path = s.make_path()
d.draw_visited(visited, distance=True)
d.draw_path(path)




