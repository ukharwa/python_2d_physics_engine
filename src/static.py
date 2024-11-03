import pygame
import constants

class Static(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
    
    def draw(self, screen):
        pass

class Line(Static):
    def __init__(self, x1, y1, x2, y2):
        super().__init__()
        self.start = pygame.Vector2(x1, y1)
        self.end = pygame.Vector2(x2, y2)
        self.position = pygame.Vector2(x2 - x1, y2 - y1)
        self.type = constants.entity_types.LINE


    def draw(self, screen):
        pygame.draw.line(screen, "white", self.start, self.end, 2)