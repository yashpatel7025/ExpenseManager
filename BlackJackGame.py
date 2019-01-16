suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}




class Player:
                    money=1000
                    score=0
                    plist=[]
                    bet=0
                    bust=False
                    count=0

                    

                    def setCard(self,rank,suit):
                        self.rank=rank
                        self.suit=suit
                        if values[self.rank]==11 and (Player.score+values[self.rank]>21):
                             Player.score=Player.score+1
                        else:
                             Player.score=Player.score+values[self.rank]

                    def __str__(self):
                        return (f'{self.rank} of {self.suit}')

                    def takeBet(self):
                        while True:
                            Player.bet=int(input('Enter Your Bet :- '))
                            print('\n')
                            if Player.bet>Player.money:
                                print(f'You have only {Player.money} RS')
                                continue
                            else:
                                break


                    def deal(self):
                                Player.count+=1
                                a,b=deck_obj.giveCard()
                                Player.plist.append(Player())
                                Player.plist[-1].setCard(a,b)
                                print("Players Hand")
                                for i,v in enumerate(Player.plist):
                                        print(f'     {Player.plist[i].rank} of {Player.plist[i].suit}')
                                if Player.count==1:
                                     print('\n')    
                                if Player.count>1:
                                        print(f'YOUR SCORE IS {Player.score}')
                                        print('\n')   

                                #whenever player or dealer get card score has to be checked

                                if Player.score>21:
                                    print("You Bust,Dealer won bet ")
                                    Dealer.money=Dealer.money+Player.bet
                                    Player.money=Player.money-Player.bet
                                    Player.bust=True
                                    
                                    
                                    
                                    
class Dealer:
                money=50000
                score=0
                dlist=[]
                count=0
                bust=False
                
               

                def setCard(self,rank,suit):
                    self.rank=rank
                    self.suit=suit
                    if values[self.rank]==11 and (Dealer.score+values[self.rank]>21):
                         Dealer.score=Dealer.score+1
                    else:
                         Dealer.score=Dealer.score+values[self.rank]

                def __str__(self):
                    return (f'{self.rank} of {self.suit}')

                def deal(self):
                            Dealer.count+=1
                            a,b=deck_obj.giveCard()
                            Dealer.dlist.append(Dealer())
                            Dealer.dlist[-1].setCard(a,b)
                            print("Dealers Hand")
                            for i,v in enumerate(Dealer.dlist):
                                    if Dealer.count<3:
                                        if i==0:
                                            print("     <hidden card>")
                                        else:
                                            print(f'     {Dealer.dlist[i].rank} of {Dealer.dlist[i].suit}')

                                    else:
                                            print(f'     {Dealer.dlist[i].rank} of {Dealer.dlist[i].suit}')
                            if Dealer.count<3:
                                 print('\n')   
                            if Dealer.count>2:
                                    print(f' DEALERS SCORE IS {Dealer.score}')
                                    print('\n') 

                            if Dealer.score>21:

                                print("Dealer Bust,You won bet,Congratulation!!")
                                Dealer.money=Dealer.money-Player.bet
                                Player.money=Player.money+Player.bet
                                Dealer.bust=True


                                
                                
                                
                                
class Card:
    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit
 
        
    def shuffle(self,deck):
        import random
        random.shuffle()
        
        
        
        

        

class Deck:
    
                def __init__(self):
                    '''now here we want array consisting 52 cards ,at one position there should be 2 place 1 for suits and other for rank ,total
                       there should be 52 places but it is not possile bye dictioaries since there occurs multiple same keys and different values
                       there for why not to use class,class would have that 2 place or items and 52 list values will be object pointing to that class'''
                    self.deck=[]
                    for i in ranks:
                         for j in suits:
                            self.deck.append(Card(i,j))

                def shuffle(self):
                    import random
                    random.shuffle(self.deck)

                def __str__(self):
                    for i in self.deck:
                        print(f'{i.rank} of {i.suit}')

                def giveCard(self):
                    temp=self.deck.pop()
                    a=temp.rank
                    b= temp.suit
                    return a,b

                def printDeck(self):
                    for i in self.deck:
                        print(f'{i.rank} of {i.suit}')
                        
                        
                        
                        
                        
                        
                        
