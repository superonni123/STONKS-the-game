import random
import time

money = 0

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
    if cmd == 'exit':
        break

    elif cmd == "help":
        print("")
        print("Help     show this page")
        print("Exit     exits the game")
        print("Work     you gain money from working")
        print("Money    shows how many money you got")

    elif cmd == "money":
        print("you have " + str(money) + " money")

    elif cmd == "work":
        money_add = random.randrange(5, 20, 1)
        print("you gained " + str(money_add) + " money from work")
        money = money + money_add
