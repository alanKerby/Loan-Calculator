import argparse
import math

parser = argparse.ArgumentParser(description="Loan credit calculator")
parser.add_argument("-t", "--type", choices=['annuity', 'diff'], help="""
What do you want to calculate?
type "annuity" for annuity monthly payment amount,
type "diff" for monthly differentiated payment:
""")
parser.add_argument("-l", "--principal", type=float, help="Initial loan amount?")
parser.add_argument("-n", "--periods", type=int, help="Number of months?")
parser.add_argument("-i", "--interest", type=float, help="Annual percentage rate?")
parser.add_argument("-m", "--payment", type=float, help="Monthly payment?")

args = parser.parse_args()
type = args.type
principal = args.principal
periods = args.periods
interest = args.interest
payment = args.payment

arg_list = [type, principal, periods, interest, payment]
count = 0
for arg in arg_list:
    if arg is not None:
        count = count + 1

if count < 4:
    print('Incorrect parameters.')
    exit()

if interest is not None:
    interest = interest / 1200

if type == 'annuity':
    if principal is not None and periods is not None and interest is not None:
        x = math.pow(1 + interest, periods)
        annuity = math.ceil(principal * ((interest * x) / (x - 1)))
        balance = round(abs(principal - (annuity * periods)))
        print(f"Your annuity payment {annuity}!")
        print(f"Overpayment = {balance}")
    if payment is not None and periods is not None and interest is not None:
        x = math.pow(1 + interest, periods)
        p = math.floor(payment / ((interest * x) / (x - 1)))
        print(f'Your loan principal = {p}!')
        print(f"Overpayment = {round((payment * periods) - p)}")

    if principal is not None and payment is not None and interest is not None:
        x = (payment / (payment - interest * principal))
        months = math.ceil(math.log(x, 1 + interest))
        years = int(months / 12)
        and_months = months % 12
        if and_months == 0:
            print(f"It will take {years} years to repay this loan!")
        else:
            print(f"It will take {years} years and {and_months} months to repay this loan!")
        print(f"Overpayment = {round((payment * months - principal))}")

if type == 'diff':
    if principal is not None and periods is not None and interest is not None:
        balance = principal
        for i in range(1, periods + 1):
            payment = math.ceil(principal / periods + (interest * (principal - ((principal * (i - 1)) / periods))))
            print(f"Month {i}: payment is {payment}")
            balance = balance - payment
        print(f"\nOverpayment = {round(abs(balance))}")
    else:
        print('Incorrect parameters.')
        exit()
