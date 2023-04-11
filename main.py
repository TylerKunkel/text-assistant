#Text Assistant

print("Welcome To My Text Assistant!")
print() #used for spacing
print('=' * 67) #used for aesthetic
print()
print()
print("Command List:")
print()
print("Type 'Tell me a joke' for a joke.")
print()
print("Type 'Cheer me up' for encouragement.")
print()
print("Type 'Motivate me' for a motivational sentence.")
print()
print("Type 'bits' for a bits to bytes calculator.")
print()
print("Type 'Quit' to close program")
print()
print()
print('=' * 67)
print()
#code 👇

# Text Assistant

while True:

        # Joke
    word = input("Give Me A Command!:\n")
    if (word == "Tell me a joke") or (word == "Joke") or (
            word == "tell me a joke") or (word == "joke"):

        print()
        print("How many programmers does it take to change a light bulb?")
        print()
        print("None!")
        print("That's a hardware problem.")
        print()

        # Encouragement
    elif (word == "Cheer me up") or (word == "cheer me up") or (
            word == "encouragement") or (word == "Encouragement"):

        print()
        print(
            "There is something, you are better at than every other person... you just haven't found it yet. Keep searching. Give every opportunity your all until it is made clear."
        )
        print()

        # Motivation
    elif (word == "Motivate me") or (word == "motivate me") or (
            word == "Motivation") or (word == "motivation"):

        print()
        print(
            "Instead of thinking how hard your journey is, think how great your story will be. - Andy Frisella"
        )
        print()
        print(
            "The instant you accept responsibility for everything in your life is the moment you acquire the power to change it. - Ed Mylett"
        )
        print()

        # Bit Value Calculator

    elif (word == "bits") or (word == "Bits") or (
            word == "How many bits?") or (word == "how many bits?"):
        number_base = 2
        number_exponent = int(input('How many bits?:\n '))
        print()
        print('Different Values: ' + str(number_base**number_exponent))
        print()

        # Quit The Program

    elif (word == "Quit") or (word == "quit"):
        print("Have a nice day!")
        break

    else:
        print("That is an invalid command")
        print()
        print("Here is a command list.")
        print()
        print("Joke - Tells a joke")
        print(
            "Encouragement - Tells a quote I tell people when they feel lost")
        print(
            "Motivate - Tells one quote from Andy Frisella and one from Ed Mylett"
        )
        print("Bits - A simple binary bits value calculator")
        print()
