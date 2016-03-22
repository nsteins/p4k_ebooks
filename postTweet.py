import os
import titleGenerator
import albumGenerator
from twython import Twython

import settings
#This will combine the results from albumGenerator.py and titleGenerator.py and post them to twitter using the Twython interface for the API. You will need to input your own authorization credentials to post to twitter.

activate_this = '~/p4k_ebooks/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

twitter = Twython(settings.MY_CONSUMER_KEY, settings.MY_CONSUMER_SECRET, settings.MY_ACCESS_TOKEN_KEY, settings.MY_ACCESS_TOKEN_SECRET)
review = titleGenerator.generateDescription()
while len(review) > 140:
    review = titleGenerator.generateDescription()
albumf = albumGenerator.generateAlbum()
mediaResponse = twitter.upload_media(media=open(os.path.join('.',albumf),'r'))
twitter.update_status(status=review, media_ids=[mediaResponse['media_id']])
