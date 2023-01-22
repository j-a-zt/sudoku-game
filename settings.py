WIDTH   = 900
HEIGHT  = 900
GAP = 150

GRID_WIDTH  = WIDTH - GAP
GRID_HEIGHT = HEIGHT - GAP
GRID_POS    = (GAP/2,GAP/2)
CELLSIZE    = GRID_WIDTH/9
outer_thickness   = 3

# COLOR
WHITE   = (255,255,255)
BLACK   = (0,0,0)
LIGHTBLUE = (204,255,255)

# GRID POSITION


# GRID
testBoard = [ [0 for x in range(9)] for x in range(9) ]

# FPS
FPS = 60

# SOUND
hover_sound = 'audio/hover_sound.wav'