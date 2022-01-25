from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


class Timer:

    def __init__(self):
        self.startTime = time.time()

    def getCurrentTime(self):
        return "{:.2f}".format(time.time() - self.startTime)

    def reset(self):
        self.startTime = time.time()


def update():
    if active_tag.visible:
        elapsed_time = float(timerLabel.text[16:])
        if elapsed_time == 0.0:
            runtimer.reset()
            time.sleep(0.01)
        timerLabel.text = "Time in seconds: " + runtimer.getCurrentTime()

    if player.x > 241:
        reset_timer()

    if 10 < player.x < 11 and not active_tag.visible:
        timerLabel.text = "Time in seconds: " + str(0.0)
        active_tag.visible = True


def reset_timer():
    active_tag.visible = False


def input(key):
    if key == 'left mouse down':
        if active_tag.visible:
            reset_timer()
        else:
            timerLabel.text = "Time in seconds: " + str(0.0)
            active_tag.visible = True


app = Ursina()

Sky()
player = FirstPersonController(y=2, origin_y=-.5, speed=7, height=3)
ground = Entity(model='plane', scale=(300, 1, 30), position=(125, 0, 0), color=color.lime, texture="white_cube",
                texture_scale=(100, 100), collider='box')

left_wall = Entity(model='cube', collider='box', position=(125, 0, 15), scale=(300, 5, 1), rotation=(0, 0, 0),
                   texture='brick', texture_scale=(5, 5), color=color.rgb(255, 128, 0))
right_wall = duplicate(left_wall, z=-15)
back_wall = Entity(model='cube', collider='box', position=(-25, 0, 0), scale=(1, 5, 30), rotation=(0, 0, 0),
                   texture='brick', texture_scale=(5, 5), color=color.rgb(255, 128, 0))
front_wall = duplicate(back_wall, x=275)

hurdle_low = Entity(model='cube', collider='box', position=(10, 0, 0), scale=(1, 2, 25), rotation=(0, 0, 0),
                    texture='brick', texture_scale=(5, 5), color=color.rgb(255, 255, 0))
hurdle_medium = Entity(model='cube', collider='box', position=(30, 0, 0), scale=(1, 3, 25), rotation=(0, 0, 0),
                       texture='brick', texture_scale=(5, 5), color=color.rgb(255, 165, 155))
hurdle_high = Entity(model='cube', collider='box', position=(50, 0, 0), scale=(1, 4, 25), rotation=(0, 0, 0),
                     texture='brick', texture_scale=(5, 5), color=color.rgb(255, 55, 0))
hurdle_3 = duplicate(hurdle_low, x=70)
hurdle_4 = duplicate(hurdle_low, x=75)
hurdle_5 = duplicate(hurdle_low, x=80)
hurdle_6 = duplicate(hurdle_high, x=100)
hurdle_7 = duplicate(hurdle_medium, x=120)
hurdle_8 = duplicate(hurdle_high, x=140)
hurdle_9 = duplicate(hurdle_medium, x=155)
hurdle_10 = duplicate(hurdle_medium, x=175)
hurdle_11 = duplicate(hurdle_medium, x=190)
hurdle_12 = duplicate(hurdle_low, x=210)
hurdle_13 = duplicate(hurdle_medium, x=225)
hurdle_14 = duplicate(hurdle_high, x=240)

window.title = 'Best Horse EUWest'  # The window title
window.borderless = False  # Show a border
window.fullscreen = False  # Do not go Fullscreen
window.exit_button.visible = False  # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True

Text.size = 0.03
Text.default_resolution = 1080 * Text.size
timerLabel = Text(text="Time in seconds: " + str(0.0))
timerLabel.x = -0.7
timerLabel.y = 0.45
timerLabel.background = False
timerLabel.visible = True
active_tag = Text(text="Timer active")
active_tag.x = -0.3
active_tag.y = 0.45
active_tag.color = rgb(0, 255, 0)
active_tag.background = True
active_tag.visible = False

runtimer = Timer()

app.run()
