#Jack Chambers
import pygame
pygame.init()

#Map Options and Variables
mapArray = [
"###########",
"#---#--##-#",
"##--##-##-#",
"#----#-##-#",
"#-##---##-#",
"###########",
]

tileSize = 25
wallColor = (0,0,0)
floorColor = (255,255,255)

#Initialization
pygame.init()

#Variables
fps = 60
mapWidth = len(mapArray[0])
mapHeight = len(mapArray)
mapRow = -1
mapColumn = 0

#Pygame Window Fooey
screen = pygame.display.set_mode((mapWidth*tileSize, mapHeight*tileSize))
pygame.display.set_caption("Jacks Game")
clock = pygame.time.Clock()

#Main Program
screen.fill((255,255,255))
for row in mapArray:
  mapRow += 1
  mapColumn = 0
  for char in row:
    rectangle = pygame.Rect((mapColumn*tileSize,mapRow*tileSize), (tileSize, tileSize))
    if char == "#":
      pygame.draw.rect(screen, wallColor, rectangle)
    if char == "-":
      pygame.draw.rect(screen, floorColor, rectangle)
    
    mapColumn += 1
  
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit();
  clock.tick(fps)
  pygame.display.flip()
