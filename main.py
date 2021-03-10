# Guess your number!
# Žans Kristians Cepeļevs
# 10.03.2021, Valmiera

# Importē random libary
# Importē math libary

import math
import random



def game_function():
    # User input skailtim no kura(min) līdz kuram(max) tiks izvēlēts nejaušs skaitlis, kas jāuzmin
    # Ievadi attiecīgu tekstu, lai lietotājs saprot, ka lower ir min un upper max
    lower = int(input("Ievadi skaitli no kura sāksim spēli :- "))
    upper = int(input("Ievadi skaitli uz kura beigsies spēle(lielāks par iepriekšējo) :- "))

    # Tiek nejauši izvēlēts random skaitlis no lietotāja izvēlētā apgabala, kas būs skaitlis, kas jāuzmin
    # __________ vietā ieraksti vajadzīgo library
    x = random.randint(lower, upper)

    # Attiecīgi norādītajam apgabalam tiek izrēķināts atbilstošs mēģinājumu skaits
    print("\n\tTev ir tikai ", round(math.log(upper - lower + 1, 2)),
          " mēģinājumi uzminēt skaitli!\n")

    # Skaitītājs minējumiem.
    count = 0

    while count < math.log(upper - lower + 1, 2):
        count += 1
        guess = int(input("Uzmini skaitli:- "))
        # __ ievadi ar kuru mainīgo tiks salīdzināts guess
        if x == guess:
            print("Apsveicu, Tu uzvarēji ar ", count, " mēģinājumiem")
            break
        elif x > guess:
            print("Tavs minējums ir pārāk mazs!")
        elif x < guess:
            print("Tavs minējums ir pārāk liels!")

    if count >= math.log(upper - lower + 1, 2):
        print("\nSkaitlis ir% d" % x)
        print("\tVēlu veiksmi nākamreiz")

    return 0



def welcome_text(text):
    print(f'Hi, {text}')
    # Izsauc game_function, funkcijai nav jānorāda nekādi parametri

if __name__ == '__main__':
    game_function()
    welcome_text("do u wanna play more? Just rerun me :D")
