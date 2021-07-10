'''A warning when you're able to see the ISS in the night sky'''

import smtplib
import time
import datetime as dt

from api_calls import get_suntimes, iss_position


MY_LAT = -23
MY_LNG = -46
EMAIL_FROM = 'emailthatiusefortests@gmail.com'
PASSWORD =  'strongpassword'


# Transforms coordinates to whole values only
def aproximate(string): return round(float(string))

# Dict with sunrise and sunset hour and minutes
suntimer = get_suntimes(MY_LAT, MY_LNG)

# Get aproximate ISS Position
iss = iss_position()
iss_lat = aproximate(iss['latitude'])
iss_lng = aproximate(iss['longitude'])

# Object with utc time
now = dt.datetime.utcnow()

# Coordinates that should trigger a warning
lat_range = range(MY_LAT-3, MY_LAT+4)
lng_range = range(MY_LNG-3, MY_LNG+4)

# Daylight time
daytime_range = range(int(suntimer['sunrise']), int(suntimer['sunset']) + 1)

while True:
    time.sleep(60)
    # Checks and send warning if iss is above you
    if iss_lat in lat_range and iss_lng in lng_range:
        if int(now.hour) not in daytime_range:
            contents = f'''The ISS is currently above you at:
            latitude: {iss["latitude"]},
            longitude: {iss["longitude"]}'''
            connection = smtplib.SMTP('smtp.gmail.com', port=587)
            connection.starttls()
            connection.login(user=EMAIL_FROM, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL_FROM,
                to_addrs=EMAIL_FROM,
                msg=f'Subject:ISS NOTIFICATION\n\n{contents}'
            )

