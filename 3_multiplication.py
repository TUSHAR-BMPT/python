"""
Choose a number: 6
1 * 6 = 6
2 * 6 = 12
3 * 6 = 18
...
10 * 6 = 60
"""
def main():
    count=1
    number=int(input("Choose a number: "))

    while count<=10:
        result=count*number
        print(f"{count} * {number} = {result}")
        count=count+1




if __name__=="__main__":
    main()