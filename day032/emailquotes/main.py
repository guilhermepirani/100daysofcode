import random
import smtplib
import datetime as dt


weekday = dt.datetime.now().weekday()

# If monday
if weekday == 0:

    send_from = 'emailthatiusefortests@gmail.com'
    password = 'strongpassword'
    send_to = 'namenotavaiable@outlook.com'

    with open('day032/emailquotes/quotes.txt', 'r') as fquotes:
        quotes = [line.strip('\n') for line in fquotes]

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=send_from, password=password)
        connection.sendmail(
            from_addr=send_from,
            to_addrs=send_to,
            msg=f'''Subject:Motivational Quote\n\n
            Here's your motivational quote:
            {random.choice(quotes)}'''
        )