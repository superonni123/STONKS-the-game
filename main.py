import os
import random
import socket
import sys
import threading
import time

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)

money = 0
owned_stock1 = 0
owned_stock2 = 0
owned_stock3 = 0
owned_stock4 = 0
owned_stock5 = 0
stock1price = random.randrange(10, 100)
stock2price = random.randrange(30, 500)
stock3price = random.randrange(69, 420)
stock4price = random.randrange(123, 666)
stock5price = random.randrange(88, 176)
osinko1 = stock1price * 0.035 * owned_stock1
osinko2 = stock2price * 0.05 * owned_stock2
osinko3 = stock3price * 0.08 * owned_stock3
osinko4 = stock4price * 0.04 * owned_stock4
osinko5 = owned_stock5 * 0.69 * owned_stock5
round_osinko = round(osinko1) + round(osinko2) + round(osinko3) + round(osinko4) + round(osinko5)
dont_use_me = 0
exi = 0
energy = 100
energy_max = 100
work_min = 5
work_max = 20
work_min_up = 0
work_max_up = 0
energy_gain_min = 5
energy_gain_max = 20
energy_up = 0
energy_max_up = 0


def background():
    while True:
        global stock1price
        global stock2price
        global stock3price
        global stock4price
        global stock5price
        global owned_stock1
        global owned_stock2
        global owned_stock3
        global owned_stock4
        global owned_stock5
        global osinko1
        global osinko2
        global osinko3
        global osinko4
        global osinko5
        global round_osinko
        global money

        time.sleep(15)
        osinko1 = stock1price * 0.035 * owned_stock1
        osinko2 = stock2price * 0.05 * owned_stock2
        osinko3 = stock3price * 0.08 * owned_stock3
        osinko4 = stock4price * 0.04 * owned_stock4
        osinko5 = owned_stock5 * 0.069 * owned_stock5
        round_osinko = round(osinko1) + round(osinko2) + round(osinko3) + round(osinko4) + round(osinko5)
        money = money + round_osinko

        a1 = random.randrange(0, 1000000, 1)

        if (a1 == 42069) or (a1 == 69420):
            print("nice")
            stock1price = stock1price + 10000

        elif a1 > 500000:
            stock1price = stock1price + random.randrange(1, 100, 1)

        elif a1 < 500000:
            stock1price = stock1price - random.randrange(1, 100, 1)

        if stock1price < 10:
            stock1price = 10

        a2 = random.randrange(0, 100, 1)

        if a2 > 50:
            stock2price = stock2price + random.randrange(1, 120, 1)

        elif a2 < 50:
            stock2price = stock2price - random.randrange(1, 120, 1)

        if stock2price < 30:
            stock2price = 30

        a3 = random.randrange(0, 100, 1)

        if a3 > 50:
            stock3price = stock3price + random.randrange(1, 140, 1)

        elif a3 < 50:
            stock3price = stock3price - random.randrange(1, 140, 1)

        if stock3price < 69:
            stock3price = 69

        a4 = random.randrange(0, 68)

        if a4 > 34:
            stock4price = stock4price + random.randrange(1, 435, 1)

        elif a4 < 34:
            stock4price = stock4price - random.randrange(1, 435, 1)

        if stock4price < 123:
            stock4price = 123

        a5 = random.randrange(1, 10, 1)

        if a5 > 5:
            stock5price = stock5price + random.randrange(1, 180, 1)

        elif a5 < 5:
            stock5price = stock5price - random.randrange(1, 180, 1)

        if stock5price < 88:
            stock5price = 88


def clear():
    print("")



b = threading.Thread(name='background', target=background)

b.start()

print("initiating loading")
time.sleep(0.5)
print("loading .")
time.sleep(0.5)
print("loading ..")
time.sleep(0.5)
print("loading ...")
time.sleep(0.5)
print("loading complete")
time.sleep(0.5)
print("")

