# Paste your code into this box

Monthly_payment_lower_bound = balance / 12
Monthly_payment_upper_bound = (balance * (1 + annualInterestRate/12)**12) / 12.0

Lowest_Payment=(Monthly_payment_lower_bound+Monthly_payment_upper_bound)/2

while 1:
    remainBalance=balance
    for i in range(1,13):
        remainBalance=remainBalance - Lowest_Payment
        remainBalance=remainBalance * (1+annualInterestRate/12)
    if(abs(remainBalance-0)<=0.001):
        break
    if(remainBalance>0):
        Monthly_payment_lower_bound=Lowest_Payment
        Lowest_Payment=(Monthly_payment_lower_bound+Monthly_payment_upper_bound)/2
    if(remainBalance<0):
        Monthly_payment_upper_bound=Lowest_Payment
        Lowest_Payment=(Monthly_payment_lower_bound+Monthly_payment_upper_bound)/2

print 'Lowest Payment: '+str(round(Lowest_Payment,2))
