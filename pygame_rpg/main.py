import pygame
import sys
import time
from pygame_rpg.textures import Tile
from pygame_rpg.pantone_colors import PantoneColor

pygame.init()

c_second = 0
c_frame = 0
fps = 0
fps_font = pygame.font.Font("/Users/seraphino1/Developer/repositories/KivyTutorial/PressStart2P-Regular.ttf", 20)
tile_size = 32
tile = Tile()
grass_texture = tile.load_texture('/Users/seraphino1/Developer/repositories/KivyTutorial/pygame_rpg/graphics/textures/grass.png')
stone_texture = tile.load_texture('/Users/seraphino1/Developer/repositories/KivyTutorial/pygame_rpg/graphics/textures/stone.jpg')
water_texture = tile.load_texture('/Users/seraphino1/Developer/repositories/KivyTutorial/pygame_rpg/graphics/textures/water.png')
sky_texture = pygame.image.load('/Users/seraphino1/Developer/repositories/KivyTutorial/pygame_rpg/graphics/textures/sky.jpg')

sky = pygame.Surface(sky_texture.get_size(), pygame.HWSURFACE|pygame.DOUBLEBUF)
sky.blit(sky_texture, (0, 0))
# del sky_texture


def shpw_fps():
    fps_overlay = fps_font.render(str(fps), True, PantoneColor.ORANGE_021_C)
    window.blit(fps_overlay, (0, 0))


def create_window():
    global window, window_height, window_width, window_title
    window_width, window_height = 800, 600
    window_title = "Youtube RPG"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)


def fps_count():
    # current second , current frame, frames per second, delta time
    global c_second, c_frame, fps, delta_time

    if c_second == time.strftime("%S"):
        c_frame += 1
    else:
        fps = c_frame
        c_frame = 0
        c_second = time.strftime("%S")

def main():
    create_window()
    isRunning = True

    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
        # Logic
        fps_count()

        # Render Graphics (0, 0, 0)
        window.blit(sky, (0, 0))

        # Render simple terrain grid
        for x in range(0, 640, tile.size):
            for y in range(0, 480, tile.size):
                # pygame.draw.rect(window, PantoneColor.RHODAMINE_RED_C, (x, y, tile_size + 1, tile_size + 1), 1)
                window.blit(grass_texture, (x, y))
        shpw_fps()
        pygame.display.update()


    pygame.quit()
    sys.exit('Exiting game, property isRunning set to False. GoodBye')

if __name__ == "__main__":
    main()

