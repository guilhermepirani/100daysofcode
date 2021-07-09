'''Simple uses of datetime module https://docs.python.org/3/library/datetime.html'''

import datetime as dt

# datetime.now() returns local date and time if timezone not specified
now = dt.datetime.now() # dt.timezone.utc for utc time
print(now)

# Now is a object with atributes
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

# You can create an datetime object with specific atributes
bday = dt.datetime(year=1994, month=2, day=7) #Time defaults to 00:00
print(bday)

# You can check the day of the week: 0 monday -> 6 sunday
print(now.weekday())
print(bday.weekday())