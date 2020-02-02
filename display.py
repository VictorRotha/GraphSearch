import pygame as pg

class Display:
    def __init__(self, cols, rows, cellw=40):
        self.columns, self.rows = cols, rows
        self.cellw = cellw

        self.width, self.height = size = cols*cellw+1, rows*cellw+1

        pg.init()
        self.screen = pg.display.set_mode(size)
        pg.display.set_caption('Pathfinding Algorithms')
        self.clock = pg.time.Clock()

        # colors
        self.c_bg = (0,0,0)
        self.c_fg = (255,255,255)

        self.running = True

    def run(self):
        self.draw_empty_grid()

    def draw_empty_grid(self):
        cellw = self.cellw
        while self.quit_loop():
            for col in range(self.columns + 1):
                pg.draw.line(self.screen, self.c_fg, (col*cellw, 0), (col*cellw, self.width), 1)
            for row in range(self.rows + 1):
                pg.draw.line(self.screen, self.c_fg, (0, row * cellw), (self.height, row * cellw), 1)

            pg.display.update()


    def quit_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                return False
        return True





