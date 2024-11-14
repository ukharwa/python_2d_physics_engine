import pygame, random
import constants
import shape, entity
import simulation

def main():
    pygame.init()
    print("Starting simulation.")
    print("Screen width: ", constants.SCREEN_WIDTH)
    print("Screen height: ", constants.SCREEN_HEIGHT)
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    engine = simulation.Simulation()
    left_wall = entity.Line(pygame.Vector2(1, 0), 5, constants.SCREEN_HEIGHT * 2 - 10)
    right_wall = entity.Line(pygame.Vector2(1, 0), constants.SCREEN_WIDTH - 10, constants.SCREEN_HEIGHT * 2 - 10)
    top_wall = entity.Line(pygame.Vector2(0, 1), 5, constants.SCREEN_WIDTH * 2 - 10)
    bottom_wall = entity.Line(pygame.Vector2(0, 1), constants.SCREEN_HEIGHT - 10, constants.SCREEN_WIDTH * 2 - 10)

    engine.add_object(left_wall)
    engine.add_object(right_wall)
    engine.add_object(top_wall)
    engine.add_object(bottom_wall)

    for i in range(100):
        pos = pygame.Vector2(random.randrange(20, constants.SCREEN_WIDTH - 20), random.randrange(20, constants.SCREEN_HEIGHT - 20))
        vel = pygame.Vector2(random.randrange(0, 70), random.randrange(0, 70))
        mass = random.randrange(10, 200)
        obj = entity.Circle(pos, 5, vel, mass, pygame.Color(255, 255-mass, 255-mass))
        engine.add_object(obj)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        engine.simulate(dt)
        engine.handle_collisions()
        engine.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()