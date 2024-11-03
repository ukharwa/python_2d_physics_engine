import pygame
import constants

class Entity(pygame.sprite.Sprite):
    def __init__(self, mass, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.mass = mass
        self.position = pygame.Vector2(x, y)
        self.acceleration = pygame.Vector2(0, constants.GRAVITY)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def check_collisons(self, other):
        pass

class Circle(Entity):
    def __init__(self, mass, x, y, radius):
        super().__init__(mass, x, y)
        self.type = constants.entity_types.CIRCLE
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt

    def check_collisons(self, other):
        if other == self:
            return False
        if other.type == constants.entity_types.CIRCLE:
            return (self.position.distance_to(other.position) <= self.radius + other.radius)
        if other.type == constants.entity_types.LINE:
            circle_to_line = self.position - other.start
            t = pygame.math.clamp((circle_to_line * other.position) / (other.position * other.position), 0, 1)
            p = pygame.Vector2(other.start.x + t * other.position.x, other.start.y + t * other.position.y)
            return (self.position.distance_to(p) <= self.radius)
