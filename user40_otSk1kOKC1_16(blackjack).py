# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
win = 0
lose = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

    def draw_back(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0] ,CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)

# define hand class

class Hand:
    def __init__(self):
        self.hand = []	# create Hand object
        
    def __str__(self):
        results = ''
        for i in range(len(self.hand)):
            results += str(self.hand[i]) + " " 
        return 'Hand contains ' + results  # return a string representation of a hand

    def add_card(self, card):
        self.hand.append(card) # add a card object to a hand
        
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0
        one_ace = True
        ace_number = 0
        for i in self.hand:
            if i.get_rank() == 'A':
                ace_number += 1
                value += 1
            else:
                value += VALUES[i.get_rank()]
        if ace_number == 0:
            return value
        else:
            if value + 10 <= 21:
                value += 10
            return value
        # compute the value of the hand, see Blackjack video
            
    def draw(self, canvas, pos):
        for i in range(len(self.hand)):
            self.hand[i].draw(canvas, [pos[0] + i * CARD_SIZE[0], pos[1]])
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []	# create a Deck object
        for suit_item in SUITS:
            for rank_numer in RANKS:
                self.deck.append(suit_item + rank_numer)     
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)    # use random.shuffle()

    def deal_card(self):
        for i in self.deck[0]:
            if i in SUITS:
                suit = i
            if i in RANKS:
                rank = i
        result = Card(suit, rank)
        self.deck.remove(suit + rank)
        # deal a card object from the deck
        return result
    def __str__(self):
        results = ""
        for i in range(len(self.deck)):
            results += self.deck[i] + " "
        return 'Deck contains ' + results
        # return a string representing the deck

    
#define event handlers for buttons
def deal():
    global outcome, in_play, deck_card, player , dealer, deck
    
    # your code goes here
    if in_play == False:
        deck = Deck()
        deck_card = deck.shuffle()
        player = Hand()
        player.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
        dealer = Hand()
        dealer.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        in_play = True
        outcome = 'Game start'
    else:
        outcome = 'You lose! New deal?'
        in_play = False
  
        


def hit():
    # replace with your code below
    global in_play, outcome
    # if the hand is in play, hit the player
    if in_play == True:
        if player.get_value() <= 21:
            player.add_card(deck.deal_card())
        else:
            in_play = False
            outcome = 'You have busted. New deal?'
    # if busted, assign a message to outcome, update in_play and score
    if player.get_value() > 21:
        in_play = False
        outcome = 'You have busted. New deal?'
def stand():
    # replace with your code below
    global in_play, outcome
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play == True:
        while dealer.get_value() <= 17:
            dealer.add_card(deck.deal_card())
            print dealer
        if dealer.get_value() > 21:
            outcome = 'Player win! New deal?'
            in_play = False
        else:
            if dealer.get_value() >= player.get_value():
                outcome = 'Dealer win! New deal?' 
                in_play = False
            else:
                outcome = 'Player win! New deal?'
                in_play = False
    else:
        outcome = 'New deal?'
        
            
    # assign a message to outcome, update in_play and score

# draw handler   
def draw(canvas):
    global player, dealer, win, lose
    total_pos = [50, 150]
    text = ('Blackjack' + str(player.get_value()))
    canvas.draw_text('Blackjack' , [total_pos[0], total_pos[1] - 50], 80, 'black')
    canvas.draw_text(outcome, [total_pos[0], total_pos[1] + 20], 40, 'red')
    canvas.draw_text(('Player cards, Score: ' + str(player.get_value())),
                     [total_pos[0], total_pos[1] + 80], 35, 'black')
    if in_play == True:
        canvas.draw_text('Dealer cards',
                          [total_pos[0], total_pos[1] + 280], 35, 'black')
    else:
        canvas.draw_text(('Dealer cards, Score: ' + str(dealer.get_value())),
                          [total_pos[0], total_pos[1] + 280], 35, 'black')
    # test to make sure that card.draw works, replace with your code below
    player.draw(canvas, [total_pos[0], total_pos[1] + 100])
    dealer.draw(canvas, [total_pos[0], total_pos[1] + 300])
    if in_play == True:
        card = Card("S", "5")
        card.draw_back(canvas, [total_pos[0], total_pos[1] + 300])
    
    # win and lose conter
    #canvas.draw_text('wins:'+ str(win),[total_pos[0], total_pos[1] + 80], 30, 'black')
    #canvas.draw_text('lose:'+ str(lose),[total_pos[0], total_pos[1] + 80], 30, 'black')
    #testing card                              
    #card = Card("S", "5")
    #card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric