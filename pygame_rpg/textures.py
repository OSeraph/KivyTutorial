import pygame

pygame.init()


class Tile(object):
    def __init__(self):
        self.size = 32
        self.dimensions = (self.size, self.size)

    def load_texture(self, file_name):
        bitmap = pygame.image.load(file_name)
        bitmap = pygame.transform.scale(bitmap, self.dimensions)
        surface = pygame.Surface(self.dimensions, pygame.HWSURFACE | pygame.SRCALPHA)
        surface.blit(bitmap, (0, 0))
        return surface

    # grass = load_texture("/Users/seraphino1/Developer/repositories/KivyTutorial/pygame_rpg/graphics/textures/grass.png")
    # # sky = load_texture('/Users/seraphino1/Developer/repositories/KivyTutorial/pygame_rpg/graphics/textures/sky.jpg')
    # stone = load_texture('/Users/seraphino1/Developer/repositories/KivyTutorial/pygame_rpg/graphics/textures/stone.jpg')
    # water = load_texture('/Users/seraphino1/Developer/repositories/KivyTutorial/pygame_rpg/graphics/textures/water.png')
    #
