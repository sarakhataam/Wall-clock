
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

window_height= 800
window_width= 800

t=1000

hour_line=520
min_line=580
second_line=630

angle_m=270
angle_s=270
angle_h=270

t_s=0
t_m=0
t_h=0

s_x =0
m_x=0
h_x=0

s_y=630
m_y=580
h_y=520


def init():
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0,0,0,0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-window_width,window_width,-window_height,window_height,0,1)

    glMatrixMode(GL_MODELVIEW)


def draw_string():
    glLineWidth(2)
    glColor3d(1,1,1)
    glLoadIdentity()
    num=1
    r=630
    for i in range(30,390,+30):
        x=r*sin(i*pi/180)
        y=r*cos(i*pi/180)
        glTranslate(x,y,0)
        glScale(0.2,0.2,1)
        s = str(num)
        s=s.encode()

        for i in s:
            glutStrokeCharacter(GLUT_STROKE_ROMAN,i)

        num+=1
        glLoadIdentity()


def lines(x,y,r,g,b,width):
    glLineWidth(width)
    glColor3d(r,g,b)
    glBegin(GL_LINES)
    glVertex(0,0)
    glVertex(x,y)
    glEnd()

# def state():


def timer(v):

    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)

    global hour_line
    global min_line
    global second_line

    global t_s
    global t_m
    global t_h

    global angle_m
    global angle_s
    global angle_h


    global s_x
    global m_x
    global h_x

    global s_y
    global m_y
    global h_y

    t_s += 1



    if t_s == 60:
        t_m += 1
        m_x = min_line * cos(-angle_m * pi / 180)
        m_y = min_line * sin(-angle_m * pi / 180)
        angle_m = angle_m + 6
        t_s = 0

    else:
        m_x = min_line * cos(-angle_m * pi / 180)
        m_y = min_line * sin(-angle_m * pi / 180)


    s_x = second_line * cos(-angle_s * pi / 180)
    s_y = second_line * sin(-angle_s * pi / 180)
    angle_s = angle_s + 6



    if t_m == 60:
        t_h += 1
        angle_h = angle_h + 30
        h_x = hour_line * cos(-angle_h * pi / 180)
        h_y = hour_line * sin(-angle_h * pi / 180)
        t_m = 0

    else:
        h_x = hour_line * cos(-angle_h * pi / 180)
        h_y = hour_line * sin(-angle_h * pi / 180)

    display()
    glutTimerFunc(t,timer,1)


def display():

    global s_x
    global m_x
    global h_x

    global s_y
    global m_y
    global h_y

    glLineWidth(5)
    glColor3d(1,1,1)
    angle=6
    r=700
    glBegin(GL_LINE_LOOP)
    for i in range(0,360,angle):
        x= r*cos(i*pi/180)
        y= r*sin(i*pi/180)
        glVertex(x,y)
    glEnd()
    # state()
    lines(m_x, m_y, 1, 1, 1, 5)
    lines(h_x, h_y, 1, 1, 1, 10)
    lines(s_x, s_y, 1, 0, 0, 3)


    for i in range(90, 450, 6):
        glLineWidth(1)
        glColor3d(1,1,1)
        x_1 = 700 * cos(i * pi / 180)
        y_1 = 700 * sin(i * pi / 180)
        x_2 = 660 * cos(i * pi / 180)
        y_2 = 660 * sin(i * pi / 180)
        glBegin(GL_LINES)
        glVertex(x_1, y_1)
        glVertex(x_2, y_2)
        glEnd()


    draw_string()
    glLoadIdentity()
    glutSwapBuffers()





def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB |GLUT_DOUBLE)
    glutInitWindowSize(window_height ,window_width)
    glutInitWindowPosition(0,0)
    glutCreateWindow(b'my clock')
    glutDisplayFunc(display)
    glutTimerFunc(t, timer, 1)
    init()
    glutMainLoop()

main()