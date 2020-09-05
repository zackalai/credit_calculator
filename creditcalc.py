import math
import argparse

# write your code here
# print('What do you want to calculate?')
# print('type "n" for number of monthly payments,')
# print('type "a" for annuity monthly payment amount,')
# print('type "p" for credit principal:')
#
# what_want_calculate = input()
parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--principal', type=float)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=float)
# args = parser.parse_args(['--type=diff', '--principal=1000000', '--interest=10', '--periods=10'])
# args = parser.parse_args(['--type=annuity', '--principal=1000000', '--interest=10', '--periods=60'])
# args = parser.parse_args(['--type=diff', '--principal=1000000', '--payment=10400'])
# args = parser.parse_args(['--type=diff', '--principal=500000', '--interest=7.8', '--periods=8'])
# args = parser.parse_args(['--type=annuity', '--payment=8722', '--interest=5.6', '--periods=120'])
#args = parser.parse_args(['--type=annuity', '--principal=500000', '--interest=7.8', '--payment=23000'])

args = parser.parse_args()


# if args.type is not None and args.principal is not None and args.interest is not None:
#     print('interest is not None')
# print(vars(args))
# print(any(v is None for v in vars(args).values()))
args_count = 0
for v in vars(args).values():
    if v is not None:
        args_count += 1


def months_to_years(months):
    number_of_months = months % 12
    number_of_years = months // 12

    if number_of_months == 1 and number_of_years == 0:
        return '{} {}'.format(number_of_months, 'month')
    elif number_of_months == 0 and number_of_years != 0:
        return '{} {}'.format(number_of_years, 'year')
    elif number_of_months == 1 and number_of_years == 1:
        return '{} {} and {} {}'.format(number_of_years, 'year', number_of_months, 'month')
    elif number_of_months != 1 and number_of_years != 1:
        return '{} {} and {} {}'.format(number_of_years, 'years', number_of_months, 'months')
    else:
        pass
# print(args_count)


if args_count == 4:

    P = args.principal
    n = args.periods
    if args.interest is not None:
        i = args.interest / (12 * 100)

    annuity = args.payment

    if args.type == 'diff':
        diff_args = [args.principal, args.interest, args.periods]
        if all(arg is not None for arg in diff_args):
            total = 0
            for period in range(1, args.periods + 1):
                payment = (P / n) + i * (P - (P * ((period - 1) / n)))
                total += math.ceil(payment)
                print('Month {}: payment is {}'.format(period, math.ceil(payment)))
            print('Overpayment = {:.0f}'.format(total - P))
        else:
            print('Incorrect Parameters')

    elif args.type == 'annuity':
        if args.payment is None:
            annuity_payment = math.ceil(P * (i * pow((1 + i), n) / (pow((1 + i), n) - 1)))
            print('Your annuity payment = {}!'.format(annuity_payment))
            print('Overpayment = {:.0f}'.format(annuity_payment * n - P))
        elif args.principal is None:
            credit_principal = math.floor(annuity / ((i * pow((1 + i), n)) / (pow((1 + i), n) - 1)))

            print('Your credit principal = {:.0f}!'.format(credit_principal))
            print('Overpayment = {:.0f}'.format(annuity * n - credit_principal))
        elif args.periods is None:
            periods = math.ceil(math.log(annuity / (annuity - i * P), (i + 1)))
#             number_of_monthly_payment = math.ceil(math.log(monthly_payment
# #                                                    / (monthly_payment - credit_interest
# #                                                       * credit_principal),
# #                                                    (credit_interest + 1)))
            print(periods)
            print('It will take {} to repay this credit!'.format(months_to_years(periods)))
            print('Overpayment = {:.0f}'.format(annuity * periods - P))
else:
    print('Incorrect Parameters')

# if args.type is not None and args.principal is not None and args.periods is not None and args.interest is not None:
#
#
#
#     P = args.principal
#     n = args.periods
#     i = args.interest / (12 * 100)
#
#     if args.type == 'diff':
#         total = 0
#         for period in range(1, args.periods + 1):
#             payment = (P / n) + i * (P - (P * ((period - 1) / n)))
#             total += math.ceil(payment)
#             print('Month {}: payment is {}'.format(period, math.ceil(payment)))
#         print('Overpayment = {:.0f}'.format(total - P))
#
#     elif args.type == 'annuity':
#         pass
#
# else:
#     print('Incorrect Parameters')


# def months_to_years(months):
#     number_of_months = months % 12
#     number_of_years = months // 12
#
#     if number_of_months == 1 and number_of_years == 0:
#         return '{} {}'.format(number_of_months, 'month')
#     elif number_of_months == 0 and number_of_years == 1:
#         return '{} {}'.format(number_of_years, 'year')
#     elif number_of_months == 1 and number_of_years == 1:
#         return '{} {} and {} {}'.format(number_of_years, 'year', number_of_months, 'month')
#     elif number_of_months != 1 and number_of_years != 1:
#         return '{} {} and {} {}'.format(number_of_years, 'years', number_of_months, 'months')
#     else:
#         pass
#
#
# if what_want_calculate == 'n':
#     print('Enter the credit principal:')
#     credit_principal = float(input())
#     print('Enter the monthly payment:')
#     monthly_payment = int(input())
#     print('Enter the credit interest:')
#     credit_interest = float(input()) / 12 / 100
#
#     number_of_monthly_payment = math.ceil(math.log(monthly_payment
#                                                    / (monthly_payment - credit_interest
#                                                       * credit_principal),
#                                                    (credit_interest + 1)))
#
#     print('You need {} to repay this credit!'.format(months_to_years(number_of_monthly_payment)))
#

# elif what_want_calculate == 'a':
#     print('Enter the credit principal:')
#     credit_principal = float(input())
#     print('Enter the number of periods:')
#     number_of_periods = int(input())
#     print('Enter the credit interest:')
#     credit_interest = float(input()) / (12 * 100)
#
#     annuity_payment = \
#         math.ceil(credit_principal * (credit_interest
#                                       * pow((1 + credit_interest), number_of_periods)
#                                       / (pow((1 + credit_interest), number_of_periods) - 1)))
#
#     print('Your annuity payment = {}!'.format(annuity_payment))
#

# elif what_want_calculate == 'p':
#     print('Enter the annuity payment:')
#     annuity_payment = float(input())
#     print('Enter the count of periods')
#     count_of_periods = int(input())
#     print('Enter the credit interest:')
#     credit_interest = float(input()) / (12 * 100)
#
#     credit_principal = round(annuity_payment \
#                        / ((credit_interest * pow((1 + credit_interest), count_of_periods))
#                           / (pow((1 + credit_interest), count_of_periods) - 1)))
#
#     print('Your credit principal = {}!'.format(credit_principal))
