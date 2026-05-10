import time
import os

red = "\033[91m"
green = "\033[92m"
blue = "\033[96m"
yellow = "\033[93m"
end = "\033[0m"
bold = "\033[1m"


while True:
    os.system("cls" if os.name == "nt" else "clear")

    print(blue + bold + "============================")
    print("      simple timer")
    print("============================" + end)

    sec = input(yellow + "\nenter seconds : " + end)

    try:
        sec = int(sec)
    except:
        print(red + "bro thats not a number" + end)
        time.sleep(1.5)
        continue

    if sec < 0:
        print(red + "enter positive number only" + end)
        time.sleep(1.5)
        continue

    while sec >= 0:
        os.system("cls" if os.name == "nt" else "clear")

        mins = sec // 60
        left = sec % 60

        print(blue + bold + "============================")
        print("      simple timer")
        print("============================" + end)

        print(green + bold + f"\n         {mins:02d}:{left:02d}\n" + end)

        time.sleep(1)
        sec -= 1

    print(red + bold + "time finished !!" + end)

    again = input(yellow + "\nrun again? y/n : " + end).lower()

    if again != "y":
        print("closing...")
        break