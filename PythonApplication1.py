from distutils import core
import random
import msvcrt

suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
values = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
deck = []
hands = []
playing = True
winGame = False

# Resets Deck
def shuffleDeck():
    deck.clear()    

    for suit in suits:
        for value in values:
            deck.append(f"{value} of {suit}")
         
    random.shuffle(deck)

shuffleDeck()

def playWordle():
    words = ['ABOUT', 'ABOVE', 'ABUSE', 'ACTOR', 'ACUTE', 'ADMIT', 'ADOPT', 'ADULT', 'AFTER', 'AGAIN', 'AGENT', 'AGREE', 'AHEAD', 'ALARM', 'ALBUM', 'ALERT', 'ALIKE', 'ALIVE', 'ALLOW', 'ALONE', 'ALONG', 'ALTER', 'AMONG', 'ANGER', 'ANGLE', 'ANGRY', 'APART', 'APPLE', 'APPLY', 'ARENA', 'ARGUE', 'ARISE', 'ARRAY', 'ASIDE', 'ASSET', 'AUDIO', 'AUDIT', 'AVOID', 'AWARD', 'AWARE', 'BADLY', 'BAKER', 'BASES', 'BASIC', 'BASIS', 'BEACH', 'BEGAN', 'BEGIN', 'BEGUN', 'BEING', 'BELOW', 'BENCH', 'BILLY', 'BIRTH', 'BLACK', 'BLAME', 'BLIND', 'BLOCK', 'BLOOD', 'BOARD', 'BOOST', 'BOOTH', 'BOUND', 'BRAIN', 'BRAND', 'BREAD', 'BREAK', 'BREED', 'BRIEF', 'BRING', 'BROAD', 'BROKE', 'BROWN', 'BUILD', 'BUILT', 'BUYER', 'CABLE', 'CALIF', 'CARRY', 'CATCH', 'CAUSE', 'CHAIN', 'CHAIR', 'CHART', 'CHASE', 'CHEAP', 'CHECK', 'CHEST', 'CHIEF', 'CHILD', 'CHINA', 'CHOSE', 'CIVIL', 'CLAIM', 'CLASS', 'CLEAN', 'CLEAR', 'CLICK', 'CLOCK', 'CLOSE', 'COACH', 'COAST', 'COULD', 'COUNT', 'COURT', 'COVER', 'CRAFT', 'CRASH', 'CREAM', 'CRIME', 'CROSS', 'CROWD', 'CROWN', 'CURVE', 'CYCLE', 'DAILY', 'DANCE', 'DATED', 'DEALT', 'DEATH', 'DEBUT', 'DELAY', 'DEPTH', 'DOING', 'DOUBT', 'DOZEN', 'DRAFT', 'DRAMA', 'DRAWN', 'DREAM', 'DRESS', 'DRILL', 'DRINK', 'DRIVE', 'DROVE', 'DYING', 'EAGER', 'EARLY', 'EARTH', 'EIGHT', 'ELITE', 'EMPTY', 'ENEMY', 'ENJOY', 'ENTER', 'ENTRY', 'EQUAL', 'ERROR', 'EVENT', 'EVERY', 'EXACT', 'EXIST', 'EXTRA', 'FAITH', 'FALSE', 'FAULT', 'FIBER', 'FIELD', 'FIFTH', 'FIFTY', 'FIGHT', 'FINAL', 'FIRST', 'FIXED', 'FLASH', 'FLEET', 'FLOOR', 'FLUID', 'FOCUS', 'FORCE', 'FORTH', 'FORTY', 'FORUM', 'FOUND', 'FRAME', 'FRANK', 'FRAUD', 'FRESH', 'FRONT', 'FRUIT', 'FULLY', 'FUNNY', 'GIANT', 'GIVEN', 'GLASS', 'GLOBE', 'GOING', 'GRACE', 'GRADE', 'GRAND', 'GRANT', 'GRASS', 'GREAT', 'GREEN', 'GROSS', 'GROUP', 'GROWN', 'GUARD', 'GUESS', 'GUEST', 'GUIDE', 'HAPPY', 'HARRY', 'HEART', 'HEAVY', 'HENCE', 'HENRY', 'HORSE', 'HOTEL', 'HOUSE', 'HUMAN', 'IDEAL', 'IMAGE', 'INDEX', 'INNER', 'INPUT', 'ISSUE', 'JAPAN', 'JIMMY', 'JOINT', 'JONES', 'JUDGE', 'KNOWN', 'LABEL', 'LARGE', 'LASER', 'LATER', 'LAUGH', 'LAYER', 'LEARN', 'LEASE', 'LEAST', 'LEAVE', 'LEGAL', 'LEVEL', 'LEWIS', 'LIGHT', 'LIMIT', 'LINKS', 'LIVES', 'LOCAL', 'LOGIC', 'LOOSE', 'LOWER', 'LUCKY', 'LUNCH', 'LYING', 'MAGIC', 'MAJOR', 'MAKER', 'MARCH', 'MARIA', 'MATCH', 'MAYBE', 'MAYOR', 'MEANT', 'MEDIA', 'METAL', 'MIGHT', 'MINOR', 'MINUS', 'MIXED', 'MODEL', 'MONEY', 'MONTH', 'MORAL', 'MOTOR', 'MOUNT', 'MOUSE', 'MOUTH', 'MOVIE', 'MUSIC', 'NEEDS', 'NEVER', 'NEWLY', 'NIGHT', 'NOISE', 'NORTH', 'NOTED', 'NOVEL', 'NURSE', 'OCCUR', 'OCEAN', 'OFFER', 'OFTEN', 'ORDER', 'OTHER', 'OUGHT', 'PAINT', 'PANEL', 'PAPER', 'PARTY', 'PEACE', 'PETER', 'PHASE', 'PHONE', 'PHOTO', 'PIECE', 'PILOT', 'PITCH', 'PLACE', 'PLAIN', 'PLANE', 'PLANT', 'PLATE', 'POINT', 'POUND', 'POWER', 'PRESS', 'PRICE', 'PRIDE', 'PRIME', 'PRINT', 'PRIOR', 'PRIZE', 'PROOF', 'PROUD', 'PROVE', 'QUEEN', 'QUICK', 'QUIET', 'QUITE', 'RADIO', 'RAISE', 'RANGE', 'RAPID', 'RATIO', 'REACH', 'READY', 'REFER', 'RIGHT', 'RIVAL', 'RIVER', 'ROBIN', 'ROGER', 'ROMAN', 'ROUGH', 'ROUND', 'ROUTE', 'ROYAL', 'RURAL', 'SCALE', 'SCENE', 'SCOPE', 'SCORE', 'SENSE', 'SERVE', 'SEVEN', 'SHALL', 'SHAPE', 'SHARE', 'SHARP', 'SHEET', 'SHELF', 'SHELL', 'SHIFT', 'SHIRT', 'SHOCK', 'SHOOT', 'SHORT', 'SHOWN', 'SIGHT', 'SINCE', 'SIXTH', 'SIXTY', 'SIZED', 'SKILL', 'SLEEP', 'SLIDE', 'SMALL', 'SMART', 'SMILE', 'SMITH', 'SMOKE', 'SOLID', 'SOLVE', 'SORRY', 'SOUND', 'SOUTH', 'SPACE', 'SPARE', 'SPEAK', 'SPEED', 'SPEND', 'SPENT', 'SPLIT', 'SPOKE', 'SPORT', 'STAFF', 'STAGE', 'STAKE', 'STAND', 'START', 'STATE', 'STEAM', 'STEEL', 'STICK', 'STILL', 'STOCK', 'STONE', 'STOOD', 'STORE', 'STORM', 'STORY', 'STRIP', 'STUCK', 'STUDY', 'STUFF', 'STYLE', 'SUGAR', 'SUITE', 'SUPER', 'SWEET', 'TABLE', 'TAKEN', 'TASTE', 'TAXES', 'TEACH', 'TEETH', 'TERRY', 'TEXAS', 'THANK', 'THEFT', 'THEIR', 'THEME', 'THERE', 'THESE', 'THICK', 'THING', 'THINK', 'THIRD', 'THOSE', 'THREE', 'THREW', 'THROW', 'TIGHT', 'TIMES', 'TIRED', 'TITLE', 'TODAY', 'TOPIC', 'TOTAL', 'TOUCH', 'TOUGH', 'TOWER', 'TRACK', 'TRADE', 'TRAIN', 'TREAT', 'TREND', 'TRIAL', 'TRIED', 'TRIES', 'TRUCK', 'TRULY', 'TRUST', 'TRUTH', 'TWICE', 'UNDER', 'UNDUE', 'UNION', 'UNITY', 'UNTIL', 'UPPER', 'UPSET', 'URBAN', 'USAGE', 'USUAL', 'VALID', 'VALUE', 'VIDEO', 'VIRUS', 'VISIT', 'VITAL', 'VOICE', 'WASTE', 'WATCH', 'WATER', 'WHEEL', 'WHERE', 'WHICH', 'WHILE', 'WHITE', 'WHOLE', 'WHOSE', 'WOMAN', 'WOMEN', 'WORLD', 'WORRY', 'WORSE', 'WORST', 'WORTH', 'WOULD', 'WOUND', 'WRITE', 'WRONG', 'WROTE', 'YIELD', 'YOUNG', 'YOUTH']
    code = list(random.choice(words))
    count = 1
    print('')
    print(f"Welcome to Wordle! You have 6 tries to guess the code...")
    while count <= 6:
        print()
        guess = list(input("Guess: ").upper())
        while len(guess) != 5:
            guess = list(input("Please input a 5 letter word\nGuess: ").upper())
        print()
        correct_letters =  0
        correct_positions = 0
        code_copy = code
        corrected_guess = [' ']*5
        print('')
        code_copy = code.copy()
        for index, (guess_letter, code_letter) in enumerate(zip(guess, code)):
            if guess_letter == code_letter:
                correct_positions += 1
                corrected_guess[index] = code_letter
            if guess_letter in code_copy:
                correct_letters += 1
                code_copy.remove(guess_letter)
        print('|'.join(corrected_guess))
        print(f'Correct letters: {correct_letters} | Correct positions: {correct_positions} | Guesses Left: {6 - count}')
        if correct_positions == 5:
            print('')
            print(f"YOU CRACKED THE CODE IN {count}!!!")
            break
        count += 1
    print(f'The code was {"".join(code)}')
    print("Try again next time")
         


