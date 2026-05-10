tasks = []

while True:

    print("\n1 add")
    print("2 show")
    print("3 remove")
    print("4 exit")

    x = input("enter : ")

    if x == "1":

        t = input("task : ")

        if t != "":
            tasks.append(t)
            print("added")
        else:
            print("empty task lol")

    elif x == "2":

        if len(tasks) == 0:
            print("nothing here")

        else:

            n = 1

            for i in tasks:
                print(str(n) + ".", i)
                n += 1

    elif x == "3":

        if len(tasks) == 0:

            print("already empty")

        else:

            try:

                no = int(input("number : "))

                tasks.pop(no - 1)

                print("removed maybe")

            except:

                print("wrong input")

    elif x == "4":

        print("ok done")
        break

    else:

        print("what even is that option")