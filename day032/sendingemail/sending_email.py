'''Sends an email'''

import smtplib

# Password needed for sender authentication
send_from = 'emailthatiusefortests@gmail.com'
password = 'strongpassword'
send_to = 'namenotavaiable@outlook.com'

with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    connection.starttls() # Encription
    connection.login(user=send_from, password=password) 
    connection.sendmail(
        from_addr=send_from,
        to_addrs=send_to,
        # \n\n needed to separate subject and body
        msg='''Subject:Testing Email Scripting\n\n
        Hello, this is a test you're sending to yourself, I hope you're happy.'''
    )