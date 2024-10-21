"""
Bored? (y/n) o
Incorrect entry.
Bored? (y/n) z
Incorrect entry.
Bored? (y/n) m
Incorrect entry.
Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) f
Incorrect entry.
Bored? (y/n) j
Incorrect entry.
Bored? (y/n) y
Well, let's stop this, then.
Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) y
Well, let's stop this, then.
"""
def main():
    count=True

    while count:
        question = input("Bored? (y/n) ")
        if question=="y":
            print("Well, let's stop this, then.")
            count=False
        elif question=="n":
            count=True
        else:
            print("Incorrect entry.")



if __name__=="__main__":
    main()