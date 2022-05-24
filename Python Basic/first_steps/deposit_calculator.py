# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

deposit_sum = float(input())
term_deposit_months = int(input())
interest_rate = float(input())

interest_rate_nominal = interest_rate / 100
interest_rate_monthly = interest_rate_nominal / 12
interest_per_month = deposit_sum * interest_rate_monthly

to_be_received = deposit_sum + term_deposit_months * interest_per_month

print(to_be_received)