def dealHands():
    players = int(input("How many players? --> "))
    num_cards = int(input("How many cards will each player have? --> "))


    for i in range(players):
        hands.append([])
   
    for i in range(num_cards):
        for hand in hands:
            hand.append(deck.pop())
    


# Function Used to Start Game
def playHigherOrLower():
    score = 0
    shuffleDeck()
    card = deck.pop()
    print(f"Welcome to Higher or Lower!\nThe first card is: {card}")

    while True:
        answer = input("Would you like to go Higher (H) or Lower (L)? --> ")
        
        # Makes sure user provides Valid Option
        while answer.upper() != 'L' and answer.upper() != 'H':
            answer = input("Please enter either H or L --> ")
            
        comparing_card = card
        card = deck.pop()
        print(card)
        

        if values.index(card.split()[0]) == values.index(comparing_card.split()[0]):
            print("== DRAW ==")
        elif (answer.upper() == 'H' and values.index(card.split()[0]) > values.index(comparing_card.split()[0])) or (answer.upper() == 'L' and values.index(card.split()[0]) < values.index(comparing_card.split()[0])):
            score += 1
            if score == 5:
                return True
                
        else:
            return False
        
def playSnap():
    stack = []
    shuffleDeck()
    player1 = deck[0:25]
    player2 = deck[25:51]
    card = 'x'
    comparing_card = 'o'
    turn = 1
    
    while True:
        if len(player1) == 0 and len(player2) == 0:
            print("Both Stacks out of Cards!\nTake half the stack each")
            quotient, remainder = divmod(len(stack), 2)
    
            player1 = stack[:quotient + remainder]
            player2 = stack[quotient + remainder:]
            stack.clear()
            comparing_card = 'x'
            card = 'o'
    
        key = msvcrt.getch().decode('utf-8').lower() 
        
        
        if card.split()[0] == comparing_card.split()[0]:
            
            while key not in ['w', 'o']:
                key = msvcrt.getch().decode('utf-8').lower() 
                    
            if key == 'w':
                player1 = player1 + stack
                random.shuffle(player1)
                print(f"Player 1 won {len(stack)} cards")
                         
            elif key == 'o':
                player2 = player2 + stack
                random.shuffle(player2)
                print(f"Player 2 won {len(stack)} cards")
                            
            stack.clear()
            comparing_card = 'x'
            card = 'o'
                
            if len(player2) == 0:
                print("Player 1 is the winner!")
                input()
                break
            if len(player1) == 0:
                print("Player 2 is the winner!")
                input()
                break
                
        else:
            increment = 1
            if len(player1) == 0 or len(player2) == 0:
                increment = 2
                
            if turn % 2 == 0:
                if key == 'p':
                    comparing_card = card
                    card = player2.pop()
                    stack.append(card)
                    print(card)
                
            else:
                if key == 'q':
                    comparing_card = card
                    card = player1.pop()
                    stack.append(card)
                    print(card)
                    
            turn += increment


       
    
        

