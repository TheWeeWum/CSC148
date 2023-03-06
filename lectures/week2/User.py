import Tweet
class User:
    def __init__(self, id, name, bio=""):
        self.id = id
        self.name = name
        self.bio = bio
        self.tweets = []

    def tweet(self, twt: Tweet):
        self.tweets.append(twt)

usr = User(0, "Liam")
new_tweet = Tweet.Tweet("Liam", "Today", "This is a tweet!")
usr.tweet(new_tweet)

print(usr.tweets)
