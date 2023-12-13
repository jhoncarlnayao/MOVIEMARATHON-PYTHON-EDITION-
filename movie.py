import os
import time
import pyautogui
from collections import deque


price = deque()
food = deque()

ticket=False

def has_ticket():
    global ticket
    if not ticket: 
        input("Please purchase a ticket to access the movies, Press enter to continue")
        viewrates()  
        return False
    return True

def alttab():
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    time.sleep(0.005)
    pyautogui.keyUp('alt')
    
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    time.sleep(0.005) 
    pyautogui.keyUp('alt')
    
   


def clearconsole():
    os.system('cls' if os.name == 'nt' else 'clear')


def foodmenu():
    while True:
        clearconsole()
        print("=======================================================")
        print("================= Food and Drinks  ====================")
        print("=======================================================")


def ragnarok():
    while True:
        clearconsole()
        print("=======================================================")
        print("================ Ragnarok Season 1 ====================")
        print("=======================================================")
        print("                     Episode List:")
        print("               [1]: Episode 2")
        print("               [2]: Episode 3")
        print("               [3]: Episode 4")
        print("               [4]: Episode 5")
        print("               [5]: Episode 6")
        print("               [6]: Episode 7")
        print("               [7]: Episode 8")
        print("               [8]: Episode 9")
        print("               [9]: Episode 10")
        print("               [10]: Episode 11")
        print("               [11]: Episode 12")
        print("               [12]: Exit")
        print()
        choice = input("Input your Choice here: ")
        if choice == '1':
            print("╭──────────────────────────────────────────────────────╮")
            print("│                                                      │")
            print("│                Processing data. Please wait...       │")
            print("│                                                      │")
            print("╰──────────────────────────────────────────────────────╯")

            time.sleep(3)

            print("╭──────────────────────────────────────────────────────╮")
            print("│                                                      │")
            print("│          Data processing completed successfully!     │")
            print("│                                                      │")
            print("│                   ENJOY YOUR MOVIE!!!                │")
            print("│                                                      │")
            print("╰──────────────────────────────────────────────────────╯")

            episode2 = r"C:\PYTHON2NDYEAR\MY PROJECTS\AnimePahe_Shuumatsu_no_Walkure_-_02_1080p_Netflix.mp4"
            os.startfile(episode2)
            alttab()

        elif choice == '2':
            print("╭──────────────────────────────────────────────────────╮")
            print("│                                                      │")
            print("│                Processing data. Please wait...       │")
            print("│                                                      │")
            print("╰──────────────────────────────────────────────────────╯")
            time.sleep(3)
            print("╭──────────────────────────────────────────────────────╮")
            print("│                                                      │")
            print("│          Data processing completed successfully!     │")
            print("│                                                      │")
            print("│                   ENJOY YOUR MOVIE!!!                │")
            print("│                                                      │")
            print("╰──────────────────────────────────────────────────────╯")
            episode3 = r"C:\PYTHON2NDYEAR\MY PROJECTS\AnimePahe_Shuumatsu_no_Walkure_-_03_1080p_Netflix.mp4"
            os.startfile(episode3)
            alttab()
        elif choice == '3':
            print("╭──────────────────────────────────────────────────────╮")
            print("│                                                      │")
            print("│                Processing data. Please wait...       │")
            print("│                                                      │")
            print("╰──────────────────────────────────────────────────────╯")
            time.sleep(3)
            print("╭──────────────────────────────────────────────────────╮")
            print("│                                                      │")
            print("│          Data processing completed successfully!     │")
            print("│                                                      │")
            print("│                   ENJOY YOUR MOVIE!!!                │")
            print("│                                                      │")
            print("╰──────────────────────────────────────────────────────╯")
            episode4 = r"C:\PYTHON2NDYEAR\MY PROJECTS\AnimePahe_Shuumatsu_no_Walkure_-_04_1080p_Netflix.mp4"
            os.startfile(episode4)
            alttab()
        elif choice == '4':
            print("╭──────────────────────────────────────────────────────╮")
            print("│                                                      │")
            print("│                Processing data. Please wait...       │")
            print("│                                                      │")
            print("╰──────────────────────────────────────────────────────╯")
            time.sleep(3)
            print("╭──────────────────────────────────────────────────────╮")
            print("│                                                      │")
            print("│          Data processing completed successfully!     │")
            print("│                                                      │")
            print("│                   ENJOY YOUR MOVIE!!!                │")
            print("│                                                      │")
            print("╰──────────────────────────────────────────────────────╯")
            episode5 = r"C:\PYTHON2NDYEAR\MY PROJECTS\AnimePahe_Shuumatsu_no_Walkure_-_05_1080p_Netflix.mp4"
            os.startfile(episode5)
            alttab()
        elif choice == '5':
            print("╭──────────────────────────────────────────────────────╮")
            print("│                                                      │")
            print("│                Processing data. Please wait...       │")
            print("│                                                      │")
            print("╰──────────────────────────────────────────────────────╯")
            time.sleep(3)
            print("╭──────────────────────────────────────────────────────╮")
            print("│                                                      │")
            print("│          Data processing completed successfully!     │")
            print("│                                                      │")
            print("│                   ENJOY YOUR MOVIE!!!                │")
            print("│                                                      │")
            print("╰──────────────────────────────────────────────────────╯")
            episode6 = r"C:\PYTHON2NDYEAR\MY PROJECTS\AnimePahe_Shuumatsu_no_Walkure_-_06_1080p_Netflix.mp4"
            os.startfile(episode6)
            alttab()
        elif choice == '6':
            print("╭──────────────────────────────────────────────────────╮")
            print("│                                                      │")
            print("│                Processing data. Please wait...       │")
            print("│                                                      │")
            print("╰──────────────────────────────────────────────────────╯")
            time.sleep(3)
            print("╭──────────────────────────────────────────────────────╮")
            print("│                                                      │")
            print("│          Data processing completed successfully!     │")
            print("│                                                      │")
            print("│                   ENJOY YOUR MOVIE!!!                │")
            print("│                                                      │")
            print("╰──────────────────────────────────────────────────────╯")
            episode7 = r"C:\PYTHON2NDYEAR\MY PROJECTS\AnimePahe_Shuumatsu_no_Walkure_-_07_1080p_Netflix.mp4"
            os.startfile(episode7)
            alttab()
        elif choice == '7':
            print("╭──────────────────────────────────────────────────────╮")
            print("│                                                      │")
            print("│                Processing data. Please wait...       │")
            print("│                                                      │")
            print("╰──────────────────────────────────────────────────────╯")
            time.sleep(3)
            print("╭──────────────────────────────────────────────────────╮")
            print("│                                                      │")
            print("│          Data processing completed successfully!     │")
            print("│                                                      │")
            print("│                   ENJOY YOUR MOVIE!!!                │")
            print("│                                                      │")
            print("╰──────────────────────────────────────────────────────╯")
            episode8 = r"C:\PYTHON2NDYEAR\MY PROJECTS\AnimePahe_Shuumatsu_no_Walkure_-_08_1080p_Netflix.mp4"
            os.startfile(episode8)
            alttab()
        elif choice == '8':
            print("╭──────────────────────────────────────────────────────╮")
            print("│                                                      │")
            print("│                Processing data. Please wait...       │")
            print("│                                                      │")
            print("╰──────────────────────────────────────────────────────╯")
            time.sleep(3)
            print("╭──────────────────────────────────────────────────────╮")
            print("│                                                      │")
            print("│          Data processing completed successfully!     │")
            print("│                                                      │")
            print("│                   ENJOY YOUR MOVIE!!!                │")
            print("│                                                      │")
            print("╰──────────────────────────────────────────────────────╯")
            episode9 = r"C:\PYTHON2NDYEAR\MY PROJECTS\AnimePahe_Shuumatsu_no_Walkure_-_09_1080p_Netflix.mp4"
            os.startfile(episode9)
            alttab()
        elif choice == '9':
            print("╭──────────────────────────────────────────────────────╮")
            print("│                                                      │")
            print("│                Processing data. Please wait...       │")
            print("│                                                      │")
            print("╰──────────────────────────────────────────────────────╯")
            time.sleep(3)
            print("╭──────────────────────────────────────────────────────╮")
            print("│                                                      │")
            print("│          Data processing completed successfully!     │")
            print("│                                                      │")
            print("│                   ENJOY YOUR MOVIE!!!                │")
            print("│                                                      │")
            print("╰──────────────────────────────────────────────────────╯")
            episode10 = r"C:\PYTHON2NDYEAR\MY PROJECTS\AnimePahe_Shuumatsu_no_Walkure_-_10_1080p_Netflix.mp4"
            os.startfile(episode10)
            alttab()
        elif choice == '10':
            print("╭──────────────────────────────────────────────────────╮")
            print("│                                                      │")
            print("│                Processing data. Please wait...       │")
            print("│                                                      │")
            print("╰──────────────────────────────────────────────────────╯")
            time.sleep(3)
            print("╭──────────────────────────────────────────────────────╮")
            print("│                                                      │")
            print("│          Data processing completed successfully!     │")
            print("│                                                      │")
            print("│                   ENJOY YOUR MOVIE!!!                │")
            print("│                                                      │")
            print("╰──────────────────────────────────────────────────────╯")
            episode11 = r"C:\PYTHON2NDYEAR\MY PROJECTS\AnimePahe_Shuumatsu_no_Walkure_-_11_1080p_Netflix.mp4"
            os.startfile(episode11)
            alttab()
        elif choice == '11':
            print("╭──────────────────────────────────────────────────────╮")
            print("│                                                      │")
            print("│                Processing data. Please wait...       │")
            print("│                                                      │")
            print("╰──────────────────────────────────────────────────────╯")
            time.sleep(3)
            print("╭──────────────────────────────────────────────────────╮")
            print("│                                                      │")
            print("│          Data processing completed successfully!     │")
            print("│                                                      │")
            print("│                   ENJOY YOUR MOVIE!!!                │")
            print("│                                                      │")
            print("╰──────────────────────────────────────────────────────╯")
            episode12 = r"C:\PYTHON2NDYEAR\MY PROJECTS\AnimePahe_Shuumatsu_no_Walkure_-_12_1080p_Netflix.mp4"
            os.startfile(episode12)
            alttab()
        elif choice == '12':
            main()


