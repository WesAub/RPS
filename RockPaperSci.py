import random
#exceptions

def rockPaperScissors():
    rps = ["Rock", "Paper", "Scissors"]
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        if age < 18:
            print("You must be over 18 to play")
        else:
            user_input = input("Select one of the following options: Rock, Paper, Scissors\n")
            if user_input not in rps:
                print("Invalid selsction")
            else:
                comp_select = random.choice(rps)
                if user_input == comp_select:
                    print(f"Congratualtions {name} you won the round")
                else:
                    print(f"Sorry {name} you lost this round")
                    
    
    except ValueError:
        print(f"Invalid age. Please enter a valid age ")


if __name__== "__main__":
    rockPaperScissors()
