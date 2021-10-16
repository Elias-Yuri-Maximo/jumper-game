class Console:
    """Holds the code responsible for printing all outputs
    and taking all inputs.

    Stereotype:
        Service Provider

    """    

    def __init__(self):
        # This is just a debug thing I guess.
        # I have no idea what's supposed to go in here. I'm thinking maybe nothing?
        #print("Console instance created")
        pass

    
    def draw_parachute(self, current_parachute):
        """ prints the current status of the parachute
        Assuming the Parachute object has a list as one of its attributes,
        use this for loop to print it out when needed.

        Parameters
            self: The current Console object (in all honesty I have no idea
                              what to do with this variable or if it's even necessary)
            current_parachute: This is a placeholder name for the LIST
                               that will be passed in. Prints the current state
                               of the parachute when called (at the end of each turn).
        
        """
        for i in current_parachute:
            print(i)


    def read_letter(self):
        """ Takes one alphabetical character from user

        Parameter:
            self: the current Console object
        
        """
        # 'while True' is my way of making sure user input is valid.
        while True:

            # input is immediately upper-cased to create a consistent style
            letter_guess = input("Guess the letter [a-z]: ")

            # Input must be exactly one alphabetical character
            if letter_guess.isalpha() and len(letter_guess) == 1:
                break
            else:
                print("Invalid input.")
                continue
        
        return letter_guess

    def write(self, word):
        print(*word)

