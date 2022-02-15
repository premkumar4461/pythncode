# if apllication has high income AND good credit eligible for loan
#AND both condition are  must be true
#  OR at list one condition must be true
# NOT any boolean value true
from re import T


has_high_income=False
has_good_income=True

if has_high_income and has_good_income:
    print("elgible for loan")
else:
    print("not elgible for loan")