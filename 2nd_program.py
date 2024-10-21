"""
Answer Y or N: q
Incorrect entry.
Answer Y or N: w
Incorrect entry.
Answer Y or N: n
You answered n
Answer Y or N: Y
You answered Y
"""
def main():
    condition=True

    while condition:
        entry=input("Answer Y or N: ")

        if entry=="Y":
            print("You answered Y")
            condition=False

        elif entry=="N":
            print("You answered N")
            condition=False

        elif entry=="n":
            print("You answered n")
            condition=False

        elif entry=="y":
            print("You answered y")
            condition=False

        else:
            print("Incorrect entry.")












if __name__=="__main__":
    main()