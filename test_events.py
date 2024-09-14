import cyberpi

PROGRAM_NAME = 'test_events'
PROGRAM_VERSION = '0.1'

def show_start_info(c: cyberpi):
    info = PROGRAM_NAME + ":" + PROGRAM_VERSION + "\nBattery: " + str(c.get_battery())
    cyberpi.display.show_label(info,16)
    
@cyberpi.event.start  # Event to be listened to
def callback():
    cyberpi.led.on("yellow")  # Code to be executed after the event happens
    show_start_info(cyberpi)