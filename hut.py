from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def draw_lines(x, y,p,q):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_LINES)
    glVertex2f(x,y)
    glVertex2f(p,q)
    glEnd()

def draw_triangle(a,b,c,d,e,f):
    glPointSize(5)  # pixel size. by default 1 thake
    glBegin(GL_TRIANGLES)
    glVertex2f(a,b)
    glVertex2f(c,d)
    glVertex2f(e,f)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    # a=[1,19,234,34,57,400,323,454,56,88,33,454,456,456,565,645,102,204,402,551,651,123]
    # for i in range(0,50):
    #     x=random.choice(a)
    #     y=random.choice(a)
    #     draw_points(x,y)

    draw_lines(100,50,100,300)
    draw_lines(350,50,350,300)
    glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
    draw_triangle(100,300,225,450,350,300)
    draw_lines(350,50,100,50)
    draw_lines(130,250,130,180)
    draw_lines(200,250,200,180)
    draw_lines(130,250,200,250)
    draw_lines(130,180,200,180)


    draw_lines(250,250,250,180)
    draw_lines(320,250,320,180)
    draw_lines(250,250,320,250)
    draw_lines(250,180,320,180)


    draw_lines(200,50,200,140)
    draw_lines(250,50,250,140)
    draw_lines(200,140,250,140)
    draw_points(240,85)

    # draw_points(250, 250)

    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()