def viewrates():
    while True:
        clearconsole()
        global ticket
        print("=======================================================")
        print("=================    Movie Rates   ====================")
        print("=======================================================")
        print("                       Rates:")
        print("               [1]: 300 Good for 2 Person")
        print("               [2]: 160 Good for 1 Person")
        print("               [3]: 700 Barkada Pack")
        print("               [4]: 250 Lovers Pack")
        print("               [5]: 850 Family Pack")
        print("               [6]: Exit")
        print()
        choice = input("Input your Choice here: ")
        if choice == '1':
            ticket=True
            print("You choose Package 1")
            pack1 = 300.00
            money = float(input("Input your cash here: "))
            change = money-pack1
            print(f"Balance: {change}")
            input("Press enter to continue")
        elif choice == '2':
            print("You choose Package 2")
            pack2 = 160.00
            money = float(input("Input your cash here: "))
            change = money-pack2
            print(f"Balance: {change}")
            input("Press enter to continue")
        elif choice == '3':
            print("You choose Package 3")
            pack3 = 700.00
            money = float(input("Input your cash here: "))
            change = money-pack3
            print(f"Balance: {change}")
            input("Press enter to continue")
        elif choice == '4':
            print("You choose Package 4")
            pack4 = 250.00
            money = float(input("Input your cash here: "))
            change = money-pack4
            print(f"Balance: {change}")
            input("Press enter to continue")
        elif choice == '5':
            print("You choose Package 5")
            pack5 = 850.00
            money = float(input("Input your cash here: "))
            change = money-pack5
            print(f"Balance: {change}")
            input("Press enter to continue")
        elif choice == '6':
            break


