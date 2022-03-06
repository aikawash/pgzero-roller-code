import pgzrun
import pgzero
import pygame

#top row buttons

button1 = Actor('1button')
button1.pos = 192, 270 
button2 = Actor('2button')
button2.pos = 400, 270

button3 = Actor('3button')
button3.pos = 576, 270

button4 = Actor('4button')
button4.pos = 768, 270

button5 = Actor('5button')
button5.pos = 960, 270

#bottom row buttons

button11 = Actor('11button')
button11.pos = 192, 810

button22 = Actor('22button')
button22.pos = 384, 810

button33 = Actor('33button')
button33.pos = 576, 810

button44 = Actor('44button')
button44.pos = 768, 810

button55 = Actor('55button')
button55.pos = 960, 810

WIDTH = 1920
HEIGHT = 1080


def draw():
    screen.fill((245, 102, 0))
    button1.draw()
    button2.draw()
    button3.draw()
    button4.draw()
    button5.draw()

    button11.draw()
    button22.draw()
    button33.draw()
    button44.draw()
    button55.draw()

# top buttons action

def on_mouse_down(pos):
    if button1.collidepoint(pos):
        print("pp1")
    if button2.collidepoint(pos):
        print("pp2")
    if button3.collidepoint(pos):
        print("pp3")
    if button4.collidepoint(pos):
        print("pp3")
    if button5.collidepoint(pos):
        print("pp5")
 # bottom buttons actions
    if button11.collidepoint(pos):
        print("pp11")
    if button22.collidepoint(pos):
        print("pp22")
    if button33.collidepoint(pos):
        print("pp33")
    if button44.collidepoint(pos):
        print("pp44")
    if button55.collidepoint(pos):
        print("pp55")       



    


    
    #screen.clear()

pgzrun.go()