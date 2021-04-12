import pygame

# иницијализација PyGame екрана са задатим параметрима
def screen_init(width, height, background_color) -> pygame.display:
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption('SPH Fluid Sim')
    screen.fill(background_color)
    return screen

# ф-ја која чисти екран
def screen_clear(screen, background_color):
    screen.fill(background_color)

# ф-ја која "рефрешује" екран, односно исцртава најновију слику из бафера
def screen_refresh(screen):
    pygame.display.flip()

# ф-ја која смештава честицу са задатим координатама у display бафер
# чести се прикаже на екрану тек након позивања ф-је screen_refresh()
def screen_draw(screen, color, x, y, radius, width):
    pygame.draw.circle(screen, color, (x,y), radius, width)

def border_draw(screen, x, y, w, h, color):
    pygame.draw.rect(screen,color,(x[0]-3,y[0]-3,x[1]-x[0]+6,y[1]-y[0]+6), 3)

# ф-ја која обрађује корисничке команде
def process_event() -> str: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            return 'QUIT'
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            return 'PAUSE'
    return None
