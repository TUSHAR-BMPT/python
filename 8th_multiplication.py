"""
Format the program's printout so that each multiplication result is shown in a printout field, which is four characters wide.
"""
def main():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i*j:4}",end="")
        print()

if __name__ == "__main__":
    main()
