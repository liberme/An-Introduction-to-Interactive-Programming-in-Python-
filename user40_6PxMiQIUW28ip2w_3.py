# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global card_list, exposed, state, card_check1, card_check2, counter
    state = 0
    counter = 0
    card_check1 = 0
    card_check2 = 0
    label.set_text("Turns = 0")
    card_list = range(0,8) * 2
    random.shuffle(card_list)
    exposed = [False] * 16
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, card_check1, card_check2, counter
    if state == 0: #first game
        for number in range(len(card_list)):
            if pos[0] // 50 == number and exposed[number] == False: # position and expose detected
                exposed[number] = True 
                counter += 1
                card_check1 = number
        state = 1
    elif state == 1:
        for number in range(len(card_list)):
            if pos[0] // 50 == number and exposed[number] == False: # position and expose detected
                exposed[number] = True
                card_check2 = number # memorize card picked
                counter += 1
        state = 2
    else:
        # Checker for pair and unpair and fix or flip
        if card_list[card_check1] == card_list[card_check2]: # if pair set True
            exposed[card_check1] = True # fix card
            exposed[card_check2] = True # fix card
        else:
            # when two unpair card exposed , player click on exposed card , prevent only flip one card
            for number in range(len(card_list)):
                if pos[0] // 50 == number and exposed[number] == False: # position and expose detected
                    exposed[card_check1] = False # flip card
                    exposed[card_check2] = False # flip card
            card_edge = 0
        for number in range(len(card_list)):
            if pos[0] // 50 == number and exposed[number] == False:# position and expose detected
                exposed[number] = True
                card_check1 = number # memorize card picked
                counter += 1
        state = 1
    # update information about game turn    
    Turns = 'Turns = ' + str(counter // 2)
    label.set_text(Turns) 

# cards are logically 50x100 pixels in size    
def draw(canvas):
    start_point = 10 # make text align center
    # check whether card filp or not
    for number in range(len(card_list)):
        pos = 50 * number
        if exposed[number] == True: 
            canvas.draw_text(str(card_list[number]),(start_point + pos , 70), 50 , 'white')
        else:
            canvas.draw_polygon([(pos , 0), (pos , 100), (50 + pos , 100), (50 + pos , 0)], 3, 'black','green')
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")
 

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric