import argparse
from colors import color

parser = argparse.ArgumentParser(prog='ProgramName',
                                 description='What the program does',
                                 epilog='Text at bottom of help')
parser.add_argument('-m',
                    '--monthly-saving',
                    type=int,
                    default=200,
                    help='월 저축 금액')
parser.add_argument('-i',
                    '--interest',
                    type=float,
                    default=0.02,
                    help='이자 (기본값: 0.02)')
parser.add_argument('--interest-type',
                    type=str,
                    default='yearly',
                    choices=['monthly', 'yearly'],
                    help='이자 계산 주기 (기본값: yearly)')
parser.add_argument('-t',
                    '--target-amount',
                    type=int,
                    default=100000000,
                    help='목표 금액 (기본값: 1억)')

args = parser.parse_args()
print(color("이자", style='bold') + ':', color("{} {}%", fg='green').format("연" if args.interest_type == "yearly" else "월",
                                                               args.interest * 100))
print(color("월 저축액", style='bold') + ':', color(format(args.monthly_saving, ','), fg='cyan'))
print(color("목표 금액", style='bold') + ':', color(format(args.target_amount, ','), fg='blue', style='bold'))

months = 12 if 'yearly' == args.interest_type else 1
total_months = 0

save_amount = months * args.monthly_saving
current_amount = 0

#TODO - 모인 금액 제대로 계산 안됨
#     - 중간에 입력을 통해 current_amount에 변화 줄 수 있도록 (추가 수입 or 지출)
#     - 임금 상승률, n년 단위로 금리 변동 기능 추가
while current_amount < args.target_amount:
        total_months += months
        current_amount += save_amount
        current_amount *= args.interest

        print()
        print(color("소요시간", style='bold') + ':', color('{}달 ({}년)'.format(total_months, total_months/12.0), fg='magenta'))
        print(color("모인 금액", style='bold') + ':', color(format(current_amount, ','), fg='red'))
        
        input()