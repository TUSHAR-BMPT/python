"""
Tell us your name: Teemu
Hey Teemu, the printout formatting is going well!
"""
def main():
    name=input("Tell us your name: ")
    print(f"Hey {name},",end=" ")
    print("the printout formatting is going well!")

if __name__=="__main__":
    main()