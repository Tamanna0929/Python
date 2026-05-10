import matplotlib.pyplot as plt

allNames = []
allMoney = []

print("expense tracker started maybe\n")

num = input("how many things u bought : ")

try:

    num = int(num)

except:

    print("not a number so using 2")
    num = 2

n = 0

while n < num:

    thing = input("\nwhat did u buy : ")

    price = input("money spent : ")

    try:

        price = float(price)

    except:

        print("amount issue,, taking 0")
        price = 0

    allNames.append(thing)

    allMoney.append(price)

    n += 1

print("\nexpenses list rn")

i = 0

while i < len(allNames):

    print(allNames[i], "-", allMoney[i])

    i += 1

plt.bar(allNames, allMoney)

plt.title("random expense graph")
plt.xlabel("items")
plt.ylabel("money gone")

plt.show()

tot = 0

for x in allMoney:

    tot = tot + x

print("\nspent total =", tot)