print('welcome to STONKS the game')
name = input("what is your name (for online leaderboard): ")
while True:
    print("")
    cmd = input("what do you want to do: ")

    if cmd == "gui":
        window = QWidget()
        window.setWindowTitle('STONKS-GUI')
        window.setGeometry(150, 125, 2500, 500)
        window.move(60, 15)
        helloMsg = QLabel('<h1>STONKS</h1>', parent=window)
        helloMsg.move(60, 15)

        window.show()
        sys.exit(app.exec_())

    if cmd == "help":
        print("")
        print("help         show this page")
        print("save         saves the game")
        print("load         loads your game")
        print("credits      nice people go here :D")
        print("work         you gain money from working")
        print("stat         shows how many money, stocks and how big interest you got")
        print("shop         you can purchase upgrades")
        print("stonks       enters STONKS mode")
        print("sleep        you gain energy")
        print("roll         remember the house always wins")
        print("upload       uploads your save to online leaderboard")

    elif cmd == "stat":
        print("")
        print("     " + name)
        print("")
        bar_energy = energy / energy_max
        if bar_energy == 1:
            print("   ENERGY")
            print("[==========]")
            print("Energy: " + str(energy) + "/" + str(energy_max))
            print("")
        elif 0.9 <= float(bar_energy) < 1:
            print("   ENERGY")
            print("[========= ]")
            print("Energy: " + str(energy) + "/" + str(energy_max))
            print("")
        elif 0.8 <= float(bar_energy) < 0.9:
            print("   ENERGY")
            print("[========  ]")
            print("Energy: " + str(energy) + "/" + str(energy_max))
            print("")
        elif 0.7 <= float(bar_energy) < 0.8:
            print("   ENERGY")
            print("[=======   ]")
            print("Energy: " + str(energy) + "/" + str(energy_max))
            print("")
        elif 0.6 <= float(bar_energy) < 0.7:
            print("   ENERGY")
            print("[======    ]")
            print("Energy: " + str(energy) + "/" + str(energy_max))
            print("")
        elif 0.5 <= float(bar_energy) < 0.6:
            print("   ENERGY")
            print("[=====     ]")
            print("Energy: " + str(energy) + "/" + str(energy_max))
            print("")
        elif 0.4 <= float(bar_energy) < 0.5:
            print("   ENERGY")
            print("[====      ]")
            print("Energy: " + str(energy) + "/" + str(energy_max))
            print("")
        elif 0.3 <= float(bar_energy) < 0.4:
            print("   ENERGY")
            print("[===       ]")
            print("Energy: " + str(energy) + "/" + str(energy_max))
            print("")
        elif 0.2 <= float(bar_energy) < 0.3:
            print("   ENERGY")
            print("[==        ]")
            print("Energy: " + str(energy) + "/" + str(energy_max))
            print("")
        elif 0.1 <= float(bar_energy) < 0.2:
            print("   ENERGY")
            print("[=         ]")
            print("Energy: " + str(energy) + "/" + str(energy_max))
            print("")
        elif 0 <= float(bar_energy) < 0.1:
            print("   ENERGY")
            print("[          ]")
            print("Energy: " + str(energy) + "/" + str(energy_max))
            print("")
        print("you have " + str(money) + " money")
        print("your interest is " + str(round_osinko))
        print("")
        print("you have " + str(owned_stock1) + " stocks of Orb Industries")
        print("you have " + str(owned_stock2) + " stocks of Chair")
        print("you have " + str(owned_stock3) + " stocks of The Pile")
        print("you have " + str(owned_stock4) + " stocks of Chromble's Pool Service")
        print("you have " + str(owned_stock5) + " stocks of Onion Bot")

    elif cmd == "work":
        money_add = random.randrange(work_min, work_max, 1)
        energy_loss = random.randrange(1, 10, 1)
        if energy < energy_loss:
            print("you dont have enough energy")
            print("")
        else:
            energy = energy - int(energy_loss)
            print("you gained " + str(money_add) + " money from work and used " + str(energy_loss) + " energy")
            print("")
            money = money + money_add

    elif cmd == "roll":
        money = money - 20
        n1 = random.randrange(0, 6, 1)
        n2 = random.randrange(0, 6, 1)
        n3 = random.randrange(0, 6, 1)
        print("=====  =====  =====")
        print("| " + str(n1) + " | " " | " + str(n2) + " | "  " | " + str(n3) + " | ")
        print("=====  =====  =====")
        if n1 == n2 and n1 == n3:
            print("three same you have won 90 money")
            money = money + 90
        elif n1 == n2 or n1 == n3 or n2 == n3:
            print("two same you have won 35")
            money = money + 35
        else:
            print("better luck next time")

    elif cmd == "sleep":
        energy_add = random.randrange(energy_gain_min, energy_gain_max, 1) + energy_up
        print("you slept and regained " + str(energy_add) + " of energy")
        energy = energy + energy_add
        print("")
        if energy >= energy_max:
            energy = energy_max

    elif cmd == "credits":
        for _ in range(100):
            clear()
            print("thank you for looking here :D")
            time.sleep(2)
            dont_use_me = dont_use_me + 1
            if dont_use_me == 1:
                print("you know what i give you a bonus from this")
                money = money + 1000000000
            if dont_use_me == 2:
                print("did you think you get more")

            print("")
            break

    elif cmd == "load":
        f = open("save_data.txt", "rt")
        ID = f.readline()
        name = f.readline()
        money = f.readline()
        owned_stock1 = f.readline()
        owned_stock2 = f.readline()
        owned_stock3 = f.readline()
        owned_stock4 = f.readline()
        owned_stock5 = f.readline()
        energy_max_up = f.readline()
        work_min_up = f.readline()
        work_max_up = f.readline()
        energy_up = f.readline()
        f.close()

        ID = str(ID)
        name = str(name)
        money = int(money)
        owned_stock1 = int(owned_stock1)
        owned_stock2 = int(owned_stock2)
        owned_stock3 = int(owned_stock3)
        owned_stock4 = int(owned_stock4)
        owned_stock5 = int(owned_stock5)
        energy_max_up = int(energy_max_up)
        work_min_up = int(work_min_up)
        work_max_up = int(work_max_up)
        energy_up = int(energy_up)

        energy_max = energy_max + (energy_max_up * 5)
        work_min = work_min + (work_min_up * 1)
        work_max = work_max + (work_max_up * 1)
        energy_up = energy_up + (energy_up * 1)

        print("loading complete")

    elif cmd == "save":
        if not os.path.exists("save_data.txt"):
            ID = random.randrange(1000000000, 9999999999)
        if os.path.exists("save_data.txt"):
            os.remove("save_data.txt")
        f = open("save_data.txt", "w")
        f.write(str(ID) + "\n")
        f.write(str(name) + "\n")
        f.write(str(money) + "\n")
        f.write(str(owned_stock1) + "\n")
        f.write(str(owned_stock2) + "\n")
        f.write(str(owned_stock3) + "\n")
        f.write(str(owned_stock4) + "\n")
        f.write(str(owned_stock5) + "\n")
        f.write(str(energy_max_up) + "\n")
        f.write(str(work_min_up) + "\n")
        f.write(str(work_max_up) + "\n")
        f.write(str(energy_up) + "\n")
        f.close()
        print("saving complete")

    elif cmd == "upload":
        with socket.socket() as s:
            s.connect(('pphole.ddns.net', 9000))
            with open('save_data.txt', 'rb') as f:
                s.sendall(f.read())
        print("uploading completed")

    elif cmd == "stonks":
        print("you have entered STONKS mode")

        while True:

            cmd2 = input("action: ")
            if cmd2 == 'exit':
                print("you have exited STONKS mode")
                break

            elif cmd2 == 'help':
                print("this is invest mode help")
                print("")
                print("help     shows this page")
                print("exit     you should know what this command does")
                print("check    checks stock prices")
                print("buy      buy stocks")
                print("sell     sell stocks")

            elif cmd2 == 'check':
                print("you have " + str(money) + " money")
                print("")
                print("ID     STOCK                    price        owned")
                print("1       Orb Industries          " + str(stock1price) + "             " + str(owned_stock1))
                print("2       Chair                   " + str(stock2price) + "             " + str(owned_stock2))
                print("3       The Pile                " + str(stock3price) + "             " + str(owned_stock3))
                print("4       Chromble's Pool Service " + str(stock4price) + "             " + str(owned_stock4))
                print("5       Onion Bot               " + str(stock5price) + "             " + str(owned_stock5))
                print("")

            elif cmd2 == 'buy':
                IDb, buy = input("first enter ID then amount to buy: ").split()

                if IDb == str(1):
                    buy_cost1 = stock1price * int(buy)
                    if buy_cost1 > money:
                        print("you dont have enough money")
                        break
                    else:
                        money = money - buy_cost1
                        owned_stock1 = owned_stock1 + int(buy)
                        print("successfully bought " + str(buy) + " stocks of Orb Industries for " + str(buy_cost1))
                elif IDb == str(2):
                    buy_cost2 = stock2price * int(buy)
                    if buy_cost2 > money:
                        print("you dont have enough money")
                        break
                    else:
                        owned_stock2 = owned_stock2 + int(buy)
                        money = money - buy_cost2
                    print("successfully bought " + str(buy) + " stocks of Chair for " + str(buy_cost2))

                elif IDb == str(3):
                    buy_cost3 = stock3price * int(buy)
                    if buy_cost3 > money:
                        print("you dont have enough money")
                        break
                    else:
                        owned_stock3 = owned_stock3 + int(buy)
                        money = money - buy_cost3
                        print("successfully bought " + str(buy) + " stocks of The Pile for " + str(buy_cost3))

                elif IDb == str(4):
                    buy_cost4 = stock4price * int(buy)
                    if buy_cost4 > money:
                        print("you dont have enough money")
                        break
                    else:
                        owned_stock4 = owned_stock4 + int(buy)
                        money = money - buy_cost4
                        print("successfully bought " + str(buy) + " stocks of Chromble's Pool Service for " + str(
                            buy_cost4))

                elif IDb == str(5):
                    buy_cost5 = stock5price * int(buy)
                    if buy_cost5 > money:
                        print("you dont have enough money")
                        break
                    else:
                        owned_stock5 = owned_stock5 + int(buy)
                        money = money - buy_cost5
                        print("successfully bought " + str(buy) + " stocks of Onion Bot for " + str(buy_cost5))

            elif cmd2 == 'sell':
                IDs, sell = input("first enter ID then amount to sell: ").split()
                if IDs == str(1):
                    sell_cost1 = int(stock1price) * int(sell)
                    if str(owned_stock1) < str(sell):
                        print("you dont have enough stocks")
                        break
                    else:
                        owned_stock1 = int(owned_stock1) - int(sell)
                        money = money + sell_cost1
                        print("successfully sold " + str(sell) + " stocks of Orb Industries " + str(sell_cost1))

                elif IDs == str(2):
                    sell_cost2 = int(stock2price) * int(sell)
                    if str(owned_stock2) < str(sell):
                        print("you dont have enough stocks")
                        break
                    else:
                        owned_stock2 = int(owned_stock2) - int(sell)
                        money = money + sell_cost2
                        print("successfully sold " + str(sell) + " stocks of Chair for " + str(sell_cost2))

                elif IDs == str(3):
                    sell_cost3 = int(stock3price) * int(sell)
                    if str(owned_stock3) < str(sell):
                        print("you dont have enough stocks")
                        break
                    else:
                        owned_stock3 = int(owned_stock3) - int(sell)
                        money = money + sell_cost3
                        print("successfully sold " + str(sell) + " stocks of The Pile for " + str(sell_cost3))

                elif IDs == str(4):
                    sell_cost4 = int(stock4price) * int(sell)
                    if str(owned_stock4) < str(sell):
                        print("you dont have enough stocks")
                        break
                    else:
                        owned_stock4 = int(owned_stock4) - int(sell)
                        money = money + sell_cost4
                        print("successfully sold " + str(sell) + " stocks of Chromble's Pool Service for " + str(
                            sell_cost4))

                elif IDs == str(5):
                    sell_cost5 = int(stock5price) * int(sell)
                    if str(owned_stock5) < str(sell):
                        print("you dont have enough stocks")
                        break
                    else:
                        owned_stock5 = int(owned_stock5) - int(sell)
                        money = money + sell_cost5
                        print("successfully sold " + str(sell) + " stocks of Onion Bot for " + str(sell_cost5))

    elif cmd == "shop":
        print("Welcome to M karket")

        while True:
            cmd3 = input("what do you want to buy: ")

            if cmd3 == "exit":
                print("you have exited M karket")
                break

            elif cmd3 == "help":
                print("exit     you know")
                print(
                    "help     you should know by now if you don't then this might be very " + '\033[1m' + ' helpful '
                    + '\033[0m' + "https://www.dictionary.com/browse/help")
                print("inv      shows you what you can buy")
                print("buy      buy items")

            elif cmd3 == "inv":
                print("you have " + str(money) + " money")
                print("")
                print("ID           NAME            COST        OWNED")
                print("1            work min up     10          " + str(work_min_up))
                print("2            work max up     10          " + str(work_max_up))
                print("3            sleep up        15          " + str(energy_up))
                print("4            max energy up   30          " + str(energy_max_up))
                print("")

            elif cmd3 == "buy":
                IDi = input("enter the ID of the item you want to purchase: ")

                if IDi == str(1):
                    if work_min == work_max:
                        print("you cant upgrade this more")
                        break
                    elif money < 10:
                        print("you dont have enough money")
                        break
                    else:
                        work_min_up = work_min_up + 1
                        money = money - 10
                        work_min = work_min + work_min_up

                elif IDi == str(2):
                    if money < 10:
                        print("you dont have enough money")
                        break
                    else:
                        work_max_up = work_max_up + 1
                        money = money - 10
                        work_max = work_max + work_max_up

                elif IDi == str(3):
                    if money < 15:
                        print("you dont have enough money")
                        break
                    else:
                        energy_up = energy_up + 1
                        money = money - 15

                elif IDi == str(4):
                    if money < 30:
                        print("you dont have enough money")
                        break
                    else:
                        energy_max_up = energy_max_up + 1
                        money = money - 30
                        energy_max = energy_max + 5
