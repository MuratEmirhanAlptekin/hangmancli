import random
word_list = []
letter_amount = int(input("how many letters do you want do play with?"))
f = open("words.txt","r")
for i in f:
    if len(i) == letter_amount+1:
        word_list.append(i)
word_list = [i.rstrip("\n") for i in word_list]
class hangman:
    def __init__(self,amount):
        self.tries = 8
        self.word = random.choice(word_list)
        self.manlist = [" |--|\n    |\n    |\n    |\n    |\n    |"," |--|\n O  |\n    |\n    |\n    |\n    |"," |--|\n O  |\n |  |\n    |\n    |\n    |"," |--|\n O  |\n\|  |\n    |\n    |\n    |"," |--|\n O  |\n\|/ |\n    |\n    |\n    |"," |--|\n O  |\n\|/ |\n |  |\n    |\n    |"," |--|\n O  |\n\|/ |\n |  |\n/   |\n    |"," |--|\n O  |\n\|/ |\n |  |\n/ \ |\n    |"]
        self.flag = 0
        self.amount = amount
    def start(self):
        guessed = list("-"*self.amount)
        while self.tries != 1:
            print()
            print("pick a letter")
            print("".join(guessed),"\n")
            letter = input()
            if letter in self.word:
                for i in range(len(self.word)):
                    if self.word[i] == letter:
                        guessed[i] = letter
            elif self.tries != 1:
                self.tries-=1
            print(self.manlist[8-self.tries])
            if "".join(guessed) == self.word:
                print(self.word)
                self.flag = 1
                break
    def show(self):
        if self.flag == 1:
            print("congrats you won.")
        else:
            print("you lost.")
            print("the word was",self.word)


print("welcome to hangman game!!")
print(" |--|\n O  |\n\|/ |\n |  |\n/ \ |\n    |")
print("press s to start")
if (input() == "s"):
    a = hangman(letter_amount)
    a.start()
    a.show()
    
    



        



