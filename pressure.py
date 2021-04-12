from math import pi

def compute_density_pressure(xy,pressure,density,h,k,rest_density,grid):
    """
    рачунамо притиске
    """
    h_2 = h ** 2
    kernel_poly6 = 315 / (64 * pi * (h ** 9))

    for i in range(xy.shape[0]):
        density[i] = 0
        for j in grid.neighbours(xy[i]):
            r = xy[j] - xy[i]
            r_2 = r.dot(r)

            if r_2 <= h_2:
                density[i] += kernel_poly6 * (h_2 - r_2) ** 3

        pressure[i] = k * (density[i] - rest_density)

    return pressure, density
