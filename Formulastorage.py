allFormulas = {}

while True:

    print("\nformula thing")
    print("1 add")
    print("2 show")
    print("3 search")
    print("4 delete")
    print("5 leave")

    x = input("enter option : ")

    if x == "1":

        n = input("name maybe : ")

        f = input("formula write here : ")

        if n == "" or f == "":

            print("nothing entered bruh")

        else:

            allFormulas[n] = f

            print("formula saved i think")

    elif x == "2":

        if len(allFormulas) == 0:

            print("empty rn")

        else:

            for i in allFormulas:

                print(i + " -> " + allFormulas[i])

    elif x == "3":

        s = input("search formula : ")

        if s in allFormulas:

            print("got it")
            print(allFormulas[s])

        else:

            print("not found maybe")

    elif x == "4":

        d = input("which one delete : ")

        if d in allFormulas:

            allFormulas.pop(d)

            print("deleted now")

        else:

            print("its not even there")

    elif x == "5":

        print("Alright closing")
        break

    else:

        print("Wrong thing entered")