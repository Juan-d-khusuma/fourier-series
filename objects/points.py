from pygame import init, draw, Rect
init()

class Point:
    def __init__(self,surface, x, y, color):
        self.surface = surface
        self.x = x
        self.y = y
        self.color = color
        self.Rect = Rect(x, y, 1.0, 1.0)

    def render(self):
        draw.rect(self.surface, self.color, self.Rect)