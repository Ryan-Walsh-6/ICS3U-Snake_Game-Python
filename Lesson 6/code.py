#!/usr/bin/env python3

# Created by: Ryan Walsh
# Created on: January 2020
# This program is the "The Snake Game" program on the PyBadge

import ugame
import stage
import constants


def menu_scene():
    # this function is the menu scene

    # image banks for CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # add text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None, 
    palette=constants.RED_PALETTE, buffer=None)
    text1.move(20,10)
    text1.text("The Snake Game")
    text.append(text1)
    
    text2 = stage.Text(width=29, height=12, font=None, 
    palette=constants.RED_PALETTE, buffer=None)
    text2.move(40,110)
    text2.text("PRESS START")
    text.append(text2)

    # sets the background to image 0 in the image bank
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X,
                            constants.SCREEN_Y)

    # create a stage for the background to show up on
    #    and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and initial location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # Start button selected
        if keys & ugame.K_START != 0:
            game_scene()

        # update game logic
        game.tick() # wait until refresh rate finishes

def game_scene():
   # this function is the main game game_scene
   
   # image banks for CircuitPython
   image_bank_bankground = stage.Bank.from_bmp16("ball.bmp")
   image_bank_sprites = stage.Bank.from_bmp16("PyBadge_bank_color_template.bmp")
   
   # set the background to image 0 in the image Bank
   #   and the size (10x8 tiles of the size 16x16)
   background = stage.Grid(image_bank_bankground, constants.SCREEN_GRID_X ,constants.SCREEN_GRID_Y)
   
   # a sprite that will be updated every frame
   snakes = []
   a_single_snake = stage.Sprite(image_bank_sprites, 11, constants.OFF_SCREEN_X,constants.OFF_SCREEN_Y)
   snakes.append(a_single_snake)
   snakes[constants.HEAD_INDEX].move(constants.SCREEN_X/2,constants.SCREEN_Y/2)
   # an apple sprite that will be updated every frame
   apple = stage.Sprite(image_bank_sprites, 8 , constants.OFF_SCREEN_X,
                                     constants.OFF_SCREEN_Y)
   #place apple on the screen
   apple.move(constants.SCREEN_X/2 + constants.APPLE_OFFSET,constants.SCREEN_Y/2 -constants.APPLE_OFFSET) 
    # create a stage for the background to show up on
   #   and set the frame rate for 5fps
   game = stage.Stage(ugame.display, constants.GAME_FPS)
   # set layers of all sprites, items show up in order
   game.layers = snakes + [apple] + [background]
   # render all sprites
   #   most likely you will only render the background once per game scene
   game.render_block()
   wormCoords = [{'x': snakes[constants.HEAD_INDEX].x , 'y': snakes[constants.HEAD_INDEX].y}]
   newHead = {'x':snakes[constants.HEAD_INDEX].x, 'y' :snakes[constants.HEAD_INDEX].y}
    # repeat forever, game loop
   while True:
       # get user input
       keys = ugame.buttons.get_pressed()
       # update game logic
       if keys & ugame.K_X:
           pass
       if keys & ugame.K_O:
           pass
       if keys & ugame.K_START:
           pass
       if keys & ugame.K_SELECT:
           pass
       if keys & ugame.K_RIGHT:
           newHead = {'x':snakes[constants.HEAD_INDEX].x + constants.SPRITE_SIZE, 'y' :snakes[constants.HEAD_INDEX].y}
       if keys & ugame.K_LEFT:
           newHead = {'x':snakes[constants.HEAD_INDEX].x - constants.SPRITE_SIZE, 'y' :snakes[constants.HEAD_INDEX].y}
       if keys & ugame.K_UP:
           newHead = {'x':snakes[constants.HEAD_INDEX].x, 'y' :snakes[constants.HEAD_INDEX].y - constants.SPRITE_SIZE}
       if keys & ugame.K_DOWN:
           pass
           newHead = {'x':snakes[constants.HEAD_INDEX].x, 'y' :snakes[constants.HEAD_INDEX].y + constants.SPRITE_SIZE}
       wormCoords.insert(0,newHead)
       del wormCoords[-1]
       for snake_number in range (len(snakes)):
           snakes[snake_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
       #Re-draw snake
       for coords in wormCoords:
           x= coords['x']
           y= coords['y']
           if snakes[snake_number].x < 0:
               snakes[snake_number].move(x,y)
       
       # redraw Sprite
       game.render_sprites(snakes + [apple])
       game.tick() # wait until refresh rate finishes

if __name__ == "__main__":
    menu_scene()
