import pygame
from math import sqrt

class Simulation:
    def __init__(self):
        self.objects = []
        self.collisions = []

    def add_object(self, obj):
        self.objects.append(obj)
    
    def simulate(self, dt):
        ke = 0
        for i in self.objects:
            ke += 0.5 * i.mass * (i.velocity.x ** 2 + i.velocity.y ** 2)
            i.update(dt)
        print("kinetic energy", ke)


    def check_collisions(self):
        for i in range(len(self.objects)):
            for j in range(i+1, len(self.objects)):
                intersection = self.objects[i].getBound().intersect(self.objects[j].getBound())
                if intersection.doesIntersect:
                    self.collisions.append((self.objects[i], self.objects[j], intersection))
    
    def fix_collisions(self):
        for i in self.collisions:
            if i[2].ctype == 1:
                direction = (i[2].direction).normalize()
                relative_velocity = i[1].velocity - i[0].velocity
                relative_velocity_normal = direction * relative_velocity

                if relative_velocity_normal < 0:
                    m0 = i[0].mass
                    m1 = i[1].mass
                    
                    impulse = 2 * relative_velocity_normal / (m0 + m1)

                    i[0].velocity += impulse * m1 * direction
                    i[1].velocity -= impulse * m0 * direction
                
            else:
                i[1].velocity = i[1].velocity.reflect(i[0].normal)

    def handle_collisions(self):
        self.check_collisions()
        if self.collisions:
            self.fix_collisions()
            self.collisions = []

    def draw(self, screen):
        for i in self.objects:
            i.getBound().draw(screen)