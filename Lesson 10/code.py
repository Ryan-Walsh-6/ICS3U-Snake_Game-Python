#!/usr/bin/env python3

# Created by: Ryan Walsh
# Created on: January 2020
# This program is the "The Snake Game" program on the PyBadge

import ugame
import stage
import random
import time
import neopixel
import board
import supervisor

import constants

def splash_scene():
    # this function is the splash scene

    # get sound ready
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    # image banks for CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    # sets the background to image 0 in the image bank
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X,
                            constants.SCREEN_Y)

    # used this program to split the image into tile:
    #    https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white


    # create a stage for the background to show up on
    #    and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = [background]
    # render the background and initial location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # Wait for 2 seconds
        time.sleep(2.0)
        menu_scene()

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
   def show_apple():
       apple.move(random.randint(0 + 
               constants.SNAKE_SIZE,constants.SCREEN_X - 
               constants.SNAKE_SIZE),(random.randint(0 + 
               constants.SNAKE_SIZE,constants.SCREEN_Y - 
               constants.SNAKE_SIZE)))
    
   def show_snake(x , y):
        # this function takes a snake from off screen and moves it on screen
       for snake_number in range(len(snakes)):
           if snakes[snake_number].x < 0:
               snakes[snake_number].move(x,y)
               break
   
   # get sound ready
   apple_crunch = open("apple_crunch.wav", 'rb')
   sound = ugame.audio
   sound.stop()
   sound.mute(False)
   
   neopixels = neopixel.NeoPixel(board.NEOPIXEL, constants.NEOPIXEL_COUNT, 
                                 auto_write=False)
   # for score
   score = 0

   score_text = stage.Text(width=29, height=14)
   score_text.clear()
   score_text.cursor(0,0)
   score_text.move(1,1)
   score_text.text("Score: {0}".format(score))
    
   # image banks for CircuitPython
   image_bank_bankground = stage.Bank.from_bmp16("ball.bmp")
   image_bank_sprites = stage.Bank.from_bmp16("PyBadge_bank_color_template.bmp")
   
   # set the background to image 0 in the image Bank
   #   and the size (10x8 tiles of the size 16x16)
   background = stage.Grid(image_bank_bankground, 10,8)
   
   # a snake sprite that will be updated every frame
   snakes = []
   for snake_number in range(constants.MAX_SCORE):
       a_single_snake = stage.Sprite(image_bank_sprites, 11, 
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
       snakes.append(a_single_snake)
   #place 1 snake on the screen
   x = constants.SCREEN_X/2
   y = constants.SCREEN_Y/2
   show_snake(x, y)

   # an apple sprite that will be updated every frame
   apple = stage.Sprite(image_bank_sprites, 8 , constants.OFF_SCREEN_X,
                                     constants.OFF_SCREEN_Y)
   #place apple on the screen
   apple.move(constants.SCREEN_X/2 + 32,constants.SCREEN_Y/2 -32 ) 
 
   # create a stage for the background to show up on
   #   and set the frame rate for 5fps
   game = stage.Stage(ugame.display, 5)
   # set layers of all sprites, items show up in order
   game.layers = [score_text] + snakes + [apple] + [background]
   # render all sprites
   #   most likely you will only render the background once per game scene
   game.render_block()
   #define initial values for the main loop
   right_button = constants.button_state["button_up"]
   left_button = constants.button_state["button_up"]
   up_button = constants.button_state["button_up"]
   down_button = constants.button_state["button_up"]
   HEAD = 0
   wormCoords = [{'x': snakes[HEAD].x , 'y': snakes[HEAD].y}]
   newHead = {'x':snakes[HEAD].x, 'y' :snakes[HEAD].y}
   collision = False

   # repeat forever, game loop
   while True:
       # get user input
       keys = ugame.buttons.get_pressed()
      
       if keys & ugame.K_RIGHT !=0:
           right_button = constants.button_state["button_just_pressed"]
           left_button = constants.button_state["button_up"]
           up_button = constants.button_state["button_up"]
           down_button = constants.button_state["button_up"]
       elif keys & ugame.K_LEFT !=0:
           right_button = constants.button_state["button_up"]
           left_button = constants.button_state["button_just_pressed"]
           up_button = constants.button_state["button_up"]
           down_button = constants.button_state["button_up"]
       elif keys & ugame.K_UP !=0:
           right_button = constants.button_state["button_up"]
           left_button = constants.button_state["button_up"]
           up_button = constants.button_state["button_just_pressed"]
           down_button = constants.button_state["button_up"]
       elif keys & ugame.K_DOWN !=0:
           right_button = constants.button_state["button_up"]
           left_button = constants.button_state["button_up"]
           up_button = constants.button_state["button_up"]
           down_button = constants.button_state["button_just_pressed"]

       if keys & ugame.K_X:
           pass
       if keys & ugame.K_O:
           pass
       if keys & ugame.K_START:
           pass
       if keys & ugame.K_SELECT:
           pass
        #set neopixels to blue by default
       neopixels[0] = (0, 0, 10)
       neopixels[1] = (0, 0, 10)
       neopixels[2] = (0, 0, 10)
       neopixels[3] = (0, 0, 10)
       neopixels[4] = (0, 0, 10) 
      
       if stage.collide(snakes[HEAD].x , snakes[HEAD].y,
                        snakes[HEAD].x + 15, snakes[HEAD].y + 15, 
                        apple.x, apple.y,
                        apple.x + 15, apple.y + 15):
           neopixels[0] = (10, 10, 0)
           neopixels[1] = (10, 10, 0)
           neopixels[2] = (10, 10, 0)
           neopixels[3] = (10, 10, 0)
           neopixels[4] = (10, 10, 0)
           neopixels.show()
           time.sleep(0.1)
           
           neopixels[0] = (0, 0, 10)
           neopixels[1] = (0, 0, 10)
           neopixels[2] = (0, 0, 10)
           neopixels[3] = (0, 0, 10)
           neopixels[4] = (0, 0, 10)
   
           sound.stop()
           sound.play(apple_crunch)
           # you hit an apple
           score = score + 1
           score_text.clear()
           score_text.cursor(0,0)
           score_text.move(1,1)
           score_text.text("Score: {0}".format(score))

           apple.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
           #place apple in new location
           show_apple()
           if right_button == constants.button_state["button_just_pressed"] :
               newHead = {'x':snakes[HEAD].x +16, 'y' :snakes[HEAD].y}
           elif left_button == constants.button_state["button_just_pressed"] :
               newHead = {'x':snakes[HEAD].x - 16, 'y' :snakes[HEAD].y}
           elif up_button == constants.button_state["button_just_pressed"] :
               newHead = {'x':snakes[HEAD].x, 'y' :snakes[HEAD].y - 16}
           elif down_button == constants.button_state["button_just_pressed"] :
               newHead = {'x':snakes[HEAD].x, 'y' :snakes[HEAD].y + 16}
           wormCoords.insert(0,newHead)
       else:        
           if right_button == constants.button_state["button_just_pressed"] :
               newHead = {'x':snakes[HEAD].x +16, 'y' :snakes[HEAD].y}
           elif left_button == constants.button_state["button_just_pressed"] :
               newHead = {'x':snakes[HEAD].x - 16, 'y' :snakes[HEAD].y}
           elif up_button == constants.button_state["button_just_pressed"] :
               newHead = {'x':snakes[HEAD].x, 'y' :snakes[HEAD].y - 16}
           elif down_button == constants.button_state["button_just_pressed"] :
               newHead = {'x':snakes[HEAD].x, 'y' :snakes[HEAD].y + 16}
           wormCoords.insert(0,newHead)
           del wormCoords[-1]
       
       #Move all snakes off screen
       for snake_number in range (len(snakes)):
           snakes[snake_number].move(constants.OFF_SCREEN_X,
                                     constants.OFF_SCREEN_Y)
       #Re-draw snake
       for coords in wormCoords:
           x= coords['x']
           y= coords['y']
           show_snake(x,y)

       #Check for off-screen
       if snakes[HEAD].x > (constants.SCREEN_X - constants.SNAKE_SIZE):
            collision = True
       for coords in wormCoords:
           x= coords['x']
           if x < 0 :
                collision = True
       if snakes[HEAD].y <  0:
                collision = True
       if snakes[HEAD].y > (constants.SCREEN_Y - constants.SNAKE_SIZE):
                collision = True
       

       #Check for the snake collision with itself
       for snake_number in range (1,len(snakes)):
           if snakes[snake_number].x > 0:
                       if stage.collide(snakes[HEAD].x , 
                                        snakes[HEAD].y,
                                        snakes[HEAD].x + 15,
                                        snakes[HEAD].y + 15,
                                        snakes[snake_number].x ,
                                        snakes[snake_number].y,
                                        snakes[snake_number].x + 15,
                                        snakes[snake_number].y + 15):
                           collision = True
       
       if collision == True:
           neopixels[0] = (10, 0, 0)
           neopixels[1] = (10, 0, 0)
           neopixels[2] = (10, 0, 0)
           neopixels[3] = (10, 0, 0)
           neopixels[4] = (10, 0, 0)
           neopixels.show()
           time.sleep(0.5)
           you_lost_scene(score)      

       if score == constants.MAX_SCORE:
           for i in range(score):
               neopixels[0] = (0, 10, 0)
               neopixels[1] = (0, 10, 0)
               neopixels[2] = (0, 10, 0)
               neopixels[3] = (0, 10, 0)
               neopixels[4] = (0, 10, 0)
               neopixels.show()
               time.sleep(0.1)
               neopixels[0] = (0, 0, 0)
               neopixels[1] = (0, 0, 0)
               neopixels[2] = (0, 0, 0)
               neopixels[3] = (0, 0, 0)
               neopixels[4] = (0, 0, 0)
               neopixels.show()
               time.sleep(0.1)
           neopixels[0] = (0, 10, 0)
           neopixels[1] = (0, 10, 0)
           neopixels[2] = (0, 10, 0)
           neopixels[3] = (0, 10, 0)
           neopixels[4] = (0, 10, 0)
           neopixels.show()
           time.sleep(0.5)
           you_won_scene(score)
       # redraw Sprite
       neopixels.show()
       game.render_sprites(snakes + [apple])
       game.tick() # wait until refresh rate finishes

def you_won_scene(score):
    # turn off sound from last scene
   sound = ugame.audio
   sound.stop()
   # image banks for Circuitpython
   image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")
           
   # sets the background to image 0 in the image bank
   background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X,
                                    constants.SCREEN_GRID_Y)
    
   text = []
   text1 = stage.Text(width=29, height=14, font=None,
   palette=constants.BLUE_PALETTE, buffer=None)
   text1.move(43,60)
   text1.text("YOU WIN!")
   text.append(text1)

   # create a stage for the background to show up on
   #     ad set the frame rate to 60fps
   game = stage.Stage(ugame.display, constants.FPS)
   # set layers of all sprites, items show up in order
   game.layers = text + [background]
   # render all sprites
   #   most likely you will only render the background once per game scene
   game.render_block()
   time.sleep(3.0)
   game_over_scene(score)

