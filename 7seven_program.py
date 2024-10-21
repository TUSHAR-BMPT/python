"""
Purchase price: 12
Paid amount of money: 50
Offer change:
3 ten-euro notes
1 five-euro notes
1 two-euro coins
1 one-euro coins
"""
def main():
    price_money=int(input("Purchase price: "))
    paid_money=int(input("Paid amount of money: "))
    return_money=paid_money-price_money
    if return_money > 0:
        print("Offer change:")
        if return_money >=10:
            ten_euro_note = int(return_money / 10)
            remainder_ten = int(return_money % 10)
            print(f"{ten_euro_note} ten-euro notes")

            if 5<=remainder_ten<10:
                five_euro_note = int(remainder_ten / 5)
                remainder_five = int(remainder_ten % 5)
                print(f"{five_euro_note} five-euro notes")


                if 2<=remainder_five <5:
                    two_euro_note = int(remainder_five / 2)
                    remainder_two = int(remainder_five % 2)
                    print(f"{two_euro_note} two-euro coins")

                    if remainder_two == 1:
                        print(f"{remainder_two} one-euro coins")


                elif remainder_five == 1:
                    print(f"{remainder_five}one-euro coins")



            elif 2<=remainder_ten <5:
                two_euro_note = int(remainder_ten / 2)
                remainder_two = int(remainder_ten % 2)
                print(f"{two_euro_note} five-euro notes")



            elif remainder_ten==1:
                print(f"{remainder_ten} one-euro coins")










        elif 5<=return_money<10:
                five_euro_note = int(return_money / 5)
                remainder_five = int(return_money % 5)
                print(f"{five_euro_note} five-euro notes")

                if 2<=remainder_five <5:
                    two_euro_note = int(remainder_five / 2)
                    remainder_two = int(remainder_five % 2)
                    print(f"{two_euro_note} two-euro coins")

                    if remainder_two == 1:
                        print(f"{remainder_two} one-euro coins")




                if remainder_five ==1:
                    print(f"{remainder_five} one-euro coins")

        elif 2<=return_money<5:
            two_euro_note = int(return_money /2)
            remainder_two = int(return_money % 2)
            print(f"{two_euro_note} two-euro coins")

            if remainder_two==1:
                print(f"{remainder_two} one-euro coins")




        elif return_money==1:
            print(f"{return_money} one-euro coins")





    else:
        print("No change")



if __name__=="__main__":
    main()