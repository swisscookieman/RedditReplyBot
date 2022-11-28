# import the modules
import praw
import time

# initialize with appropriate values
client_id = ""  # this is the id of your reddit app
client_secret = ""  # this is the secret code of your reddit app
username = ""  # this is the username of the reddit account your bot will be controlling
password = ""  # this is the password of the reddit account your bot will be controlling
user_agent = ""  # this should be a TRUE description of what your bot will do

# creating an authorized reddit instance
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)

# defining the subreddit that will be scanned for new posts
subreddit = reddit.subreddit('assetto_pirate')
# initiating the lastUrl variable to check if a post is new
lastUrl = ""
# continuous scanning
while True:
    # take the last post of the reddit
    for submission in subreddit.new(limit=1):
        # check if it is new
        if str(submission.url) != lastUrl:
            # displays the submission title
            print("Title: ", submission.title)
            # displays the url of the submission
            print("URL: ", submission.url)
            # setting its url to the lastUrl value to remember it as old post
            lastUrl = submission.url
            # setting the url that will be used
            theurl = str(submission.url)

            # verifiying if this is a text post's url (this bugs when you have a image post)
            if theurl[-1] == "/":
                # prints that replying is possible
                print("I COULD REPLY")
                # initiating the submission variable
                submission = reddit.submission(url=theurl)
                # trying to reply
                try:
                    submission.reply("This an automated bot message. SwissCookieMan has made a modlist for r/assetto_pirate . Try to see if what you need is here: https://docs.google.com/spreadsheets/d/1SzrNAgVKnx8Wc1wbpdgN_j-qLne-yKhxMAbD0Q_mIms/edit?usp=sharing  | This is automated by a bot")
                # catching errors from when the bot has exceeded the reply rate and resetting lastUrl to retry at next scan
                except:
                    lastUrl = ""
                    print("I was blocked from replying, retrying in 20 secs")
                # if no error the bot has replyied correctly so we print that
                else:
                    print("I replyied")
            print("--------------")
        # if there is no post we also print that
        else:
            print("No new post")
            print("--------------")
        # we wait 20 seconds between each scan.
        time.sleep(20)
