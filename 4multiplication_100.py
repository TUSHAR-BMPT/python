"""
Create a program that prints a multiplication
table for a given number until it reaches a result
that is more than hundred.
"""
def main():
    result=0
    number=int(input("Choose a number: "))
    count=1

    while result<=100:
        result=count*number
        print(f"{count} * {number} = {result}")
        count=count+1



if __name__=="__main__":
    main()