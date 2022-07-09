import random
from words import word_list1
from words import word_list2
from words import word_list3
from gtts import gTTS
import os

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
def voice(given_word): #A FUNCTION WHICH CONVERTS TEXT TO AUDIO
    my = given_word    # MY IS VARIABLE WHICH CONTAINS WORD TO CONVERT INTO AUDIO
    langg = "en"       # LANGG IS VARIABLE TO STORE LANGUAGE CODE FOR WHICH IT SHOULD TRANSASLTE
    output = gTTS(text=my, lang=langg, slow=False)
    output.save("output.mp3")   # SAVING AUDIO FILE
    os.system("start output.mp3") #PRODUCING AUDIO FILE


name = input('enter the name ')
print(f"wel come to the game {name} ")
print("You have 7 lives to play this game")


lives = 7                                       #VARIABLE TO KEEP COUNT OF LIVES
correct = 0                                     #VARIABLE TO KEEP CONT OF CORRECT WORDS
while (lives > 0):
     if correct<= 10:
         given_word = random.choice(word_list1)     #PICKS THE WORD FROM WORDLIST1 IF SCORE IS LESS THAN OR EQUAL TO 10
     elif 10 < correct <= 20:
         given_word = random.choice(word_list2)     #PICKS THE WORD FRPM WORDLIST2 IF SCORE IS GREATER THAN 10 AND LESS THAN OR EQUAL TO 20
     else:
         given_word = random.choice(word_list3)     #PICKS THE WORD FROM WORDLIST IF SCORE IS GREATER THAN 20


     voice(given_word)                              #PASSES WORD TO VOICE FUNCTION TO CONVERT TEXT TO AUDIO
     taken_word = input("enter the word")
     if given_word == taken_word:                   #CHECKING INPUT OF USER WITH ANSWER
         correct = correct + 1                      #INCREMENT OF SCORE
         print(f"you said it correctly ")
     else:
         lives = lives - 1                          #DECREMENT OF LIVES
         print(f"you spelled wrong and you have {lives} lives to play this game ")
     if lives>=1:
         print(stages[7-lives])
print("THE GAME IS OVER")
print(f"Score is {correct}")                        #DISPLAYING SCORE OF THE USER
