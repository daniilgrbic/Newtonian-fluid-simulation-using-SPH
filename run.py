"""
главни део SPH симулације који обједиљује све потребне модуле/функције
"""

# укључивање модула
from graphics import *
from force import compute_force
from pressure import compute_density_pressure
from integrate import do_step
from grid import Grid

# спољашње библиотеке
import numpy as np
from time import time

# иницијализација dam-break експеримента 
def setup_sim():
    i = 0
    for y in range(boundary_y[0], boundary_y[1], h):
        for x in range(boundary_x[0] + 80, boundary_x[1]-80, h):
            if i < N:
                # функција np.random.normal(А, Д) враћа независне случајне величине са просеком А и девијацијом Д
                coordinates[i] = x + np.random.normal(0, 0.25), y + np.random.normal(0, 0.25)
                hashmap.move(i, coordinates[i])
            i += 1
        
# један 'фрејм' или корак
def next_frame():
    global pressure, density, force
    # рачунамо притиске
    pressure, density = compute_density_pressure(coordinates, pressure, density, h, k, rest_density, hashmap)
    # рачунамо резултујуће силе
    force = compute_force(coordinates, vel, pressure, density, h, mass, visc, f_external, force, hashmap)
    # интеграција
    do_step(coordinates, vel, force, density, delta, boundary_x, boundary_y, damping, hashmap)

if __name__ == "__main__":
    N = 1000  # број честица
    width, height = 350, 350 # димензије PyGame прозора
    boundary_x,boundary_y = [40,width-40],[40,height-40] # границе симулације

    # параметри честица
    mass = 1  # маса честице
    k = 40  # Десбрунов коефициент ( п = k(ρ−ρ0) )
    rest_density = 1  # густина мировања ρ0
    h = 5  # радијус језгара
    visc = 0.15  # коефициент вискозности
    f_external = np.array([0, -0.1])  # вектор спољашње силе
    delta = 0.03  # временски корак
    damping = -0.5  # подеок 4.9

    # NumPy низови
    coordinates = np.zeros((N, 2)) # позиције
    vel = np.zeros((N, 2))  # брзине 
    force = np.zeros((N, 2))  # резултујуће силе
    density = np.zeros(N)  # густине у околини честица
    pressure = np.zeros(N) # притисак на честице

    # просторни хеш
    hashmap = Grid(width, height, h)

    # изглед симулације (позадина; боја и димензије честица)
    background_color, border_color= (255,255,255), (200,200,200)
    particle_radius, particle_width = 1, 1
    particle_color = (0,102,255)

    # иницијализација Pygame екрана (променљива screen)
    screen = screen_init(width, height, background_color)
    setup_sim()
    screen_refresh(screen)

    paused = False
    while True:
        event = process_event()
        # притиском на тастер 'p' паузитамо симулацију (корисно при анализи)
        if event == 'PAUSE':
            paused = not paused
            print("Paused:", paused)
        # притисом на тастер 'q' симулација с епрекида
        elif event == 'QUIT':
            print("Process terminated")
            break
        if paused: 
            continue
        screen_clear(screen, background_color)
        next_frame() # ту се одвија рачун
        print(time())
        border_draw(screen, boundary_x, boundary_y, width, height, border_color)
        for x, y in coordinates:
            screen_draw(screen, particle_color, int(x), int(350-y), particle_radius, particle_width)
        screen_refresh(screen)

