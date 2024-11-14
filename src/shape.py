import pygame
import collision

class BoundingCircle:
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color

    def intersectCircle(self, other):
        combined_radii = self.radius + other.radius
        center_distance = self.center.distance_to(other.center)
        distance = center_distance - combined_radii
        direction = (self.center - other.center).normalize()

        return collision.intersectData(center_distance < combined_radii, distance * direction, 1)

    def intersect(self, other):
        if isinstance(other, BoundingCircle):
            return self.intersectCircle(other)
        if isinstance(other, BoundLine):
            return other.intersectCircle(self)
        
        return collision.intersectData(False, pygame.Vector2(0, 0), 3)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.center, self.radius)

class BoundLine:
    def __init__(self, normal, distance, length):
        self.normal = normal.normalize()
        self.distance = distance
        self.length = length

        direction_vector = pygame.Vector2(-self.normal.y, self.normal.x)
        half = direction_vector * self.length/2
        midpoint = self.normal * self.distance

        self.start = pygame.Vector2(midpoint.x - half.x, midpoint.y - half.y)
        self.end = pygame.Vector2(midpoint.x + half.x, midpoint.y + half.y)
    
    def intersectCircle(self, other):
        distance_from_circle_center = abs((self.normal * other.center) - self.distance)
        distance_from_circle = distance_from_circle_center - other.radius

        return collision.intersectData(distance_from_circle < 0, self.normal * distance_from_circle, 2)
    
    
    def intersect(self, other):
        if isinstance(other, BoundingCircle):
            return self.intersectCircle(other)
        
        return collision.intersectData(False, pygame.Vector2(0, 0), 3)
    
    def draw(self, screen):
        pygame.draw.line(screen, "white", self.start, self.end, 2)