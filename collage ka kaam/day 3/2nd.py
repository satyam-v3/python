## WAP to display current date and time ###

import datetime
now = datetime.datetime.now()
print(" Current Date & Time : ")
print(now.strftime("%Y/%m/%d %H:%M:%S"))