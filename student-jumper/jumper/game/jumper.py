


class Jumper:
    '''


    Class Jumper will take controll of the Jumper, deleting parts of the parachute if needed and returning information. 

    Function:
    __init__(self)
    get_parachute(self)
    check_parachute(self)

    Attributes:
    self.parachute: list that will save the draw of the jumper
    self.keep_playing: boolean that will be True while the jumper still has a parachute

    '''

    def __init__(self):
        """The class constructor.

        Args:
            self (Jumper): an instance of Jumper.

        """

        self.parachute = ["  ___  ", " /___\ ", " \   / ",
                          "  \ /  ", "   0   ", "  /|\  ", "  / \  "]

        self.keep_playing = True

    def get_parachute(self):
        '''
        Gets the current state of the parachute and returns it. 

        '''
        return self.parachute

    def update_parachute(self, state):
        '''
        Will take result (boolean) as a parameter
        if result is False it will delete part of the parachute, 
        if it is True things stay the same. 
        '''

        #print(state)
        if state:
            self.parachute = self.parachute
        else:
            if len(self.parachute) > 3:
                self.parachute.pop(0)
            else:
                self.parachute[0] = "   x   "
                self.keep_playing = False

    def check_parachute(self):
        '''
        checks if it is possible to still play,
        return false if not. 
        return true if yes.
        '''
        return self.keep_playing
