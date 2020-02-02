class Search:
    def __init__(self, grid, start, target):
        self.grid = grid
        self.start, self.target = start, target

    def neighbours(self, pos):
        x, y = pos
        return [(x + dx, y + dy) for (dx, dy) in ((1, 0), (-1, 0), (0, 1), (0, -1)) if (x + dx, y + dy) in self.grid]

    def BFS(self):
        queue = [self.start]
        visited = [self.start]

        while queue:
            node = queue.pop(0)
            if node == self.target:
                print('BFS TARGET FOUND AT', node, 'DISTANCE', self.grid[node][0], 'VISITED', len(visited))
                break
            nbs = [nb for nb in self.neighbours(node) if nb not in visited]
            for nb in nbs:
                self.grid[nb] = (self.grid[node][0] + 1, node)
                queue.extend(nbs)
            visited.extend(nbs)
        return visited

