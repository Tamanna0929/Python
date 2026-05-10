
booksList = ["Python Basics", "Physics", "Chemistry"]

takenBooks = []

while True:

    print("\nlibrary tracker running")
    print("1 show books")
    print("2 take book")
    print("3 return book")
    print("4 close")

    option = input("choose something : ")

    if option == "1":

        print("\nbooks available right now\n")

        if len(booksList) == 0:

            print("library looks empty")

        else:

            i = 0

            while i < len(booksList):

                print(str(i + 1) + ".", booksList[i])

                i += 1

    elif option == "2":

        take = input("book name : ")

        if take in booksList:

            booksList.remove(take)

            takenBooks.append(take)

            print("book taken successfully")

        else:

            print("could not find that book")

    elif option == "3":

        giveBack = input("return book name : ")

        if giveBack in takenBooks:

            takenBooks.remove(giveBack)

            booksList.append(giveBack)

            print("book returned")

        else:

            print("this book was not taken before")

    elif option == "4":

        print("closing library system")
        break

    else:

        print("option not correct")