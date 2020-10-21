import random
import time
import threading
import sys

money = 0
owned_stock1 = 0
owned_stock2 = 0
stock1price = random.randrange(10, 100, 1)
stock2price = random.randrange(30, 500, 1)
osinko1 = stock1price * 0.035 * owned_stock1
osinko2 = stock2price * 0.05 * owned_stock2
round_osinko = round(osinko1) + round(osinko2)
dont_use_me = 0
exi = 0


def background():
    while True:
        global stock1price
        global stock2price
        global owned_stock1
        global owned_stock2
        global osinko1
        global osinko2
        global round_osinko
        global money

        time.sleep(8)
        osinko1 = stock1price * 0.035 * owned_stock1
        osinko2 = stock2price * 0.05 * owned_stock2
        round_osinko = round(osinko1) + round(osinko2)
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


b = threading.Thread(name='background', target=background)

b.start()

print("initiating loading")
time.sleep(1)
print("loading .")
time.sleep(1)
print("loading ..")
time.sleep(1)
print("loading ...")
time.sleep(1)
print("loading complete")
time.sleep(1)
print("")

print('welcome to STONKS the game')
while True:
    print("")
    cmd = input("what do you want to do: ")

    if cmd == "help":
        print("")
        print("help         show this page")
        print("work         you gain money from working")
        print("check        shows how many money, stocks and how big interest you got")
        print("stonks       enters STONKS mode")
        print("shutdown     shuts the game down")

    elif cmd == "check":
        print("you have " + str(money) + " money")
        print("you have " + str(owned_stock1) + " stocks of Orb Industries")
        print("you have " + str(owned_stock2) + " stocks of Chair")
        print("your interest is " + str(round_osinko))

    elif cmd == "work":
        money_add = random.randrange(5, 20, 1)
        print("you gained " + str(money_add) + " money from work")
        money = money + money_add

    elif cmd == 'OwO':
        dont_use_me = dont_use_me + 1
        print("OwO you found a easter egg good for you")
        print("unless you looked at the source code D:<")
        money = money + 1000000000
        if dont_use_me == 2:
            print("HEY don't use this easter egg twice!!")
            sys.exit(0)

    elif cmd == "shutdown":
        print("are you sure type 'shutdown again'")
        exi = exi + 1
        if exi == 2:
            print("game closed now you can close this window")
            sys.exit()

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
                print("ID     STOCK                    price        owned")
                print("")
                print("1       Orb Industries          " + str(stock1price) + "             " + str(owned_stock1))
                print("2       Chair                   " + str(stock2price) + "             " + str(owned_stock2))

            elif cmd2 == 'buy':
                ID, buy = input("first enter ID then amount to buy: ").split()

                if ID == str(1):
                    buy_cost1 = stock1price * int(buy)
                    if buy_cost1 > money:
                        print("you dont have enough money")
                        break
                    else:
                        money = money - buy_cost1
                        owned_stock1 = owned_stock1 + int(buy)
                        print("successfully bought " + str(buy) + " stocks of Orb Industries for " + str(buy_cost1))
                elif ID == str(2):
                    buy_cost2 = stock2price * int(buy)
                    if buy_cost2 > money:
                        print("you dont have enough money")
                        break
                    else:
                        owned_stock2 = owned_stock2 + int(buy)
                        money = money - buy_cost2
                    print("successfully bought " + str(buy) + " stocks of Chair for " + str(buy_cost2))

            elif cmd2 == 'sell':
                ID, sell = input("first enter ID then amount to sell: ").split()
                if ID == str(1):
                    sell_cost1 = int(stock1price) * int(sell)
                    if str(owned_stock1) < str(sell):
                        print("you dont have enough stocks")
                        break
                    else:
                        owned_stock1 = int(owned_stock1) - int(sell)
                        money = money + sell_cost1
                        print("successfully sold " + str(sell) + " stocks of Orb Industries " + str(sell_cost1))

                if ID == str(2):
                    sell_cost2 = int(stock2price) * int(sell)
                    if str(owned_stock2) < str(sell):
                        print("you dont have enough stocks")
                        break
                    else:
                        owned_stock2 = int(owned_stock2) - int(sell)
                        money = money + sell_cost2
                        print("successfully sold " + str(sell) + " stocks of Chair for " + str(sell_cost2))