opt="temp"
def hit_stay():
        global opt
        while True:
                opt=input("do you want to HIT or STAY :-")
                if opt.lower()=='hit' or opt.lower()=='stay': 
                    break
                else:
                    print("PLEASE Enter HIT or STAY :-")
                    continue
        return opt
            
def playerstayed():
    while Dealer.score<17:
        dealer_obj.deal()
    if Dealer.bust==True:
        return 1
    if 16<Dealer.score<22:
        if Player.score>Dealer.score:
            print(f' YOURS CARD IS {[str(x.rank) +" of "+ str(x.suit) for x in Player.plist ]}')
            print(f'YOUR SCORE IS {Player.score}')
            print("You won bet,Congratulation!! ")
            Dealer.money=Dealer.money-Player.bet
            Player.money=Player.money+Player.bet
        elif Player.score<Dealer.score:
            print(f' DEALERS CARD IS {[str(x.rank) +" of "+ str(x.suit) for x in Dealer.dlist ]}')
            print(f' DEALERS SCORE IS {Dealer.score}')
            print("Dealer won bet,You lose!!")
            Dealer.money=Dealer.money+Player.bet
            Player.money=Player.money-Player.bet
        else:
            print(f' YOURS CARD IS {[str(x.rank) +" of "+ str(x.suit) for x in Player.plist ]}')
            print(f'YOUR SCORE IS {Player.score}')
            print(f' DEALERS CARD IS {[str(x.rank) +" of "+ str(x.suit) for x in Dealer.dlist ]}')
            print(f'DEALERS SCORE IS {Dealer.score}')
            print("draw bet i.e push")
        return 2
    
         
def play():
            global deck_obj
            global player_obj
            global dealer_obj
            global opt
            playing=True
            while playing==True:
                        deck_obj=Deck()
                        deck_obj.shuffle()
                        player_obj=Player()
                        player_obj.takeBet()


                        player_obj.deal()
                        player_obj.deal()


                        dealer_obj=Dealer()
                        dealer_obj.deal()
                        dealer_obj.deal()


                        while hit_stay().lower()!='stay':
                                player_obj.deal()
                                if Player.bust==True:
                                    break
                        if Player.bust==True:
                                break
                        if opt.lower()=='stay':#for this statment i had to make opt as globalotherwise not defines error
                            temp=playerstayed()
                            if temp==1:
                                break
                            if temp==2:
                                 pass

                        while True:
                            opt2=input("do you want to play again...?YES or NO :-")
                            if opt2.lower()=='yes' or opt2.lower()=='no':
                                break
                            else:
                                print("PLEASE Enter HIT or STAY :-")
                                continue
                        if opt2.lower()=='yes':
                                playing=True
                                # DONT REASSIGN MONEY Player.money=1000
                                Player.score=0
                                Player.plist=[]
                                Player.bet=0
                                Player.bust=False
                                Player.count=0
                                # DONT REASSIGN MONEY Dealer.money=50000
                                Dealer.score=0
                                Dealer.dlist=[]
                                Dealer.count=0
                                Dealer.bust=False
                                clear_output()

                                continue
                        elif opt2.lower()=='no':
                            print("Thanks for playing...")
                            
                            
                            
                            
                            
 #MAIN SCRIPT                           
from IPython.display import clear_output                           
deck_obj='temp'
player_obj='temp'
dealer_obj='temp'
play()                   
if Player.bust==True or Dealer.bust==True:
                while True:
                            
                            opt2=input("do you want to play again...?YES or NO :-")
                            if opt2.lower()=='yes' or opt2.lower()=='no':
                                break
                            else:
                                print("PLEASE Enter HIT or STAY :-")
                                continue
                if opt2.lower()=='yes':
                                playing=True
                                # DONT REASSIGN MONEY Player.money=1000
                                Player.score=0
                                Player.plist=[]
                                Player.bet=0
                                Player.bust=False
                                Player.count=0
                                # DONT REASSIGN MONEY Dealer.money=50000
                                Dealer.score=0
                                Dealer.dlist=[]
                                Dealer.count=0
                                Dealer.bust=False
                                clear_output()

                                play()
                elif opt2.lower()=='no':
                            print("Thanks for playing...")



            
                
                        
    
    



