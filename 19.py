def days(month,year):
    thirty = ['november','april','june','september']

    if month == 'february':
        leap = False
        if year % 100 == 0 and year % 400 == 0:
            leap = True
        
        elif year % 100 == 0 and year % 400 != 0:
            leap = False

        elif year % 4 == 0:
            leap = True
        
        if leap:
            return 29
        else:
            return 28

    if month in thirty:
        return 30

    else:
        return 31

months = ['january','february','march','april','may','june','july','august','september','october','november','december']
week = ['sunday','monday','tuesday','wednesday','thirsday','friday','saturday']

sum = 0
limitWeek = len(week)
weekCounter = 1 # 01/01/1900 was a monday

for year in range(1900,2001):
    for month in months:
        daysInThisMonth = days(month,year)
        for day in range(1,daysInThisMonth + 1):
            if year > 1900 and (week[weekCounter] == 'sunday' and day == 1):
                sum += 1
            weekCounter = (weekCounter + 1) % limitWeek

print sum