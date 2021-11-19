import argparse
import math

parser: argparse = argparse.ArgumentParser(description="Loan credit calculator")
parser.add_argument("-t", "--type_", choices=['annuity', 'diff'], help="type_ 'annuity' or 'diff")
parser.add_argument("-l", "--principal", type=float, help="Initial loan amount? (decimal number)")
parser.add_argument("-n", "--periods", type=int, help="Number of months? (whole number)")
parser.add_argument("-i", "--interest", type=float, help="Annual percentage rate? (decimal number)")
parser.add_argument("-m", "--payment", type=float, help="Monthly payment? (decimal number)")


class Params():
    args = parser.parse_args()
    type_ = args.type_
    principal = args.principal
    periods = args.periods
    interest = args.interest
    payment = args.payment


def interest_mod():
    if Params.interest is not None:
        Params.interest = Params.interest / 1200


def parameter_check(type_, principal, periods, interest, payment):
    if type_ == 'annuity':
        if principal is not None and periods is not None and interest is not None:
            annuity_payment(principal, periods, interest)
        elif payment is not None and periods is not None and interest is not None:
            annuity_principal(payment, periods, interest)
        elif principal is not None and payment is not None and interest is not None:
            annuity_loan_period(principal, payment, interest)
        else:
            incorrect_params()
    elif type_ == 'diff' and principal is not None and periods is not None and interest is not None:
        print(Params.type_, Params.principal, Params.periods, Params.interest, Params.payment)
        monthly_diff(principal, periods, interest)
    else:
        incorrect_params()


def incorrect_params():
    print('Incorrect Params.')
    manual_input()


def manual_input():
    Params.type_ = input("type_ 'annuity' or 'diff: ")
    if Params.type_ == 'annuity':
        option = input("""
        What do you want to calculate?
        type_ "n" for number of monthly payments,
        type_ "a" for annuity monthly payment amount,
        type_ "p" for loan principal:
            """)
        if option != 'p':
            Params.principal = float(input("Enter the loan principal: "))
        if option != 'a':
            Params.payment = float(input("Enter the monthly payment: "))
        if option != 'n':
            Params.periods = int(input("Enter the number of periods: "))
    elif Params.type_ == 'diff':
        Params.principal = float(input("Enter the loan principal: "))
        Params.periods = int(input("Enter the number of periods: "))

    Params.interest = float(input("Enter the loan interest: "))
    interest_mod()
    print(Params.type_, Params.principal, Params.periods, Params.interest, Params.payment)
    parameter_check(Params.type_, Params.principal, Params.periods, Params.interest, Params.payment)


def annuity_payment(principal, periods, interest):
    x = math.pow(1 + interest, periods)
    annuity = math.ceil(principal * ((interest * x) / (x - 1)))
    balance = round(abs(principal - (annuity * periods)))
    print(f"Your annuity payment {annuity}!")
    print(f"Overpayment = {balance}")


def annuity_principal(payment, periods, interest):
    x = math.pow(1 + interest, periods)
    p = math.floor(payment / ((interest * x) / (x - 1)))
    print(f'Your loan principal = {p}!')
    print(f"Overpayment = {round((payment * periods) - p)}")


def annuity_loan_period(principal, payment, interest):
    x = (payment / (payment - interest * principal))
    months = math.ceil(math.log(x, 1 + interest))
    years = int(months / 12)
    and_months = months % 12
    if and_months == 0:
        print(f"It will take {years} years to repay this loan!")
    else:
        print(f"It will take {years} years and {and_months} months to repay this loan!")
    print(f"Overpayment = {round((payment * months - principal))}")


def monthly_diff(principal, periods, interest):
    balance = principal
    for i in range(1, periods + 1):
        payment = math.ceil(principal / periods + (interest * (principal - ((principal * (i - 1)) / periods))))
        print(f"Month {i}: payment is {payment}")
        balance = balance - payment
    print(f"\nOverpayment = {round(abs(balance))}")


interest_mod()
parameter_check(Params.type_, Params.principal, Params.periods, Params.interest, Params.payment)



