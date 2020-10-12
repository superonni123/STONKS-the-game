import random
import time

money = 0
owned_stock1 = 0
stock1price = random.randrange(1, 100, 1)

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

print("welcome to STONKS the game")
while True:
    print("")
    cmd = input("what do you want to do: ")

    if cmd == "help":
        print("")
        print("Help     show this page")
        print("Work     you gain money from working")
        print("Check    shows how many money and stocks you got")
        print("Invest   enters INVESTMENT mode")

    elif cmd == "check":
        print("you have " + str(money) + " money")
        print("you have " + str(owned_stock1) + " stock1")

    elif cmd == "work":
        money_add = random.randrange(5, 20, 1)
        print("you gained " + str(money_add) + " money from work")
        money = money + money_add

    elif cmd == "invest":
        print("you have entered INVESTMENT mode")

        while True:
            cmd2 = input("action: ")
            if cmd2 == 'exit':
                print("you have exited INVESTMENT mode")
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
                a = random.randrange(0, 10000000, 1)
                if a < 5:
                    stock1price = stock1price + random.randrange(1, 100, 1)

                elif a > 5:
                    stock1price = stock1price - random.randrange(1, 100, 1)

                print("stock 1 costs " + str(stock1price) + " money")
                print("")

            elif cmd2 == 'buy':
                buy = int(input("how many stocks to buy: "))
                owned_stock1 = owned_stock1 + buy
                money = money - (stock1price * buy)
                print("successfully bought " + str(buy) + " stocks")

            elif cmd2 == 'sell':
                sell = int(input("how many stock to sell: "))
                owned_stock1 = owned_stock1 - sell
                money = money + (stock1price * sell)
                print("successfully sold " + str(sell) + " stocks")
