import matplotlib.pyplot as plt

apps = []
hours = []

print("mobile usage analyzer started\n")

totalApps = input("how many apps to enter : ")

try:

    totalApps = int(totalApps)

except:

    print("input was not correct so using 3")
    totalApps = 3

i = 0

while i < totalApps:

    appName = input("\nenter app name : ")

    usedTime = input("enter hours used : ")

    try:

        usedTime = float(usedTime)

    except:

        print("could not read the number so using 0")
        usedTime = 0

    apps.append(appName)

    hours.append(usedTime)

    i += 1

print("\nshowing entered data\n")

x = 0

while x < len(apps):

    print(str(x + 1) + ".", apps[x], "-", hours[x], "hours")

    x += 1

plt.pie(hours, labels=apps, autopct="%1.1f%%")

plt.title("daily mobile usage")

plt.show()

total = 0

for h in hours:

    total = total + h

print("\ntotal screen time =", total, "hours")

if total > 10:

    print("screen time is very high")

elif total > 5:

    print("screen time is moderate")

else:

    print("screen time is low")