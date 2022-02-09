
#stlye points
def bars():
    print("-0=TTTTTTTTTTTTTTTTTTTTTTTTTT=0-")
#importing random lib
import random
import numpy
#randomizing alien and player health
def healthRan():
    global enH
    global pH
    enH = random.randint(400, 800)
    pH = random.randint(400, 800)
#unused style points
def spacing():
    print("..............")
#normal build ship gui
def ship_one():
    print("..............-l-........+.....")
    print(".....+........[H]..............")
    print("...........+..]-[..............")
def ship_two():
    print("..............)=(............+.")
    print(".........+....-0-..............")
    print(".............. 8 .........+....")
#broken ship gui
def ship_one_boom():
    print("...boom....-....1..-....+.....")
    print(".....+..[.......H.....]...boom.")
    print(".......]....+......-......[...")
def ship_two_boom():
    print("......).........=.......(....+.")
    print("...-.....+....0........-..boom.")
    print("...boom............8......+....")

#player shooting
def pew():
    global enH
    print("pew")
    enH = enH - random.randint(10,20)
#enemy shooting
def epew():
    global pH
    print("pew pew")
    pH = pH - random.randint(10, 20)
#main file
def shoot():
    global enH
    global pH
    healthRan()
    while True:
        bars()
        ship_two()
        print(" ")
        print(" ")
        ship_one()
        bars()
        x = input(": ")
        pew()
        print("Enemy health is: ")
        print(enH)
        epew()
        print("Player health is: ")
        print(pH)
        if enH < 0:
            bars()
            print("You won")
            ship_two_boom()
            print(" ")
            print(" ")
            ship_one()
            bars()
            x = input(": ")
            break
        elif pH < 0:
            bars()
            print("You lost :(")
            ship_two()
            print(" ")
            print(" ")
            ship_one_boom()
            bars()
            x = input(": ")
            break
        else:
            continue
    print("--Time for a new round--")
    shoot()
#game starter
def start():
    bars()
    print("--Space game--")
    x = input("--press enter to start--")
    shoot()
start()
