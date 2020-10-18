import random
import time
import threading
import sys

money = 0
owned_stock1 = 0
stock1price = random.randrange(10, 100, 1)
dont_use_me = 0
osinko = stock1price * 0.035 * owned_stock1
round_osinko = round(osinko)
exi = 0


def background():
    while True:
        global stock1price
        global round_osinko
        global osinko
        global money
        global owned_stock1

        time.sleep(10)
        osinko = stock1price * 0.035 * owned_stock1
        money = money + osinko
        round_osinko = round(osinko)
        if osinko > 0:
            a = random.randrange(0, 1000000, 1)

            if (a == 42069) or (a == 69420):
                print("nice")
                stock1price = stock1price + 10000

            elif a > 500000:
                stock1price = stock1price + random.randrange(1, 100, 1)

            elif a < 500000:
                stock1price = stock1price - random.randrange(1, 100, 1)

            if stock1price < 10:
                stock1price = 10


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
        print("you have " + str(owned_stock1) + " stock-1")
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
            break

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
                print("stock 1 costs " + str(stock1price) + " money")
                print("")

            elif cmd2 == 'buy':
                buy = int(input("how many stocks to buy: "))
                owned_stock1 = owned_stock1 + buy
                money = money - (stock1price * buy)
                print("successfully bought " + str(buy) + " stocks")
                if money < 0:
                    print("you dont have enough money")
                    sys.exit()

            elif cmd2 == 'sell':
                sell = int(input("how many stock to sell: "))
                owned_stock1 = owned_stock1 - sell
                money = money + (stock1price * sell)
                print("successfully sold " + str(sell) + " stocks")
                if owned_stock1 < 0:
                    print("you dont have enough stocks")
                    sys.exit()
