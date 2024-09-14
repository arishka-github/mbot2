import cyberpi
import time

PROGRAM_NAME = 'test_events5'
PROGRAM_VERSION = '0.5'

def show_start_info(c: cyberpi):
    info = PROGRAM_NAME + ":" + PROGRAM_VERSION + "\nBattery: " + str(c.get_battery())
    cyberpi.display.show_label(info,16)
    
@cyberpi.event.start  # Event to be listened to
def callback():
    cyberpi.led.on("yellow")  # Code to be executed after the event happens
    show_start_info(cyberpi)
    while True:
        cyberpi.console.print(1)
        time.sleep(1)    

@cyberpi.event.start  # Event to be listened to
def callback():
    time.sleep(3)
    cyberpi.display.clear()
    cyberpi.led.on("cyan")  # Code to be executed after the event happens
    cyberpi.console.print('2nd @start after 3s')  
    while True:
        cyberpi.console.print(2)
        time.sleep(1)    

@cyberpi.event.start  # Event to be listened to
def callback():
    time.sleep(6)
    cyberpi.display.clear()
    cyberpi.led.on("blue")  # Code to be executed after the event happens
    cyberpi.console.print('3nd @start after 6s')  
    while True:
        cyberpi.console.print(3)
        time.sleep(1)    

@cyberpi.event.is_press('b')
def callback():
    cyberpi.audio.set_vol(2)
    cyberpi.audio.play_until('sigh')

time_a_pressed = time.time()
cyberpi.console.print('tap: ' + str(time_a_pressed))

@cyberpi.event.is_press('a')
def callback():
    global time_a_pressed
    if (time.time() - time_a_pressed) < 1:
        cyberpi.restart()
    else:
        cyberpi.stop_all()
        time_a_pressed = time.time()