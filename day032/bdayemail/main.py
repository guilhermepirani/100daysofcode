'''An automated happy bday sender you can schedule in services like pythonanywhere'''

import random
import smtplib
import datetime as dt
import pandas as pd

SEND_FROM = 'emailthatiusefortests@gmail.com'
PASSWORD = 'strongpassword'

# Get date and all bdays data
today = dt.datetime.now()
df = pd.read_csv('day032/bdayemail/birthdays.csv')

# Adds to bdays only those happenning today
bdays = df.query(f'day == {today.day} and month == {today.month}')

# Send emails
for row in bdays.itertuples(index=None, name=None):
    name = row[0]
    send_to = row[1]
    
    with open(f'day032/bdayemail/letter_templates/letter_{random.randint(1,3)}.txt', 'r') as ftemplate:
        letter = ftemplate.read().replace('[NAME]', name)

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=SEND_FROM, password=PASSWORD)
        connection.sendmail(
            from_addr=SEND_FROM,
            to_addrs=send_to,
            msg=f'Subject: Happy Birthday!\n\n{letter}'
        )
    