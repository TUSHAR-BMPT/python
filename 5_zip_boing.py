"""
    Implement a program that makes a cheat sheet
    for as many numbers as the player wants.
    The program should first ask how many numbers
    the cheat sheet should include and then print them in 
    correct order (with all the zips, boings and zip boings).
"""
def main():
    input_number=int(input("How many numbers would you like to have? "))
    count=1
    while count<=input_number:
        if count%21==0:
            print("zip boing")
        elif count%3==0:
            print("zip")
        elif count%7==0:
            print("boing")
        elif count%21==0:
            print("zip boing")
        else:
            print(count)
        count=count+1



if __name__=="__main__":
    main()