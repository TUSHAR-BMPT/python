"""
How do you feel? (1-10) 6
A suitable smiley would be :-|
"""
def main():
    feelings = int(input("How do you feel? (1-10) "))
    if 1<=feelings<=10:
        if feelings==10:
            print("A suitable smiley would be :-D")

        elif 7<feelings<10:
            print("A suitable smiley would be :-)")
        elif 4<=feelings<=7:
            print("A suitable smiley would be :-|")
        elif 1<feelings<4:
            print("A suitable smiley would be :-(")
        else :
            print("A suitable smiley would be :'(")
    else:
        print("Bad input!")

if __name__== "__main__":
    main()
