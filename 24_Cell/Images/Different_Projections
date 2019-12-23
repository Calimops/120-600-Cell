from Rotation_Code import *
import pygame as pg
import numpy as np
import XXIVcell

pg.init()

WIDTH = 640
HEIGHT = 640

l = 50
scale = np.pi/100

d1 = 2.2
d2 = 2.2
d3 = 2.2
d4 = 2.2

ab = 0
ac = 0
ad = 1
bc = 1
bd = 0
cd = 0


display = pg.display.set_mode((WIDTH, HEIGHT))                

def projection3(x, d3):
    u = d3/(d3 - x[0])
    y = x[1:]
    z = u*y
    return z

def projection4(x, d4):
    u = d4/(d4 - x[0])
    y = x[1:]
    z = u*y
    return z


#CHANGE BACKGROUND COLOUR

display.fill((255, 255, 255))

clock = pg.time.Clock()
done = False

#COLOUR SCHEMES
#(max(0, min(128*(1 + np.sin(n*s)), 255)), max(0, min(128*(1 + np.cos(n*s)), 255)), 5*(x[0] + x[1]))

nn = 0
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    color = (127*(1 + np.cos(nn*scale)), 127*(1 + np.sin(nn*scale)), 0)

    display.fill((255, 255, 255))

    M = rotator(nn*scale, ab, ac, ad, bc, bd, cd)

    new_points1 = []

    new_points2 = []

    new_points3 = []

    new_points4 = []

    for vert in XXIVcell.vertices:
        new_points1.append(l*projection2(projection1(M.dot(XXIVcell.vertices[vert]), d1), d2))

    for line in XXIVcell.lines:
        new_points2.append(l*projection2(projection1(M.dot(XXIVcell.lines[line]), d1), d2))

    for face in XXIVcell.faces:
        new_points3.append(l*projection2(projection1(M.dot(XXIVcell.faces[face]), d1), d2))

    for cell in XXIVcell.cells:
        new_points4.append(l*projection2(projection1(M.dot(XXIVcell.cells[cell]), d1), d2))
        
    for points in new_points1:
        pg.draw.circle(display, (int('FF', 16), int('00', 16), int('CC', 16)), (int(points[0]) + 440, int(points[1]) + 320), 2)

    for lines in new_points2:
        pg.draw.circle(display, (int('FF', 16), int('33', 16), int('00', 16)), (int(lines[0]) + 440, int(lines[1]) + 320), 2)

    for faces in new_points3:
        pg.draw.circle(display, (int('99', 16), int('FF', 16), int('33', 16)), (int(faces[0]) + 440, int(faces[1]) + 320), 2)

    for cells in new_points4:
        pg.draw.circle(display, (int('CC', 16), int('00', 16), int('66', 16)), (int(cells[0]) + 440, int(cells[1]) + 320), 2)

    for line in (XXIVcell.celllines['aeimqu'] + XXIVcell.celllines['cgkmqu'] +
                 XXIVcell.celllines['cdghkl'] + XXIVcell.celllines['dhlptx'] +
                 XXIVcell.celllines['bfjptx'] + XXIVcell.celllines['abefij']):
        pg.draw.line(display,
                     (0, 0, 0),
                     (int(new_points1[ord(line[0]) - 97][0]) + 440, int(new_points1[ord(line[0]) - 97][1]) + 320),
                     (int(new_points1[ord(line[1]) - 97][0]) + 440, int(new_points1[ord(line[1]) - 97][1]) + 320),
                     3)

    new_points5 = []

    new_points6 = []

    new_points7 = []

    new_points8 = []

    for vert in XXIVcell.vertices:
        new_points5.append(l*projection4(projection3(M.dot(XXIVcell.vertices[vert]), d3), d4))

    for line in XXIVcell.lines:
        new_points6.append(l*projection4(projection3(M.dot(XXIVcell.lines[line]), d3), d4))

    for face in XXIVcell.faces:
        new_points3.append(l*projection4(projection3(M.dot(XXIVcell.faces[face]), d3), d4))

    for cell in XXIVcell.cells:
        new_points8.append(l*projection4(projection3(M.dot(XXIVcell.cells[cell]), d3), d4))
        
    for points in new_points5:
        pg.draw.circle(display, (int('FF', 16), int('00', 16), int('CC', 16)), (int(points[0]) + 200, int(points[1]) + 320), 2)

    for lines in new_points6:
        pg.draw.circle(display, (int('FF', 16), int('33', 16), int('00', 16)), (int(lines[0]) + 200, int(lines[1]) + 320), 2)

    for faces in new_points7:
        pg.draw.circle(display, (int('99', 16), int('FF', 16), int('33', 16)), (int(faces[0]) + 200, int(faces[1]) + 320), 2)

    for cells in new_points8:
        pg.draw.circle(display, (int('CC', 16), int('00', 16), int('66', 16)), (int(cells[0]) + 200, int(cells[1]) + 320), 2)

    for line in (XXIVcell.celllines['aeimqu'] + XXIVcell.celllines['cgkmqu'] +
                 XXIVcell.celllines['cdghkl'] + XXIVcell.celllines['dhlptx'] +
                 XXIVcell.celllines['bfjptx'] + XXIVcell.celllines['abefij']):
        pg.draw.line(display,
                     (0, 0, 0),
                     (int(new_points5[ord(line[0]) - 97][0]) + 200, int(new_points5[ord(line[0]) - 97][1]) + 320),
                     (int(new_points5[ord(line[1]) - 97][0]) + 200, int(new_points5[ord(line[1]) - 97][1]) + 320),
                     3)

        
    pg.time.delay(10)
    pg.display.flip()
    clock.tick(10)
    nn += 1
pg.quit()
quit()
