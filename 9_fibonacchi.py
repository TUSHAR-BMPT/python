"""
How many Fibonacci numbers do you want? 7
1. 1
2. 1
3. 2
4. 3
5. 5
6. 8
7. 13
"""
def main():
    enter_number=int(input("How many Fibonacci numbers do you want? "))
    fibonacchi=0
    a=0
    b=1


    for count in range(1,enter_number+1):

        fibonacchi=a+b
        print(f"{count}fibonacchi)
        b=a
        a=fibonacchi


if __name__=="__main__":
    main()