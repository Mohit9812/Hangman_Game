from uword_creator import create
from hang_body import stages
import pyword
import random
from colorama import *
def getword(wlist):
    word=(random.choice(wlist)).upper()
    return word

def play(word):
    g=False
    gl=[]
    gw=[]
    t=6
    u=create(word)
    uw=u[0]
    cw=u[1]
    print(Fore.RED+'Welcome to HaNgMaN !!!!'+Fore.RESET)
    print(stages[t-1])
    print(Fore.LIGHTGREEN_EX+"HINT: ",pyword.hints[word.lower()]+Fore.RESET)
    print(Fore.BLUE+uw+Fore.RESET)
    print('\n')
    while not g and t>1:
        s=input(Fore.MAGENTA+'Guess a word or letter (Only Uppercase allowed):'+Fore.LIGHTMAGENTA_EX).strip()
        if s.isupper() and s.isalpha(): 
            if len(s)==1:
                if s in gl:
                    print(Fore.YELLOW+"You have already guessed the letter ",s,'.'+Fore.RESET)
                elif s in list(cw.values()):
                    print(Fore.GREEN+'You guessed correct.'+Fore.RESET)
                    uwl=list(uw)
                    gl.append(s)
                    for i in cw:
                        if s==cw[i]:
                            uwl[i]=s
                    uw="".join(uwl)
                    if "_" not in uw:
                        g=True
                else:
                    print(Fore.RED+'You guessed wrong.'+Fore.RESET)
                    t-=1
                    gl.append(s)
            elif len(s)==len(word):
                if s in gw:
                    print(Fore.YELLOW+'You have already guessed the word ',s,'.'+Fore.RESET)
                elif s==word:
                    print(Fore.GREEN+'You guessed correct.'+Fore.RESET)
                    g=True
                    uw=" ".join(list(s))
                else:
                    print(Fore.RED+'You guessed wrong.'+Fore.RESET)
                    t-=1
                    gw.append(s)
            else:
                print(Fore.YELLOW+'Invalid Entry! Either enter a letter or the full word'+Fore.RESET)
        else:
            print(Fore.YELLOW+'Invalid Entry! Only uppercase letter or word allowed'+Fore.RESET)
        print(stages[t-1])
        print(Fore.BLUE+uw+Fore.RESET)
        print("\n")
    if g:
        print(Fore.GREEN+"You guessed correct.")
        print("          ______                                      ______    _       ")
        print(" \   /   |      | |      |        \              /   |      |  | \    | ")
        print("  \ /    |      | |      |         \     /\     /    |      |  |  \   | ")
        print("   |     |      | |      |          \   /  \   /     |      |  |   \  | ")
        print("   |     |______| |______|           \_/    \_/      |______|  |    \_| "+Fore.RESET)
        print("\n\n")
    else:
        print(Fore.RED+"Your chances are over. "+word+" was the correct word.")
        print("          ______                            ______    ______   _____   ")
        print(" \   /   |      | |      |        |        |      |  |      | |        ")
        print("  \ /    |      | |      |        |        |      |  |______  |____    ")
        print("   |     |      | |      |        |        |      |         | |        ")
        print("   |     |______| |______|        |_____   |______|  |______| |_____   "+Fore.RESET)
        print("\n\n")

def main():
    word = getword(pyword.words)
    play(word)
    while input(Fore.MAGENTA+"Wanna Play Again? (Y/N) "+Fore.RESET).upper() == "Y":
        word = getword(pyword.words)
        play(word)
    print(Fore.RED+"______       ___           __    __     ______")
    print(Fore.RED+"|           /   \         /  \  /  \    |     ")
    print(Fore.RED+"|  ___     /_____\       /    \/    \   |___  ")
    print(Fore.RED+"|  | |    /       \     /            \  |     ")
    print(Fore.RED+"|____|   /         \   /              \ |_____")
    print(Fore.RED+" ______                 ______     ____       ")
    print(Fore.RED+"|      |   \       /    |          |   |      ")
    print(Fore.RED+"|      |    \     /     |___       |___|      ")
    print(Fore.RED+"|      |     \   /      |          | \        ")
    print(Fore.RED+"|______|      \_/       |_____     |  \       "+Fore.RESET)
    print("\n")
    print("\n")
if __name__=="__main__":
    main()