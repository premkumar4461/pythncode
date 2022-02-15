price=1000000
has_gd_credit=True
if has_gd_credit:
    down_payment=0.1 * price
else:
    down_payment=0.2 * price

print(f'down payment: ${down_payment}')
