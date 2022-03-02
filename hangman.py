import random
from os import name, system

class Hangman:

    def __init__(self, word_list) -> None:
        self.word_list = word_list
        self.word = self.__choose_word()
        self.lives = 6

    def __choose_word(self) -> str:

        return random.choice(self.word_list)

    def __replace(self, word, placing, letter):
        
        # replace "_" with corresponding "letter"
         # 1. GET THE INDEX OF THE LETTER IN THE WORD
         # - IF THE LETTER IS ALREADY PRESENT IN PLACING SEARCH AFTER THAT LETTER AND REPLACE THE LETTER WITH CORRESPONDING UNDERSCORE, 
         # OTHERWISE REPLACE THE LETTER WITH THE CORRESPONDING UNDERSCORE
        if letter in placing:
            try:
                idx = word.index(letter)
                next_idx = word.index(letter, idx+1)
                # 4. REPLACE THE CORRESPONDING LETTER
                placing[next_idx] = letter
            except ValueError:
                self.lives -= 1
        else:
            placing[word.index(letter)] = letter

    def start(self) -> None:
       
        # display empty places for letters
        placing = [i for i in ("_"*len(self.word))]
        
        while True:
            # clear console
            self.__clear()
             # display banner
            self.__create_banner()
            # display hangman
            self.__draw_hangman()
            if self.lives > 0:
                if "_" in placing:
                    
                    # format placing
                    for i in placing:
                        print(i + " ", end=" ")
                    print("\n")

                    # ask user input
                    letter = input("Enter a letter: ").lower()
                    
                    # CHECK IF THE LETTER EXISTS IN WORD
                    # - IF THAT IS THE CASE DO FOLLOWING, OTHERWISE LOSE LIFE
                    if letter in self.word and letter != "":
                        self.__replace(self.word, placing, letter[0])
                        
                    else:
                        self.lives -= 1
                else:
                    print("You won!")
                    break
            else:
                print("You loose!")
                print(f"The word was {self.word}")
                break

    def __clear(self):
        if name == 'nt':
            system("cls")
        else:
            system("clear")
                
    def __draw_hangman(self) -> None:

        if self.lives == 6:
            print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')
        elif self.lives == 5:
            print( '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')
        elif self.lives == 4:
            print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')
        elif self.lives == 3:
            print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
        elif self.lives == 2:
            print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')
        elif self.lives == 1:
            print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')
        else:
            print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')
            

    def __create_banner(self) -> None:
        print("""
888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P"     
""")

# 1. generate random word
with open("./wordlist.txt") as file:
    words = file.readlines()
    # remove new line characters from wordlist
    new_wordlist = [i.strip("\n") for i in words]
    print(new_wordlist)
    
hangman = Hangman(word_list=new_wordlist)
hangman.start()
