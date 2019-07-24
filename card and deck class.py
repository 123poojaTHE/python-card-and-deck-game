import random
suits=("hearts",'diamonds','spades','clubs')
ranks=('two','three','four','five','six','seven','eight','nine','ten','ace','king','queen','jack')
values={'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'king':10,'jack':10,"queen":10,'ace':11}
playing =True

# make card name class that for holding card with their rank
class Card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return self.rank + " of " +self.suit



class Deck():
    def __init__(self):
        self.deck =[]
        for suit in suits :
            for rank in ranks :
                self.deck.append(Card(suit,rank))
    def __str__(self):
        deck_comp=''
        for card in self.deck:
            deck_comp +='\n'+ card.__str__()
        return "the deck has :"+deck_comp
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card=self.deck.pop()
        return single_card
test_deck=Deck()
test_deck.shuffle()
print(test_deck)
        
class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
    def add_card(self,card):
        self.cards.append(card)
       # values[card.rank]
        self.value+=values[card.rank]
        if card.rank=='ace':
            self.aces+= 1
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value-=10
            self.aces-=1
zero=0
one=1
two=2
if 2:
    print('TRUE')
test_player = Hand()
pulled_card=test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)
test_player.add_card(test_deck.deal())
test_player.value


class Chips:
    def __init__(self,total=100):
        self.total=total
        self.bet=0
    def win_bet(self):
        self.total+=self.bet
    def lose_bet(self):
        self.total-=self.bet
def take_bet(chips):
    while True:
        try:
            chips.bet= int(input("how many chps whould you like to bet?"))
        except ValueError:
            print("sorry please provide an integer")
        else:
            if chips.bet> chips.total:
                print ("sorry ur bet cant exceed !  chips! you have :{} ".format(chips.total))
            else:
                break
            
def hit(deck,hand):
    single_card=deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()
def hit_or_stand(deck,hand):
    global playing
    while True:
        x=input("hit or stand ? Enter h or s")
        
        if x[0].lower()=='h':
            hit(deck,hand)
        elif x[0].lower() =='s':
            print("player stand dealer's turn")
            playing =False
        else:
            print("sorry! i did not understand  that! please enter 'h' and 's' only")
            continue
        break
def show_some(player,dealer):
    print("DEALERs HAND")
    print("one card hiden")
    print(dealer.cards[1])
    print("\n")
    print("PLAYER HAND :")
    for card in player.cards:
        print(card)
def show_all(player,dealer):
    print("DEALER HAND")
    for card in dealer.cards:
        print(card)
    print('\n')
    print("PLAYER HAND ")
    for card in player.cards:
        print(card)
        
def player_busts(player,dealer,chips):
    print("BUST PLAYER!")
    chips.lose_bet()
    
def player_wins(player,dealer,chips):
    print("PLAYER WINS!")
    chips.win_bet()
def dealer_busts(player,dealer,chips):
    print("PLAYER WINS ! DEALER BUSTED!")
    chips.win_bet()
def dealer_wins(player,dealer,chips):
    print("DEALER WINS!")
    chips.lose_bet()
def push(player ,dealer ):
    print("dealer and player tie! push")


while True:
    print("welcom to backjack")
    deck=Deck()
    deck.shuffle()
    
    player_hand=Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand=Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    
    player_chips=Chips()
    
    take_bet(player_chips)
    
    show_some(player_hand,dealer_hand)
    
    while playing:
        
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        if player_hand.value>21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    if player_hand.value<=21:
         while dealer_hand.value<player_hand.value:
             hit(deck,dealer_hand)
             
         show_all(player_hand,dealer_hand)
         
         if dealer_hand.value>21:
             dealer_busts(player_hand,dealer_hand,player_chips)
         elif dealer_hand.value > player_hand.value:
             dealer_wins(player_hand,dealer_hand,player_chips)
         elif dealer_hand.value<player_hand.value:
             player_wins(player_hand,dealer_hand,player_chips)
         else:
             push(player_hand,dealer_hand)

    print("\n player total chips are st:{}".format(player_chips.total))
        
    new_game=input("would you like to playe another hand?")
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
         print("thank you for playing!")
         break
        
















             
    