def main():
    print('===== Welcome to GameCentre =====')
    game = int(input('Choose a game:\n1: Higher or Lower\n2 Wordle\n3: Snap\n ---> '))
    if game == 1: 
        winGame = playHigherOrLower()

        
        while playing:
            if winGame == False:
                print("You Lose! Press any Key to Try Again")
            else:
                print("Congrats you won! Press any Key to Try Again")
    
            input()
            winGame = playHigherOrLower()
    elif game == 2:
        playWordle()
    elif game == 3:
        playSnap()
        
#main()


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def calculator():
    saved = None
    
    while True:
        print("Simple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Clear")

        choice = input("Select operation (1/2/3/4/5): ")
        
        if choice == '5':
            saved = None
            print('Calculator cleared!')
            
        else:
            if saved is None:
                num1 = float(input("Enter first number: "))
            else:
                num1 = saved
            
            num2 = float(input("Enter second number: "))

            if choice == '1':
                saved = add(num1, num2)
                print(f"{num1} + {num2} = {saved}")

            elif choice == '2':
                saved = subtract(num1, num2)
                print(f"{num1} - {num2} = {saved}")

            elif choice == '3':
                saved = multiply(num1, num2)
                print(f"{num1} * {num2} = {saved}")

            elif choice == '4':
                saved = divide(num1, num2)
                print(f"{num1} / {num2} = {saved}")
        
        

        
calculator()