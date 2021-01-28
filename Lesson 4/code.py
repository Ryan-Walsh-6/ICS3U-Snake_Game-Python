#!/usr/bin/env python3

# Created by: Ryan Walsh
# Created on: January 2020
# This program is the "The Snake Game" program on the PyBadge

import ugame
import stage
import constants

def game_scene():
   # this function is the main game game_scene
   
   # image banks for CircuitPython
   image_bank_bankground = stage.Bank.from_bmp16("ball.bmp")
   image_bank_sprites = stage.Bank.from_bmp16("PyBadge_bank_color_template.bmp")
   
   # set the background to image 0 in the image Bank
   #   and the size (10x8 tiles of the size 16x16)
   background = stage.Grid(image_bank_bankground, 10,8)
   
   # a sprite that will be updated every frame
   snakes = []
   a_single_snake = stage.Sprite(image_bank_sprites, 11, 75, 66)
   snakes.append(a_single_snake)
    # create a stage for the background to show up on
   #   and set the frame rate for 5fps
   game = stage.Stage(ugame.display, 5)
   # set layers of all sprites, items show up in order
   game.layers = snakes + [background]
   # render all sprites
   #   most likely you will only render the background once per game scene
   game.render_block()
   HEAD = 0
   wormCoords = [{'x': snakes[HEAD].x , 'y': snakes[HEAD].y}]
   newHead = {'x':snakes[HEAD].x, 'y' :snakes[HEAD].y}
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
           newHead = {'x':snakes[HEAD].x +16, 'y' :snakes[HEAD].y}
       if keys & ugame.K_LEFT:
           newHead = {'x':snakes[HEAD].x - 16, 'y' :snakes[HEAD].y}
       if keys & ugame.K_UP:
           newHead = {'x':snakes[HEAD].x, 'y' :snakes[HEAD].y - 16}
       if keys & ugame.K_DOWN:
           newHead = {'x':snakes[HEAD].x, 'y' :snakes[HEAD].y + 16}
       wormCoords.insert(0,newHead)
       del wormCoords[-1]
       for snake_number in range (len(snakes)):
           snakes[snake_number].move(-100, -100)
       #Re-draw snake
       for coords in wormCoords:
           x= coords['x']
           y= coords['y']
           if snakes[snake_number].x < 0:
               snakes[snake_number].move(x,y)
       
       # redraw Sprite
       game.render_sprites(snakes)
       game.tick() # wait until refresh rate finishes

if __name__ == "__main__":
    game_scene()