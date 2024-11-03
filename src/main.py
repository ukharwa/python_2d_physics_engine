import pygame
import constants
import entity, static

def main():
    pygame.init()
    print("Starting simulation.")
    print("Screen width: ", constants.SCREEN_WIDTH)
    print("Screen height: ", constants.SCREEN_HEIGHT)
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    solid = pygame.sprite.Group()

    entity.Circle.containers = (updateable, drawable, solid)
    static.Line.containers = (drawable, solid)


    circle = entity.Circle(20, 10, 10, 5)
    circle1 = entity.Circle(20, 30, 10, 10)
    circle2 = entity.Circle(20, 65, 10, 20)
    circle3 = entity.Circle(20, 150, 10, 40)

    line = static.Line(0, 500, 1080, 500)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        for i in updateable:
            i.update(dt)
            for j in solid:
                if i.check_collisons(j):
                    i.velocity = pygame.Vector2(0, 0)
                    i.acceleration = pygame.Vector2(0, 0)
        
        for i in drawable:
            i.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000




if __name__ == "__main__":
    main()