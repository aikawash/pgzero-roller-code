import subprocess
import yaml
import time

#import pgzrun
#import pgzero
#import pygame

def ticcmd(*args):
  return subprocess.check_output(['ticcmd'] + list(args))

def currentPos(ser):
    status = yaml.safe_load(ticcmd('-d',ser,'-s'))
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

SERIAL1 = '00382275'
SERIAL2 = '00382269'
setPos(SERIAL1,0)
setPos(SERIAL2,0)

currentPos(SERIAL1)
currentPos(SERIAL2)

setTarget(SERIAL1,SERIAL2,500)
