from game.console import Console
from game.guesser import Guesser
from game.jumper import Jumper

class Director:
    
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        seeker (Seeker): An instance of the class of objects known as Seeker.
        hider (Hider): An instance of the class of objects known as Hider.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.seeker = Seeker()
        self.hider = Hider()
        self.keep_playing = True
        
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.do_outputs()
            self.get_inputs()
            self.do_updates()
    
    def do_outputs(self):
        """Outputs the important game information for each round of play. 
        gets the current state of the parachute from the JUMPER CLASS
        tells the CONSOLE to print it 

        Args:
            self (Director): An instance of Director.
        """
        #gets and prints the current state of the parachute from Jumper Class
        current_parachute = self.jumper.get_parachute()

        #Telss the console class to print current parachute
        self.console.write(current_parachute)



    def get_inputs(self):
        """Gets the inputs in the middle of each round of play. In this case,
        that means getting the letter from the player. 
        updates word, calculates if the player missed or got it wrong.
        and then updates the parachute. 

        Args:
            self (Director): An instance of Director.
        """

        # tells the class console to print the message "Enter a letter [a-z]: "
        letter = self.console.read_letter("Enter a letter [a-z]: ")

       
        #sends the letter to be evaluated by the class guesser.
        result = self.guesser.update_word(letter)

        #sends the result to the jumper class subtract or not 
        #depending on the result of the evaluation.
        self.jumper.update_parachute(result)
        
       
        
       
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means the hider watches the seeker.

        Args:
            self (Director): An instance of Director.
        """

        #gets the partial word 
        word = self.guesser.get_word()
        #telss console to write the word
        self.console.write(word)


        #Checks if possible to play still.
        # Keep_playing = false if not able 
        # Keep_playing = true if able 
        self.keep_playing = check_parachute()

        self.keep_playing = check_word()