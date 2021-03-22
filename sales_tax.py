#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Sep 2020
# This program calculates total from subtotal and tax


import constants


def main():
    # this function calculates total from subtotal and tax

    # input
    sub_total = float(input("Enter the subtotal: $"))

    # process
    tax = sub_total * constants.HST
    total = sub_total + tax

    # output
    print("")
    print("The HST is ${0:,.2f}, and the total cost is: ${1:,.2f}".format(tax, total))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
