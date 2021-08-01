'''Follow all the follower of target account'''

from instagram_bot import InstaFollower


CHROME_DRIVER_PATH = 'YOUR CHROME DRIVER PATH'
SIMILAR_ACCOUNT = 'ACCOUNT YOU WANT TO GET FOLLOWERS FROM'
USERNAME = 'YOUR INSTAGRAM EMAIL'
PASSWORD = 'YOUR INSTAGRAM PASSWORD'


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login(USERNAME, PASSWORD)
bot.find_followers(SIMILAR_ACCOUNT)
bot.follow()