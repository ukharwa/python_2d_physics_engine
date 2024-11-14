from enum import Enum
import shape
import pygame


class intersectData:   
    def __init__(self, doesIntersect, direction, ctype):
        self.doesIntersect = doesIntersect
        self.direction = direction
        self.distance = direction.distance_to(pygame.Vector2(0, 0))
        self.ctype = ctype

    def __repr__(self):
        return "Intersect: " + str(self.doesIntersect) + " direction: " + str(self.distance)
