import os
import titleGenerator
import albumGenerator
from twython import Twython

#This will combine the results from albumGenerator.py and titleGenerator.py and post them to twitter using the Twython interface for the API. You will need to input your own authorization credentials to post to twitter.

MY_CONSUMER_KEY = '3HGHFzwemPanF4cJl6TRXURLs'
MY_CONSUMER_SECRET = 'zhTst30FnUedsudWeUtZpNJ6EJKlPaNXemULVTepyTJHL7o3n3'
MY_ACCESS_TOKEN_KEY = '3403286699-8awGaAOaczRJ7lbg1ftniCkLTSgf8Sqbj7AD4vJ'
MY_ACCESS_TOKEN_SECRET = 'rtq4tPJr06Xy763BwRagvs1zlS4X5iW8t6wQEsIZG6VL5'


twitter = Twython(MY_CONSUMER_KEY, MY_CONSUMER_SECRET, MY_ACCESS_TOKEN_KEY, MY_ACCESS_TOKEN_SECRET)
review = titleGenerator.generateDescription()
while len(review) > 140:
    review = titleGenerator.generateDescription()
albumf = albumGenerator.generateAlbum()
mediaResponse = twitter.upload_media(media=open(os.path.join('.',albumf),'r'))
twitter.update_status(status=review, media_ids=[mediaResponse['media_id']])
