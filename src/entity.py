import shape, constants
import pygame

class Entity:
    def __init__(self, position, velocity, mass):
        self.velocity = velocity
        self.position = position
        self.mass = mass

    def update(self, dt):
        self.position += self.velocity * dt
    
    def getBound(self):
        pass

class Circle(Entity):
    def __init__(self, center, radius, velocity, mass, color):
        super().__init__(center, velocity, mass)
        self.radius = radius
        self.color = color
    
    def getBound(self):
        return shape.BoundingCircle(self.position, self.radius, self.color)
    
class Line(Entity):
    def __init__(self, normal, distance, length):
        super().__init__(normal * distance, pygame.Vector2(0, 0), constants.INFINITY)
        self.normal = normal
        self.distance = distance
        self.length = length
    
    def getBound(self):
        return shape.BoundLine(self.normal, self.distance, self.length)
    
    def update(self, dt):
        self.velocity = pygame.Vector2(0, 0)