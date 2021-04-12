def apply_bound(xy, vel, xbound, ybound, damp, i):
    """
    честице које се нађу изван граница симулације се одбију назад и изгубе део енергије
    """
    vel0 = vel[i]
    if xy[i, 0] < xbound[0]:
        vel[i, 0] *= damp
        xy[i, 0] = xbound[0]
    elif xy[i, 0] > xbound[1]:
        vel[i, 0] *= damp
        xy[i, 0] = xbound[1]

    if xy[i, 1] < ybound[0]:
        vel[i, 1] *= damp
        xy[i, 1] = ybound[0]
    elif xy[i, 1] > ybound[1]:
        vel[i, 1] *= damp
        xy[i, 1] = ybound[1]

