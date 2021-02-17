# from pygame import event, init, QUIT, quit
from util.imports import *
from objects.surface import Surface

init()

surface = Surface(500, 500, True)
surface.render()

try:
    def main() -> None:
        run = True
        while run:
            for i in event.get():
                if i.type == QUIT:
                    quit()
                    run = False
            surface.blank_surface
except SyntaxError:
    print("\n\033[91m⚠ Make sure you're running this on Python 3.9\033[0m")
        
        
main()