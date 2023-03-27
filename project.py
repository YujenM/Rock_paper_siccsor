from random import randint
import cowsay
def main():
    while True:
        user=input("Press S to start game and press Q to quit the game: ")
        if user.lower() == "s":
            print("Keys of the Game")
            print("1=✊rock")
            print("2=✋paper")
            print("3=✌️ siccsor")
            try:
                round=0
                rounds=int(input("How many rounds do you want to play?: "))
                while True:
                    if round==rounds:
                        break
                    elif round!=rounds:
                        while True:
                            user=int(input("Enter number from 1-3: "))
                            if user==1 or user==2 or user==3:
                                break
                        if user ==1:
                            print ("✊")
                        if user==2:
                            print ("✋")
                        if user==3:
                            print ("✌️")
                        computer=randint(1,3)
                        if computer==1:
                            print ("✊")
                        if computer==2:
                            print ("✋")
                        if computer==3:
                            print ("✌️")
                        print(wining(user,computer))
                        round+=1
            except ValueError:
                print("Enter integer")
            continue
        elif user.lower() =="q":
            exit()
            break
def wining(user,computer):
    if user==computer:
        return ("Tie")
    if user==1 and computer==2:
        return ("computer wins")
    if user==2 and computer==3:
        return ("computer wins")
    if user==3 and computer==1:
        return ("computer wins")
    if user==1 and computer==3:
        return ("user wins")
    if user==3 and computer==2:
        return ("user wins")
    if user==2 and computer==1:
        return ("user wins")
def exit():
    cowsay.cow("Thanks for playing")
if __name__ == "__main__":
    main()