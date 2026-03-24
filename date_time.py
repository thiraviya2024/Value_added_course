# from datetime import date
# import datetime
# a=date(2005,12,9)
# b=date(2026,3,24)
# print(b-a)

# get value from user
from datetime import datetime
c=input("enter ur birth:,YYYY-MM-DD")
d=input("enter ur birth:,YYYY-MM-DD")
c1=datetime.strptime(c,"%Y-%m-%d")
d1=datetime.strptime(d,"%Y-%m-%d")
print(c1-d1)