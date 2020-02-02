import pygame as pg

class Display:
    def __init__(self, cols, rows, cellw=40):
        self.columns, self.rows = cols, rows
        self.cellw = cellw
        self.width, self.height = size = cols*cellw+1, rows*cellw+1

        self.grid = {}
        self.start, self.target = (0, 0), (cols - 1, rows - 1)

        pg.init()
        self.screen = pg.display.set_mode(size)
        pg.display.set_caption('Pathfinding Algorithms')
        self.clock = pg.time.Clock()

        # colors
        self.c_bg = (0,0,0)
        self.c_fg = (255,255,255)
        self.c_walls = (100, 100, 100)
        self.c_start = (0, 200, 0)
        self.c_target = (200, 0, 0)

        self.running = True

    def make_grid(self):
        self.create_empty_grid()
        self.create_walls()
        return self.grid, self.start, self.target

    def draw_grid(self, walls=False):
        cellw = self.cellw
        sx, sy = self.start
        tx, ty = self.target

        if walls:
            for col in range(self.columns):
                for row in range(self.rows):
                    if (col, row) not in self.grid:
                        pg.draw.rect(self.screen, self.c_walls, (col * cellw, row * cellw, cellw, cellw))

        pg.draw.circle(self.screen, self.c_start, (sx*cellw + cellw//2, sy*cellw + cellw//2), int(cellw*0.3))
        pg.draw.circle(self.screen, self.c_target, (tx * cellw + cellw // 2, ty * cellw + cellw // 2), int(cellw * 0.3))

        for col in range(self.columns + 1):
            pg.draw.line(self.screen, self.c_fg, (col*cellw, 0), (col*cellw, self.width), 1)
        for row in range(self.rows + 1):
            pg.draw.line(self.screen, self.c_fg, (0, row * cellw), (self.height, row * cellw), 1)

    def create_empty_grid(self):
        # grid[(x,y)] = (distance, parent)
        for x in range(self.columns):
            for y in range(self.rows):
                self.grid[(x,y)] = (0, None)

    def create_walls(self):
        cellw = self.cellw
        start = True
        loop = True
        while loop:
            self.screen.fill(self.c_bg)
            mpos = pg.mouse.get_pos()
            pos = mpos[0] // cellw, mpos[1] // cellw

            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    loop = False

                if event.type == pg.MOUSEBUTTONDOWN and event.button == pg.BUTTON_MIDDLE:
                    if pos in self.grid:
                        if start:
                            self.start = pos
                        else:
                            self.target = pos
                        start = not start

            if pg.mouse.get_pressed()[0]:
                if pos in self.grid and pos not in (self.start, self.target):
                    del self.grid[pos]
            if pg.mouse.get_pressed()[2]:
                if pos not in self.grid:
                    self.grid[pos] = (0, None)

            self.draw_grid(walls=True)

            pg.display.update()


    def quit_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                return False
        return True





