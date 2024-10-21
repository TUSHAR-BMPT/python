"""
Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) y
Well, let's stop this, then.
"""
def main():
    bored=True
    input_feelings=0

    while bored:
        input_feelings=input("Bored? (y/n) ")
        bored= input_feelings== "n"
    print("Well, let's stop this, then.")



if __name__=="__main__":
    main()