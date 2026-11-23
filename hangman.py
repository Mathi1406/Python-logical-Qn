import random
class Hangman:
    def __init__(self):
        self.words=["python","java","apple","computer","developer",]
        self.secret_word=random.choice(self.words)
        self.guessed_letters=[]
        self.attempts=6
    def display_word(self):
        for letters in self.secret_word:
            if letters in self.guessed_letters:
                print(letters, end="") 
            else:
                print("_",end="")
    def guess_letter(self):
                guess=input("Guess a letter:").lower()
                if guess in self.guessed_letters:
                     print("Already Guessed")
                elif guess in self.secret_word:
                     print("Correct Guess")
                     self.guessed_letters.append(guess)
                     self.display_word()
                else:
                     print("Wrong Guess")
                     self.guessed_letters.append(guess)
                     self.attempts-=1
                     self.display_word()
    def check_win(self):
         for letter in self.secret_word:
              if letter not in self.guessed_letters:
                return False
         return True
    def play(self):
         while self.attempts>0 and not self.check_win():
              self.display_word()
              print("\n Attempt left",self.attempts)
              self.guess_letter()
         if self.check_win():
              print("\n You Win!")
              print("Word:",self.secret_word)
         else:
              print("\nGame Over!")
              print("Word:",self.secret_word)

game =Hangman()
game.play()       