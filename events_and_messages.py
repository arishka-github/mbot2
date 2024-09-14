import cyberpi

PROGRAM_NAME = 'events_and_messages'
PROGRAM_VERSION = '0.1'


@cyberpi.event.start  # Event to be listened to
def callback1():
    cyberpi.led.on("yellow")  # Code to be executed after the event happens
    show_start_info(cyberpi)


@cyberpi.event.is_press('a')
def is_pressed():
    cyberpi.restart()


@cyberpi.event.is_press('b')
def is_pressed():
    cyberpi.broadcast('hello')


@cyberpi.event.is_press('left')
def is_pressed_left():
    cyberpi.broadcast('bye')


@cyberpi.event.receive('hello')  # Event (with a parameter) to be listened to
def callback2():
    cyberpi.led.on("green")  # Code to be executed after the event happens
    cyberpi.console.clear()  # Code to be executed after the event happens
    cyberpi.console.println('hello message received')  # Code to be executed after the event happens


@cyberpi.event.receive('bye')  # Event (with a parameter) to be listened to
def callback3():
    # cyberpi.led.on("blue red green orange cyan")  # Code to be executed after the event happens
    cyberpi.led.on("cyan")  # Code to be executed after the event happens
    cyberpi.console.clear()  # Code to be executed after the event happens
    cyberpi.console.println('bye message received')  # Code to be executed after the event happens


def show_start_info(c: cyberpi):
    # info = ':'.join([PROGRAM_NAME, PROGRAM_VERSION, str(c.get_battery())])
    info = PROGRAM_NAME + ":" + PROGRAM_VERSION + "\nBattery: " + str(c.get_battery())
    # info = f"name:ver={PROGRAM_NAME}:{PROGRAM_VERSION}\nBattery: {str(c.get_battery())}"
    cyberpi.display.show_label(info,16)
    # cyberpi.console.println(cyberpi.get_battery)
    # cyberpi.console.println(cyberpi.get_extra_battery)
    # cyberpi.console.println(cyberpi.get_mac_address)
    # cyberpi.console.println(__name__)
    # cyberpi.console.println(PROGRAM_NAME, PROGRAM_VERSION)
