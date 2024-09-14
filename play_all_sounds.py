import event, time, os
import cyberpi as cbp

sounds = ['hello', 'up', 'down', 'left', 'right', 'hello', 'hi', 'bye', 'yeah', 'wow', 'laugh', 'hum', 'sad', 'sigh',
          'annoyed', 'angry', 'surprised', 'yummy', 'curious', 'embarrassed', 'ready', 'sprint', 'sleepy', 'meow',
          'hurt', 'start', 'switch', 'beeps', 'buzzing', 'exhaust', 'explosion', 'gotcha', 'jump', 'laser', 'level-up',
          'low-energy', 'prompt-tone', 'prompt-tone-up', 'prompt-tone-down', 'right', 'wrong', 'ring', 'score',
          'step-1', 'step-2', 'wake', 'warning', 'radar', 'metal-clash', 'shot-1', 'shot-2', 'glass-clink', 'inflator',
          'running water', 'clockwork', 'click', 'bell', 'current', 'switch', 'wood-hit-1', 'wood-hit-2', 'wood-hit-3',
          'wood-hit-4', 'wood-hit-5', 'iron-1', 'iron-2', 'buckle', 'coin', 'drop', 'bubble-1', 'bubble-2',
          'wine-bottle-open', 'wave', 'magic', 'spitfire', 'heartbeat', 'load', 'black', 'red', 'orange', 'yellow',
          'green', 'cyan', 'blue', 'purple', 'gray', 'white', 'brown', 'pink', 'sunny', 'rainy', 'cloudy', 'windy',
          'snowy', 'foggy', 'yes', 'no', 'ok', 'good', 'thank you', 'cm', 'inch', 'celsius', 'fahrenheit', 'pct']

# print(len(sounds))

# stop_all = False

pause = False
led_pause = 'yellow red yellow red yellow'
led_running = 'cyan green cyan green cyan'


@event.is_press('a')
def is_btn_press_a():
    cbp.console.clear()
    # stop_all = True


@event.is_press('b')
def is_btn_press_b():
    global pause
    pause = not pause
    if pause:
        cbp.led.show(led_pause)
    else:
        cbp.led.show(led_running)


@event.start
def on_start():
    cbp.led.show(led_running)
    cbp.console.clear()
    cbp.audio.set_vol(10)
    # global pause
    for s in sounds:
        while pause:
            time.sleep(0.5)  # wait for unpause

        # if stop_all: break
        t = time.time()
        cbp.console.print('... ')
        cbp.audio.play_until(s)
        if (time.time() - t > 0.4):
            cbp.console.println(s)
        else:
            sounds.remove(s)
            cbp.console.println(' ---')
        time.sleep(0.5)
    cbp.console.print('total sounds:' + str(len(sounds)))
    cbp.led.show('red red red red red')


