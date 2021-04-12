from boundary import apply_bound

def do_step(coordinates, vel, force, density, dt, xbound, ybound, damp, grid):
    for i in range(coordinates.shape[0]):
        vel[i] += dt * force[i] / density[i]
        coordinates[i] += dt * vel[i]
        apply_bound(coordinates, vel, xbound, ybound, damp, i)
        grid.move(i, coordinates[i])
