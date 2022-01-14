from ursina import *
from random import uniform
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

Sky()
player = FirstPersonController(y=2, origin_y=-.5)
ground = Entity(model='plane', scale=(100, 1, 100), color=color.lime, texture="white_cube", texture_scale=(100, 100), collider='box')

wall_1 = Entity(model='cube', collider='box', position=(-8, 0, 0), scale=(8, 2, 1), rotation=(0, 0, 0), texture='brick', texture_scale=(5, 5), color=color.rgb(255, 128, 0))
wall_2 = duplicate(wall_1, z=5)
wall_3 = duplicate(wall_1, z=10)
wall_4 = Entity(model='cube', collider='box', position=(-15, 0, 10), scale=(1, 2, 20), rotation=(0, 0, 0), texture='brick', texture_scale=(5, 5), color=color.rgb(255, 128, 0))


window.title = 'Best Horse EUWest'                # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen
window.exit_button.visible = False      # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True

# def update():   # update gets automatically called.
#     player.x += held_keys['d'] * .1
#     player.x -= held_keys['a'] * .1
#     player.z += held_keys['w'] * .1
#     player.z -= held_keys['s'] * .1

app.run()