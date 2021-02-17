from pygame import init, display, Vector2, draw
from util.constants import COLOR

init()

### The surface where everything is rendered
class Surface:
    def __init__(self, width: int, height: int, enable_grid: bool = True, background: tuple[int]= COLOR["BLACK"]) -> None:
        self.width = width
        self.height = height
        self.enable_grid = enable_grid
        self.midpoint = Vector2(self.width/2, self.height/2)
        self.background = background
    
    ### Draw grid on the surface
    def __draw_grid(self) -> None:
        pass

    ### Render the surface
    def render(self) -> None:
        self.__initialized_surface = display.set_mode((self.width, self.height))
        if self.enable_grid:
            self.__draw_grid()    
    
    ### Clean the surface, make the screen black
    def blank_surface(self) -> None:
        if self.__initialized_surface != None:
            self.__initialized_surface.fill(COLOR["BLACK"]) 
