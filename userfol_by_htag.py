from instagrapi import Client
import config
import time
import random

cl = Client()
cl.login(config.username, config.password)

hashtag = "birmingham"
amount = 25
posts = cl.hashtag_medias_recent(hashtag,amount)
#posts = cl.hashtag_medias_top(hashtag, amount)

while True:

    try:

        for i in range(amount):
            print("Post" + str(i+1))
            cl.media_like(posts[i].id)
            print("Liked post: " + posts[i].id)
            cl.user_follow(posts[i].user.pk)
            print("Followed: " + posts[i].user.username)
            time.sleep(random.randint(864,901 ))

    except Exception as ex:
        print(ex)
        continue






