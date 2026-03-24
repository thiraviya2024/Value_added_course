from datetime import datetime
import pytz
a=datetime.now()
b=pytz.timezone("Asia/Kolkata")
c=a.astimezone(b)
print(c)