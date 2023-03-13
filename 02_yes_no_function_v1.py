# Functions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer yes / no")


# Main Routine goes here

show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask the user if they have played before
    show_instructions = yes_no("Have you played this game before? ")

    # If they say yes, output 'program continues'
    if show_instructions == "yes":
        print("program continues")

    else:
        print("displays instructions")
