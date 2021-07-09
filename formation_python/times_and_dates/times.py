import time

start = time.time()
print('start: ' , start)

time.sleep(2)

end = time.time()
print('now: ' , end)

duration = int(start) - int(end)
print('the duration time is: ' , int(duration), 'secondes')

#format time %d = Day - %m = Month - %Y = Years... or %y(00-99) - %H = Hours - %I = Minutes - %S = secondes - %p = AM/PM - %A= Week-Day - %B = Month Name

print(time.strftime("%B-%A-%Y/%Z"))
