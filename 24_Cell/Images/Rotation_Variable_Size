import pygame as pg
import numpy as np
import XXIVcell
from Rotation_Code import *

pg.init()

WIDTH = 640
HEIGHT = 640

l = 65
scale = np.pi/100

d1 = 100
d2 = 100

ab = 0
ac = 0
ad = 0
bc = 1
bd = 1
cd = 1

display = pg.display.set_mode((WIDTH, HEIGHT))

display.fill((255, 255, 255))

clock = pg.time.Clock()
done = False

nn = 0
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    factor = (1 + np.cos(5*nn*scale))/6

    display.fill((0, 0, 0))

    M = rotator(nn*scale, ab, ac, ad, bc, bd, cd)

    new_points = []

    for vert in XXIVcell.vertices:
        new_points.append(l*M.dot(XXIVcell.vertices[vert]))

    order = []
    for cell in XXIVcell.cells:
        order.append([cell, projection1(M.dot(XXIVcell.cells[cell]), d1)[2]])
    order.sort(key=lambda x: x[1])
    
    for i in range(24):
        cc = l*M.dot(XXIVcell.cells[order[i][0]])
        for line in XXIVcell.celllines[order[i][0]]:
            p1 = projection2(projection1((1 - factor)*cc + factor*new_points[ord(line[0])-97], d1), d2)
            p2 = projection2(projection1((1 - factor)*cc + factor*new_points[ord(line[1])-97], d1), d2)
            pg.draw.line(display,
                         (255-5*i,
                          10*i,
                          127 + 5*i*np.cos(nn*scale)),
                         (int(p1[0]) + 320, int(p1[1]) + 320),
                         (int(p2[0]) + 320, int(p2[1]) + 320),
                         3)

        
    pg.time.delay(10)
    pg.display.flip()
    clock.tick(10)
    nn += 1
pg.quit()
quit()
