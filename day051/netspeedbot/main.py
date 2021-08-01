'''A bot that tweets your ISP if your internet connection is bad'''

from internet_speed_bot import InternetSpeedTwitterBot


PROMISED_DOWN = int('YOUR CONTRACT DOWNLOAD RATE')
PROMISED_UP = int('YOUR CONTRACT UPLOAD RATE')
EMAIL = 'YOUR TWITTER EMAIL'
PWD = 'YOUR TWITTER PASSWORD'
CHROME_DRIVER_PATH = 'YOUR CHROME DRIVER PATH'

# Initialize bot and get internet speed data
bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()

# Tweet text
contents = f'''@vivobr, por quê estou recebendo {bot.down}down/{bot.up}up \
quando pago por {PROMISED_DOWN}down/{PROMISED_UP}up?'''

# Sends tweet only if not receiving what you pay for
if bot.down < PROMISED_DOWN or bot.up < PROMISED_UP:
    bot.tweet_at_provider(EMAIL, PWD, contents)