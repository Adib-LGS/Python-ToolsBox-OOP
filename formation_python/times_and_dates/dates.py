from datetime import *

date1 = datetime(1, 12, 30, 12, 12, 12)
#print(date1)

date2 = datetime(1970, 12, 30, 12, 12, 12)
if date1 < date2:
     print(date1, 'is older')
elif date1 == date2:
    print('Same')
else:
    print(date2, 'is older')

print(datetime.today())

