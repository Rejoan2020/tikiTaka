from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

zone_of_the_line = 0;

def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def drawit(point1,point2):
    ans = mpa(point1, point2)
    for i in range(2, len(ans), 2):
        draw_points(ans[i], ans[i + 1])

def draw_vertical_line(x):
    point3 = (152+x,150)
    point4 = (152+x,350)
    drawit(point3,point4)

def draw_upper_horizontal_line(x):
    p1 = (101+x,348)
    p2 = (203+x,348)
    drawit(p1,p2)

def draw_horizontal_line(x):
    point1 = (101+x,150)
    point2 = (203+x,150)
    drawit(point1,point2)

def draw_middle_horizontal(x):
    p1 = (203+x,250)
    p2 = (101+x,250)
    drawit(p2,p1)

def draw_right_vertical_line(x):
    p1 = (205+x,347)
    p2 = (205+x,150)
    drawit(p2,p1)

def draw_hypo(x):
    point1 = (100+x,300)
    point2 = (150+x,350)
    drawit(point1,point2)

def draw_one(x):
    draw_hypo(x)
    draw_vertical_line(x)
    draw_horizontal_line(x)

def draw_two(x):
    draw_upper_horizontal_line(x)
    draw_horizontal_line(x)
    p3 = (205+x,346)
    p4 = (205+x,250)
    drawit(p4,p3)
    draw_middle_horizontal(x)
    p1 = (101+x,248)
    p2 = (101+x,150)
    drawit(p2,p1)

def draw_three(x):
    draw_horizontal_line(x)
    draw_middle_horizontal(x)
    draw_upper_horizontal_line(x)
    draw_right_vertical_line(x)

def draw_four(x):
    draw_right_vertical_line(x)
    p1 = (101+x,220)
    p2 = (210+x,220)
    drawit(p1,p2)
    p3 = (205+x,347)
    drawit(p1,p3)

def draw_five(x):
    draw_upper_horizontal_line(x)
    draw_horizontal_line(x)
    draw_middle_horizontal(x)
    p1 = (101+x,347)
    p2 = (101+x,250)
    drawit(p2,p1)
    p1 = (205+x,248)
    p2 = (205+x,150)
    drawit(p2,p1)

def draw_six(x):
    draw_upper_horizontal_line(x)
    draw_horizontal_line(x)
    draw_middle_horizontal(x)
    p1 = (101+x,347)
    p2 = (101+x,150)
    drawit(p2,p1)
    p1 = (205+x,247)
    p2 = (205+x,150)
    drawit(p2,p1)

def draw_seven(x):
    draw_upper_horizontal_line(x)
    p1 = (203+x,347)
    p2 = (141+x,145)
    drawit(p2,p1)

def draw_eight(x):
    draw_upper_horizontal_line(x)
    draw_middle_horizontal(x)
    draw_horizontal_line(x)
    draw_right_vertical_line(x)
    p1 = (101+x,150)
    p2 = (101+x,347)
    drawit(p1,p2)

def draw_nine(x):
    draw_horizontal_line(x)
    draw_middle_horizontal(x)
    draw_upper_horizontal_line(x)
    draw_right_vertical_line(x)
    p1 = (101+x,347)
    p2 = (101+x,250)
    drawit(p2,p1)

def draw_zero(x):
    draw_upper_horizontal_line(x)
    draw_horizontal_line(x)
    draw_right_vertical_line(x)
    p1 = (101+x,347)
    p2 = (101+x,150)
    drawit(p2,p1)

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    #draw_points(100,200)
    global ld
    global pd
    #print(ld)
    if pd == 1 :
        draw_one(0)
    if pd == 2 :
        draw_two(0)
    if pd == 3 :
        draw_three(0)
    if pd == 4 :
        draw_four(0)
    if pd == 5 :
        draw_five(0)
    if pd == 6 :
        draw_six(0)
    if pd == 7 :
        draw_seven(0)
    if pd == 8 :
        draw_eight(0)
    if pd == 9 :
        draw_nine(0)
    if pd == 0 :
        draw_zero(0)
    if ld == 1:
        draw_one(150)
    if ld == 2:
        draw_two(150)
    if ld == 3:
        draw_three(150)
    if ld == 4:
        draw_four(150)
    if ld == 5:
        draw_five(150)
    if ld == 6:
        draw_six(150)
    if ld == 7:
        draw_seven(150)
    if ld == 8:
        draw_eight(150)
    if ld == 9:
        draw_nine(150)
    if ld == 0:
        draw_zero(150)

    #draw_two(0)
    #draw_two(150)
    #draw_three(0)
    #draw_three(150)
    #draw_four(0)
    #draw_four(150)
    #draw_five(0)
    #draw_five(150)
    #draw_six(0)
    #draw_six(150)
    #draw_seven(0)
    #draw_seven(150)
    #draw_eight(0)
    #draw_eight(150)
    #draw_nine(0)
    #draw_nine(150)
    #draw_zero(0)
    #draw_zero(150)


    glutSwapBuffers()


def findzone(x1,y1):
    dx = x1
    dy = y1
    ans = 0
    if abs(dx) > abs(dy) :
        if dx>0:
            if dy>0:
                ans = 0
            else :
                ans = 7
        else :
            if dy>0:
                ans = 3
            else :
                ans = 4
    else :
        if dx>0:
            if dy>0:
                ans = 1
            else :
                ans = 6
        else :
            if dy>0:
                ans = 2
            else :
                ans = 5
    return ans

def convert_to_original_zone(a,b):
    x1=0
    y1=0
    zone = zone_of_the_line
    if zone == 1:
        x1 = b
        y1 = a
    elif zone == 2:
        x1 = b
        y1 = -a
    elif zone == 3:
        x1 = -a
        y1 = b
    elif zone == 4:
        x1 = -a
        y1 = -b
    elif zone == 5:
        x1 = -b
        y1 = -a
    elif zone == 6:
        x1 = -b
        y1 = a
    elif zone == 7:
        x1 = a
        y1 = -b
    else:
        x1 = a
        y1 = b

    r=(x1,y1)
    return r

def convert_back(a,b) :
    x1 = 0
    y1 = 0
    zone = zone_of_the_line
    if zone == 1:
        x1 = b
        y1 = a
    elif zone == 2:
        x1 = -b
        y1 = a
    elif zone == 3:
        x1 = -a
        y1 = b
    elif zone == 4:
        x1 = -a
        y1 = -b
    elif zone == 5:
        x1 = -b
        y1 = -a
    elif zone == 6:
        x1 = b
        y1 = -a
    elif zone == 7:
        x1 = a
        y1 = -b
    else:
        x1 = a
        y1 = b

    r = (x1, y1)
    return r

def mpa(a,b) :
    dx = abs(a[0]-b[0])
    dy = abs(a[1]-b[1])
    global zone_of_the_line
    zone_of_the_line = findzone(dx,dy)

    p = convert_to_original_zone(a[0],a[1])
    q = convert_to_original_zone(b[0],b[1])
    dx = abs(q[0]-p[0])
    dy = abs(p[1]-q[1])

    d = 2 * dy - dx
    x = p[0]
    y = p[1]
    points = []
    points.extend(p)

    while x<=q[0]:
        #draw
        if d <= 0 :
            d = d + 2 * dy
            x += 1
        else :
            d = d + 2 * (dy - dx)
            x += 1
            y += 1
        tp = convert_back(x,y)
        points.extend(tp)
    return points



# User_input
d = int(input("Enter your user ID : "));
ld = d % 10
d /= 10;
pd = int(d % 10)


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()