def availablemovies():
    while True:
        global ticket
        clearconsole()
        print("=======================================================")
        print("================ Available Movies  ====================")
        print("=======================================================")
        print("                       Menu:")
        print("               [1]: Ragnarok (12 Episodes)")
        print("               [2]: Not yet Available")
        print("               [3]: Not yet Available")
        print("               [4]: Exit")
        print()
        choice = input("Input your Choice here: ")
        if choice == '1':
            if has_ticket():  
                ragnarok()
            else:
                return
        elif choice == '2':
            viewrates()
        elif choice == '3':
            print()
            
            
            
def foodanddrinks():
    while True:
        clearconsole()
        print("=======================================================")
        print("=============== Food and Drinks Area  =================")
        print("=======================================================")
        print("                       Menu:")
        print("             [1]: Normal Popcorn         (50 Pesos)")
        print("             [2]: Popcorn with Coca-cola (80 Pesos)")
        print("             [3]: Family Popcorn         (250 Pesos)")
        print("             [4]: Barkada Popcorn        (230 Pesos)")
        print("             [5]: Exit")
        print()
        choice = input("Input your Choice here: ")
        if choice =='1':
            print("You choose Normal Popcorn (50 Pesos)")
            food.append("Normal Popcorn")
            input("Press enter to continue.")
        elif choice =='2':
            print("You coose Popcorn with Coca-cola (80 Pesos)")
            food.append("Popcorn with Coca-cola")
            input("Press enter to continue.")
        elif choice =='3':
            print("You choose Family Popcorn (250 Pesos)")
            food.append("Family Popcorn")
            input("Press enter to continue.")
        elif choice =='4':
            print("You choose Barkada Popcorn (230 Pesos)")
            food.append("Barkada Popcorn")
            input("Press enter to continue.")
        elif choice =='5':
            break
        
        
    


def main():
    while True:
        clearconsole()
        print("=======================================================")
        print("======= CineCash: Your Virtual Movie Ticket  ==========")
        print("=======================================================")
        print("                       Menu")
        print("               [1]: View Available Movie")
        print("               [2]: View Rates")
        print("               [3]: Buy Food/Drinks")
        print()
        choice = input("Input your Choice here: ")
        if choice == '1':
            availablemovies()
        elif choice == '2':
            viewrates()
        elif choice =='3':
            foodanddrinks()


main()
