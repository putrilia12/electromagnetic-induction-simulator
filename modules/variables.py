import pygame
import os
pygame.init()
# Sprite addresses
(dirname, prom) = os.path.split(os.path.dirname(__file__))
magnet_address = dirname + '\\pic\\magnet.png'
icon_address = dirname + '\\pic\\icon.png'
# Sprites
sp_magnet = pygame.image.load(magnet_address)
icon = pygame.image.load(icon_address)
# Window variables
wind_width = 1250
wind_height = 700
simWindow = pygame.display.set_mode((wind_width, wind_height))
pygame.display.set_caption('Electromagnetism')
pygame.display.set_icon(icon)
# Color variables
background = (255, 255, 255)
magnetic_field_color = (97, 189, 194)
coil_color = (184, 115, 51)
# Lightbulb color will change during simulation
lightbulb_color = [35, 35, 0]
# Other variables
field_width = 330
field_height = 60
field_lines_thickness = 2
induction_min = 1
induction_max = 10
coil_width = 50
coil_height = 145
coil_min_height = 95
coil_max_height = 200
coil_spacing = 16
coil_thickness = 5
coil_min_num = 3
coil_max_num = 35
coil_line_lenght = 110
lightbulb_radius = 25
clock = pygame.time.Clock()
