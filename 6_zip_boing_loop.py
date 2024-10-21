"""
Number series game Zip Boing Using for-loop
"""
def main():
    count = 1
    input_number=int(input("How many numbers would you like to have? "))
    for count in range(1,input_number+1):
        if count % 21 == 0:
            print("zip boing")
        elif count % 3 == 0:
            print("zip")
        elif count % 7 == 0:
            print("boing")
        elif count % 21 == 0:
            print("zip boing")
        else:
            print(count)
        count = count + 1
if __name__=="__main__":
    main()

