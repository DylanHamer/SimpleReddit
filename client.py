"""
SimpleReddit
Very simple Reddit client to learn the Reddit API
By Dylan Hamer
"""

import praw  # Reddit API
import pyfiglet  # Optional subreddit headers

"""OAuth credentials: Remove these before commiting to source control"""
id = ""
secret = ""
agent = "SimpleReddit (by /u/dylanhamer13)"

class simpleReddit:
    def __init__(self):
        """Initialise Reddit instance"""
        self.reddit = praw.Reddit(user_agent=agent,
                             client_secret=secret,
                             client_id=id)
        self.subreddit = "dadjokes"
        self.sort = "hot"

    def browse(self, showScores = True):
        """View posts"""
        subreddit = self.reddit.subreddit(self.subreddit)
        posts = getattr(subreddit, self.sort)()  # Get posts in subreddit
        pyfiglet.print_figlet("/r/{}".format(self.subreddit))
        for post in posts:
            print("-"*40)
            print(post.title)
            print(getattr(post, "selftext", "-"))
            if showScores:
                print("Score: {}".format(post.score))
            print("-"*40+"\n")

simpleReddit = simpleReddit()
simpleReddit.browse()
