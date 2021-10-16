import random

class Guesser: 
    '''
    This class will need to have a method: 

    update_word( ) that takes letter as a parameter. 
    It will check if the letter was a mistake, if it wasn't it will update
    the word. return a False if wrong or a True value if it was correct. 

    get_word() returns the current state of the word as a string. 

    check_word() checks if the word is complete, if it is print a small win message. 
    also, return a True boolean value if can still play and a False if game over.
    
    '''

    def __init__(self):
        self.word_list = ("loves", "byuid", "crazy", "idaho", "cleat",  "types")
        self.current_list = ["_","_","_","_","_"]
        # self.letter_list = []
        self.generated_word = random.choice(self.word_list)
        self.letter_list = list(self.generated_word)
        self.guessed_letter = ""

        print(self.generated_word)

    def update_word(self, guessed_letter):
        #debug print(guessed_letter)
        letter_index = 0
        result = False
        # walk through each letter and where there is a match, insert the guessed_letter into the list at position letter_index 
        for letter in self.letter_list:

            if guessed_letter == letter:
            # debug print("match")
                self.current_list[letter_index] = guessed_letter 
                result = True
            # debug print(self.current_list)
            # debug print(self.letter_list)
            # if guessed_letter does not match current_list position letter_index check for any letter (condition = "") if true insert "_" 
            # if current_list position letter_index contains a letter (or any character) increment letter_index and check the next letter 
            else:
                if self.current_list[letter_index] == "":  
                    self.current_list[letter_index] = "_" 
            letter_index += 1

        
        return result

        
                


    def get_word(self): 
        return self.current_list   

    def check_word(self): 
        # check if word is complete return false
        # if word is not complete return true
        if self.current_list == self.letter_list:
            print('Congratulations!') 
            return False
            
        else:
            return True