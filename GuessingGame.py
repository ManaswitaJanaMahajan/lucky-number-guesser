import random
def Play_Game():
    Lucky_No = random.randint(1,50)

    while True:
        user_no = int(input("Guess your lucky no:"))
        if user_no == Lucky_No:
            print("You have guessed the right no: ",Lucky_No, ". You have won. Game over!")
        elif user_no < Lucky_No :
            print("Low value.")
        else:
            print("High value.")

    print("Thank you for playing.")

Play_Game()

