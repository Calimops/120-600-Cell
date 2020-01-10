import pygame as pg
import numpy as np
import XXIVcell
from Rotation_Code import *

pg.init()

WIDTH = 640
HEIGHT = 640

l = 65
scale = np.pi/200

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

    factor = 0.3

    display.fill((255, 255, 255))

    M = rotator(nn*scale, ab, ac, ad, bc, bd, cd)

    new_vert = {}
    for vert in XXIVcell.vertices:
        new_vert[vert] = l*M.dot(XXIVcell.vertices[vert])

    new_face = {}
    for face in XXIVcell.faces:
        new_face[face] = l*M.dot(XXIVcell.faces[face])

    order = []
    for cell in XXIVcell.cells:
        order.append([cell, projection1(M.dot(XXIVcell.cells[cell]), d1)[2]])
        
    order.sort(key = lambda x: x[1])
    Order = [x[0] for x in order]

    for x in Order:
        cellorder = []
        cc = l*M.dot(XXIVcell.cells[x])
        
        for face in XXIVcell.cellfaces[x]:
            cellorder.append([face, projection1(new_face[face], d1)[2]])
            
        cellorder.sort(reverse = True, key = lambda x: x[1])
        Cellorder = [x[0] for x in cellorder]
        
        for faces in Cellorder:
            p1 = projection2(projection1((1 - factor)*cc + factor*new_vert[faces[0]], d1), d2)
            p2 = projection2(projection1((1 - factor)*cc + factor*new_vert[faces[1]], d1), d2)
            p3 = projection2(projection1((1 - factor)*cc + factor*new_vert[faces[2]], d1), d2)

            pg.draw.polygon(display,
                            (255,
                            10,
                            127),
                            [(p1[0] + 320, p1[1] + 320),
                             (p2[0] + 320, p2[1] + 320),
                             (p3[0] + 320, p3[1] + 320)])

            pg.draw.lines(display,
                          (0,
                           0,
                           0),
                          True,
                          [(p1[0] + 320, p1[1] + 320),
                           (p2[0] + 320, p2[1] + 320),
                           (p3[0] + 320, p3[1] + 320)],
                          3)

        
    pg.time.delay(10)
    pg.display.flip()
    clock.tick(10)
    nn += 1
pg.quit()
quit()
