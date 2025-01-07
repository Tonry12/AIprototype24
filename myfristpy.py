import argparse
from datetime import datetime

def parse_input():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--bd',
        type=str,
        required=True,
        help='birthday of the user in DD-MM-YYYY format'
    )

    parser.add_argument(
        '--name',
        type=str,
        default='Tonry',
        help='input name of the person who is using the app'
    )

    args = parser.parse_args()
    return args

def printHello(who):
    print(f"Hello world!, {who}!!")

def cal_days_from_today(birthday_str):
    birthday = datetime.strptime(birthday_str, '%d-%m-%Y')
    today = datetime.today()
    delta = today - birthday
    return delta.days

if __name__ == "__main__":
    input_v = parse_input()
    print('this is my first .py file.')
    printHello(input_v.name)
    days_diff = cal_days_from_today(input_v.bd)
    print(f'I was born {abs(days_diff)} days {"ago" if days_diff > 0 else "from today"}')