def you_lost_scene(score):
    # turn off sound from last scene
   sound = ugame.audio
   sound.stop()
   # image banks for Circuitpython
   image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")
           
   # sets the background to image 0 in the image bank
   background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X,
                                    constants.SCREEN_GRID_Y)
       
   text = []
   text1 = stage.Text(width=29, height=14, font=None,
   palette=constants.BLUE_PALETTE, buffer=None)
   text1.move(43,60)
   text1.text("YOU LOSE :(")
   text.append(text1)

   # create a stage for the background to show up on
   #     ad set the frame rate to 60fps
   game = stage.Stage(ugame.display, constants.FPS)
   # set layers of all sprites, items show up in order
   game.layers = text + [background]
   # render all sprites
   #   most likely you will only render the background once per game scene
   game.render_block()
   time.sleep(3.0)
   game_over_scene(score)

def game_over_scene(final_score):
    # this function is the game over scene
           
   # turn off sound from last scene
   sound = ugame.audio
   sound.stop()
           
   # image banks for Circuitpython
   image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")
           
   # sets the background to image 0 in the image bank
   background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X,
                                    constants.SCREEN_GRID_Y)
            
   # add text objects
   text = []
   text1 = stage.Text(width=29, height=14, font=None,
   palette=constants.BLUE_PALETTE, buffer=None)
   text1.move(22,20)
   text1.text("Final Score: {:0>2d}".format(final_score))
   text.append(text1)
           
   text2 = stage.Text(width=29, height=14, font=None, 
                      palette=constants.BLUE_PALETTE, buffer=None) 
   text2.move(43,60)
   text2.text("GAME OVER")
   text.append(text2)
           
   text3 = stage.Text(width=29, height=14, font=None, 
                      palette=constants.BLUE_PALETTE, buffer=None)
   text3.move(32,110)
   text3.text("PRESS SELECT")
   text.append(text3)
   # create a stage for the background to show up on
   #     ad set the frame rate to 60fps
   game = stage.Stage(ugame.display, constants.FPS)
   # set layers of all sprites, items show up in order
   game.layers = text + [background]
   # render all sprites
   #   most likely you will only render the background once per game scene
   game.render_block()
           
   # repeat forever, game loop
   while True:
       # get user input
       keys = ugame.buttons.get_pressed()
                
       # Start button selecte
       if keys & ugame.K_SELECT !=0:
           supervisor.reload()
                
           # update game logic
       game.tick() #  wait until refresh rate finishes

if __name__ == "__main__":
    splash_scene()
