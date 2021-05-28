import pygame
import math
from queue import PriorityQueue

WIDTH = 800   #width of the display screen
WIN = pygame.display.set_mode((WIDTH,WIDTH))    #setting a display screen size
pygame.display.set_caption("A* Path Finding Algorithm")    #caption of a window


#defining colors for making paths and changing colors
#Capital letters determines they are constant

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,255,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (128,0,128)
ORANGE = (255,165,0)
GREY = (128,128,128)
TURQUOISE = (64,224,208)


#building visualiztion tool
class Node:
    # to define total cubes and their appearence on screen
    def _init_(self,row,col,width,total_rows):
        self.row = row
        self.col = col
        self.x = row * width   #actual corner position on screen
        self.y = col * width    #actual corner position on screen
        self.color = WHITE    # color of cubes
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows

    # represent rows and columns
    def get_pos(self):
        return self.row,self,col

    # Red color determines that we already looked at that path
    def is_closed(self):
        return self.color == RED

    # open point 
    def is_open(self):
        return self.color == GREEN

    # It is a barrier we have to avoid that path
    def is_barrier(self):
        return self.color == BLACK

    # It is the start node from which the path starts
    def is_start(self):
        return self.color == ORANGE

    # end color
    def is_end(self):
        return self.color == TURQUOISE

    # change the color back to white
    def reset(self):
        self.color == WHITE

# actually changes the color 
    # already looked at the path
    def make_closed(self):
        self.color = RED

    # open point
    def make_open(self):
        self.color = GREEN

    # avoid the path
    def make_barrier(self):
        self.color = BLACK

    # ending point
    def make_end(self):
        self.color = TURQUOISE

    # It is the path to follow
    def make_path(self):
        self.color = PURPLE

    # draw cube on the display screen
    def draw(self,win):
        pygame.draw.rect(win, self.color,(self.x,self.y,self.width,self.width)) #Draw a cube in pygame

    def update_neighbors(self,grid):
        pass

    # defines what happened when we compare two spots
    def _LT_(self,other):
        return False
    
# heuristic function    
# figure out the distance between two points
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

# holds all the spots in the grid
def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([]) # making list of list
        for j in range(rows):
            node=Node(i, j, gap, rows)
            grid[i].append(spot)
        return grid

# draw the grid lines
def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


    
