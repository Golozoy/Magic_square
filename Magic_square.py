from tkinter import *                                                                                                                                                                         
import time
import math
 
WIDTH = 1920
HEIGHT = 1080
CANVAS_MID_X = WIDTH/2
CANVAS_MID_Y = HEIGHT/2
SIDE = WIDTH/40
 
root = Tk()
canvas = Canvas(root, bg="black", height=HEIGHT, width=WIDTH)
canvas.pack()
 
 
def rotate(angle, center):
    global COUNT
    vertices = [
        [CANVAS_MID_X - SIDE, CANVAS_MID_Y - SIDE],
        [CANVAS_MID_X + SIDE, CANVAS_MID_Y - SIDE],
        [CANVAS_MID_X + SIDE, CANVAS_MID_Y + SIDE],
        [CANVAS_MID_X - SIDE, CANVAS_MID_Y + SIDE],
    ]
    angle = math.radians(angle)
    cos_val = math.cos(angle)
    sin_val = math.sin(angle)
    cx, cy = center
    new_points = []
    for x_old, y_old in vertices:
        x_old -= cx
        y_old -= cy
        x_new = x_old * cos_val - y_old * sin_val
        y_new = x_old * sin_val + y_old * cos_val
        new_points.append([x_new + cx, y_new + cy])
    return new_points
 
def draw_square(points, color="red", obj=None):
    canvas.delete(obj)
    obj = canvas.create_polygon(points, fill=color)
    return obj
 
def get_center_square(event):
    global CANVAS_MID_X
    global CANVAS_MID_Y
    CANVAS_MID_X = event.x
    CANVAS_MID_Y = event.y
 
def mouse_wheel(event):
    global SIDE
    if event.num == 5 or event.delta == -120:
        SIDE -= 5
    if event.num == 4 or event.delta == 120:
        SIDE += 5
 
def test_square():
    old_vertices = [[150, 150], [250, 150], [250, 250], [150, 250]]
    print("vertices: ", vertices, "should be: ", old_vertices)
    print(vertices == old_vertices)
 
def test_mouse(event):
    print(event)
    print(event.x, event.y)
 
 
root.bind('<Motion>', get_center_square)    #Постоянное движение за курсором
#root.bind('<Button-1>', get_center_square) #Перемещение по нажатию лкм
 
# Windows
root.bind("<MouseWheel>", mouse_wheel)
 
# Linux
root.bind("<Button-4>", mouse_wheel)
root.bind("<Button-5>", mouse_wheel)
 
gem = None
angle = 0
while True:
    center = (CANVAS_MID_X, CANVAS_MID_Y)
    new_square = rotate(angle, center)
    gem = draw_square(new_square, obj=gem)
    time.sleep(.01)
    root.update()
    angle += 10
mainloop()
