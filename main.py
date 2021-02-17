from pygame import event, init, QUIT, quit
from objects.surface import Surface

init()

surface = Surface(500, 500, True)
surface.render()


def main() -> None:
    run = True
    while run:
        for i in event.get():
            if i.type == QUIT:
                quit()
                run = False
        surface.blank_surface
        
        
main()