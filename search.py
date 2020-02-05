class Search:
    def __init__(self, grid, start, target):
        self.grid = grid
        self.start, self.target = start, target
        self.visited = []

    def neighbours(self, pos):
        x, y = pos
        return [(x + dx, y + dy) for (dx, dy) in ((1, 0), (-1, 0), (0, 1), (0, -1)) if (x + dx, y + dy) in self.grid]

    def make_path(self):
        path = [self.target]
        node = self.target
        while self.grid[node][1] is not None:
            _, parent, _ = self.grid[node]
            path.append(parent)
            node = parent
        return path

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
                self.grid[nb] = (self.grid[node][0] + 1, node, self.grid[nb][2])
                queue.extend(nbs)
            visited.extend(nbs)
        return visited

    def DFS_iterative(self, branches=False):
        visited = [self.start]
        stack = [self.start]
        distance = 0
        deadend = False
        while stack:
            node = stack.pop()
            if node == self.target:
                if branches:
                    print('DFS ITERATIVE TARGET FOUND AT', node, 'BRANCHES', self.grid[node][0], 'VISITED', len(visited))
                else:
                    print('DFS ITERATIVE TARGET FOUND AT', node, 'DISTANCE', self.grid[node][0], 'VISITED', len(visited))
                break

            nbs = [nb for nb in self.neighbours(node) if nb not in visited]
            stack.extend(nbs)
            visited.extend(nbs)

            if branches:
                if not nbs:
                    deadend = True

                elif deadend:
                    deadend = False
                    distance += 1
                    self.grid[node] = (distance, self.grid[node][1], self.grid[node][2])
            else:
                distance = self.grid[node][0] + 1
            for nb in nbs:
                self.grid[nb] = (distance, node, self.grid[nb][2])
        return visited

    def DFS_recursive(self, node):
        self.visited.append(node)
        if node == self.target:
            print('DFS RECOURSIVE TARGET FOUND AT', node, 'DISTANCE', self.grid[node][0], 'VISITED', len(self.visited))
            return True
        nbs = self.neighbours(node)
        distance = self.grid[node][0] + 1
        for nb in nbs:
            if nb not in self.visited:
                self.grid[nb] = (distance, node, self.grid[nb][2])
                if self.DFS_recursive(nb):
                    return True
        return False
