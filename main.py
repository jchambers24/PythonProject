#Jack Chambers
import pygame

#Map Options and Variables
#Map Can Be Customized Here
map = [
"#####",
"#---#",
"##--#",
"#---#",
"#--##",
"#####",
]

tileSize = 50
wallColor = (0,0,0)
floorColor = (0,0,0)

#Variables
mapWidth = len(map[0])
mapHeight = len(map)
mapRow = 0
mapColumn = 0

#Pygame Window Fooey
screen = pygame.display.set_mode((mapWidth*tileSize, mapHeight*tileSize))
pygame.display.set_caption("Jacks Game")

#Main Program
for row in map:
  mapRow += 1
  mapColumn = 0
  for char in row:
    if char == "#":
      Tiles.SetWall()
    if char == "-":
      Tiles.SetFloor()
     
    mapColumn += 1
