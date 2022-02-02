import math
import argparse


def cal_differentiated_payment(principal_, periods_, interest_):
    principal_ = float(principal_)
    periods_ = int(periods_)
    interest_ = float(interest_)
    check_list = [principal_, periods_, interest_]
    is_negative = False
    for i in check_list:
        is_negative = check_negative(i)
        if is_negative is True:
            break
    if is_negative is False:
        i = (interest_ / 12) / 100
        sum_ = 0
        for x in range(1, periods_ + 1):
            result = math.ceil(principal_ / periods_ + i * (principal_ - (principal_ * (x - 1)) / periods_))
            sum_ += result
            print(f"Month 10: payment is {result}")
            over_payment = round(sum_ - principal_)
            print(f"\nOverpayment = {over_payment}")
    else:
        print("Incorrect parameters")


def cal_annuity_payment(principal_, periods_, interest_):
    principal_ = float(principal_)
    periods_ = float(periods_)
    interest_ = float(interest_)
    check_list = [principal_, periods_, interest_]
    is_negative = False
    for i in check_list:
        is_negative = check_negative(i)
        if is_negative is True:
            break
    if is_negative is False:
        i = (interest_ / 12) / 100
        above_part = i * math.pow(1 + i, periods_)
        bottom_part = math.pow(1 + i, periods_) - 1
        x = above_part / bottom_part
        annuity_p = math.ceil(principal_ * x)
        over_payment = round(annuity_p * periods_ - principal_)
        print(f"Your monthly payment = {annuity_p}!")
        print(f"Overpayment = {over_payment}")
    else:
        print("Incorrect parameters")


def cal_principal(payment_, periods_, interest_):
    payment_ = float(payment_)
    periods_ = float(periods_)
    interest_ = float(interest_)
    check_list = [payment_, periods_, interest_]
    is_negative = False
    for i in check_list:
        is_negative = check_negative(i)
        if is_negative is True:
            break
    if is_negative is False:
        i = (interest_ / 12) / 100
        above_part = i * math.pow(1 + i, periods_)
        bottom_part = math.pow(1 + i, periods_) - 1
        x = above_part / bottom_part
        loan_principal = math.floor(payment_ / x)
        over_payment = round(payment_ * periods_ - loan_principal)
        print(f"Your loan principal = {loan_principal}!")
        print(f"Overpayment = {over_payment}")
    else:
        print("Incorrect parameters")


def cal_number_of_monthly_payments(payment_, principal_, interest_):
    payment_ = float(payment_)
    principal_ = float(principal_)
    interest_ = float(interest_)
    check_list = [payment_, principal_, interest_]
    is_negative = False
    for i in check_list:
        is_negative = check_negative(i)
        if is_negative is True:
            break
    if is_negative is False:
        i = (interest_ / 12) / 100
        base = payment_ / (payment_ - i * principal_)
        number_of_payments = math.ceil(math.log(base, 1 + i))
        year, month = divmod(number_of_payments, 12)
        over_payment = round(payment_ * number_of_payments - principal_)
        if number_of_payments > 12 and year >= 1 and month != 0:
            print(f"It will take {year} years and {month} months to repay this loan!")
            print(f"Overpayment = {over_payment}")
        elif year >= 1 and month == 0:
            print(f"It will take {year} years to repay this loan!")
            print(f"Overpayment = {over_payment}")
        else:
            print(f"It will take {number_of_payments} months to repay this loan!")
            print(f"Overpayment = {over_payment}")
    else:
        print("Incorrect parameters")


def check_negative(s):
    try:
        f = float(s)
        if f < 0:
            return True
        return False
    except ValueError:
        return False


parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")
args = parser.parse_args()

type_ = args.type
periods = args.periods
principal = args.principal
payment = args.payment
interest = args.interest


if type_ == "diff":
    if None not in (principal, periods, interest):
        cal_differentiated_payment(principal, periods, interest)
    else:
        print("Incorrect parameters")
elif type_ == "annuity":
    if None not in (principal, periods, interest):
        cal_annuity_payment(principal, periods, interest)
    elif None not in (payment, periods, interest):
        cal_principal(payment, periods, interest)
    elif None not in (payment, principal, interest):
        cal_number_of_monthly_payments(payment, principal, interest)
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")

