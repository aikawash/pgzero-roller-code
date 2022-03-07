import subprocess
import yaml
import time

import pgzrun
import pgzero
import pygame

def ticcmd(*args):
  return subprocess.check_output(['ticcmd'] + list(args))

def currentPos(ser):
    status = yaml.load(ticcmd('-d',ser,'-s'))
    position = int(status['Current position'])
    
    print(position)
    
    return position

def setPos(ser,pos):
    ticcmd('-d',ser,'--halt-and-set-position',str(pos))
    return

def setTarget(leftser,rightser,tar):
    t1 = time.time()
    t2 = time.time()
    
    #current position of one stepper
    pos = currentPos(leftser)
    
    #calculate the running time based on the speed
    runtime = abs(pos-tar)/300
    
    while ((t2-t1)<runtime):
        ticcmd('-d',leftser,'--exit-safe-start','--position', str(tar))
        ticcmd('-d',rightser,'--exit-safe-start', '--position', str(tar))
        t2 = time.time()
    
    #keep the tension of paper
    ticcmd('-d',leftser,'--exit-safe-start','--position', str(tar+100))
    ticcmd('-d',rightser,'--exit-safe-start','--position', str(tar-100))    
    time.sleep(0.5)
    
    #reset the position
    setPos(leftser,tar)
    setPos(rightser,tar)
    
    return


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
    screen.clear()
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

#SERIAL1 = '00377013' from the first motors
#SERIAL2 = '00376994'

SERIAL1 = '00382277' #top left
SERIAL2 = '00376981' #top right

SERIAL3 = '00377011' #bottom left
SERIAL4 = '00382261' #bottom right

currentPos(SERIAL1)
currentPos(SERIAL2)

setPos(SERIAL1,0)
setPos(SERIAL2,0)


setPos(SERIAL3,0)
setPos(SERIAL4,0)

# 3 is cover, 1 is schools, 2 is render, 4 is team, 5 is construction
 
def on_mouse_down(pos):
    if button1.collidepoint(pos):
        currentPos(SERIAL1)
        currentPos(SERIAL2)
        setTarget(SERIAL1,SERIAL2,700)
        #button 1 is 700

    if button2.collidepoint(pos):
        currentPos(SERIAL1)
        currentPos(SERIAL2)
        setTarget(SERIAL1,SERIAL2,350)

    if button3.collidepoint(pos):
        currentPos(SERIAL1)
        currentPos(SERIAL2)
        setTarget(SERIAL1,SERIAL2,0)

    if button4.collidepoint(pos):
        currentPos(SERIAL1)
        currentPos(SERIAL2)
        setTarget(SERIAL1,SERIAL2,-350)

    if button5.collidepoint(pos):
        currentPos(SERIAL1)
        currentPos(SERIAL2)
        setTarget(SERIAL1,SERIAL2,-700)


 # bottom buttons actions
    if button11.collidepoint(pos):
        currentPos(SERIAL3)
        currentPos(SERIAL4)
        setTarget(SERIAL3,SERIAL4,-850)

    if button22.collidepoint(pos):
        currentPos(SERIAL3)
        currentPos(SERIAL4)
        setTarget(SERIAL3,SERIAL4,-500)

    if button33.collidepoint(pos):
        currentPos(SERIAL3)
        currentPos(SERIAL4)
        setTarget(SERIAL3,SERIAL4,0)

    if button44.collidepoint(pos):
        currentPos(SERIAL3)
        currentPos(SERIAL4)
        setTarget(SERIAL3,SERIAL4,400)

    if button55.collidepoint(pos):
        currentPos(SERIAL3)
        currentPos(SERIAL4)
        setTarget(SERIAL3,SERIAL4,850)
        #button 1 is 700         


pgzrun.go()

#from -3000 to 3000       
#SERIAL1 = '00377013'
#SERIAL2 = '00376994'
#setTarget(SERIAL1,SERIAL2,0)