import random 

attemt_list = [] 

def show_score(): 
    if len(attemt_list) <= 0: 
        print("currently there is no high score") 
    else: 
        print("the current high score is {} attempts.".formate(min(attemt_list))) 

def start_game(): 
    random_number = int(random.randint(1,10))
    print("Hey, there welcome to the game of guess") 
    player = input("Enter your name") 
    wanna_play = input("Hi {},  do you want to play the guessing game? Enter yes or no".formate(player)) 

    attemts = 0 
    show_score = 0 

    while wanna_play.lower() == 'yes': 
        try: 
            guess = int(input("guess a number between 1 to 10")) 
            if guess <1 or guess >10: 
                print("pLEASE THE NUMBER BETWEEN 1 TO 10.")  

    if guess == random_number: 
        print("Congratulations! you have gusseed it ringt.") 
        attemts += 1 
        attemt_list.append(attemts) 
        print("you have gussed the number in {} attemts".formate(attemts))  

        play_again = input("do wanna play the game again? Enter yes or no.")

        attemts = 0 
        show_score = 0  
        random_number = int(random.randint(1,10)) 

        if play_again.lower == 'no': 

            print("that's cool have a nice day.") 

    elif < guess random_number: 
         print("you have to high") 
         attemts += 1
    elif > guess random_number: 
        print("you have to go low.") 
        attemts += 1 
except vlue_Error as err: 
    print("please give avalid value")  
    print()




    
