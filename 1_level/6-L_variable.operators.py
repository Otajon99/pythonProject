good_income=False
good_credit=False

if good_income and good_credit:
    print('Your are eligible to our loan ')
elif good_income or good_credit:
    print('Our management will review and contact you as soon as possible ')
else:
    print('You are not eligible for the loan. please contact us next year!')