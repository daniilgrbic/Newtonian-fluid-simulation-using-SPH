import numpy as np
from math import sqrt, pi


def compute_force(xy,vel,press,density,h,mass,visc,f_external,force,grid):
    """
    рачунамо силе притиска и вискозне силе
    """
    h_6 = h ** 6
    kernel_spiky = mass * -45 / (pi * h_6)
    kernel_visc = visc * mass * 45 / (pi * h_6)

    for i in range(xy.shape[0]):
        f_pres = np.array([0, 0], dtype=float)
        f_visc = np.array([0, 0], dtype=float)

        for j in grid.neighbours(xy[i]):
            if i == j:
                continue
            
            r = xy[j] - xy[i]
            n = sqrt(r.dot(r))

            if 0 < n < h:
                f_pres += -r / n * mass * (press[i] + press[j]) / (2 * density[j]) * kernel_spiky * ((h - n) ** 2)
                f_visc += visc * mass * (vel[j] - vel[i]) / density[j] * kernel_visc * (h - n)

        force[i] = f_pres + f_visc + f_external
    return force
