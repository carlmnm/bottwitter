import tweepy
import time

auth = tweepy.OAuthHandler('j3xjpuDi950EsotjY9L4PKrWE','skSp7GcQXgtLiu90mddumiqHiW2wjTGUlgdXgWwcWEsNl8iQCO')
auth.set_access_token('1278858626539675651-hTqJ9YSpUSOLh3lwI71EvwCSdfNwC1','FwxUkiKalSHPAWnhThhdAnrzyhmTsOTL4HEJaAEEEYR4A')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'the smiths'
numtwt = 100

for tweet in tweepy.Cursor(api.search, search).items(numtwt):
    try:
        print('retuitei esse')
        tweet.retweet()
        time.sleep(1800)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
