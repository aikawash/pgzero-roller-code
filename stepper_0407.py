import subprocess
import yaml
import time

def ticcmd(*args):
    """ send the command to the controller
    
    Parameters:
        args -- tic command
    Precondition:
        the control mode of stepper controller is Serial/I2C/USB
    """ 
    return subprocess.check_output(['ticcmd'] + list(args))

def currentPos(ser):
    """ Get and print current position of the stepper

    Parameters:
        ser -- stepper controller id
    """
    status = yaml.load(ticcmd('-d',ser,'-s'))
    position = int(status['Current position'])
    print(position)
    
    return position

def setPos(ser,pos):
    """ Set the position of stepper
    
    Parameters:
        ser -- stepper controller id
        pos -- new position for this stepper
    """
    ticcmd('-d',ser,'--halt-and-set-position',str(pos))
    return

def deenergize(ser):
    ticcmd('-d',ser,'--deenergize')
    return

def energize(ser):
    ticcmd('-d',ser,'--energize')
    return

def setCurrent(ser, cur):
    ticcmd('-d',ser,'--position', str(cur))
    return

def setTarget(leftser,rightser,tar):
    """ Roll paper to the target
    
    Parameters:
        leftser -- left side stepper controller id
        rightser -- right side stepper controller id
        tar -- target of the paper roll, from -3000 to 3000
    Precondition:
        Set the current limit to 1092mA
        Set the stepper speed to 200, not sure, need check...
        Before the first time call this function, manually move the paper roll 
        to the original point and set two stepper's position to 0
    """
    t1 = time.time()
    t2 = time.time()
    
    #energize steppers
    energize(leftser)
    energize(rightser)
    
    #current position of one stepper
    pos = currentPos(leftser)
    
    #calculate the running time based on the speed
    runtime = abs(pos-tar)/190
    
    while ((t2-t1)<runtime):
        ticcmd('-d',leftser,'--exit-safe-start','--position', str(tar))
        ticcmd('-d',rightser,'--exit-safe-start', '--position', str(tar))
        t2 = time.time()
    
    #keep the tension of paper
    ticcmd('-d',leftser,'--exit-safe-start','--position', str(tar-15))
    ticcmd('-d',rightser,'--exit-safe-start','--position', str(tar+15))  
    time.sleep(0.5)
    
    #reset the position
    setPos(leftser,tar)
    setPos(rightser,tar)
    
    #deenergize steppers
    deenergize(leftser)
    deenergize(rightser)
    
    return


#module 1
SERIAL1 = '00382280'
SERIAL2 = '00379284'
SERIAL3 = '00382262'
SERIAL4 = '00379317'

#module 2
SERIAL5 = '00382274'
SERIAL6 = '00382272'
SERIAL7 = '00379299'
SERIAL8 = '00379323'

#module 3
SERIAL9 = '00382278'
SERIAL10= '00382271'
SERIAL11= '00382276'
SERIAL12= '00382279'

#module 4
SERIAL13= '00382277'
SERIAL14= '00376981'
SERIAL15= '00377011'
SERIAL16= '00382261'

#module 5
SERIAL17= '00377013'
SERIAL18= '00376994'
SERIAL19= '00379318'
SERIAL20= '00382281'

#module 6
SERIAL21= '00382264'
SERIAL22= '00382270'
SERIAL23= '00382282'
SERIAL24= '00382283'


#setPos(SERIAL9,0)
#setPos(SERIAL10,0)

#setTarget(SERIAL17,SERIAL18,0)
#setTarget(SERIAL20,SERIAL19,0)