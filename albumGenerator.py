import os
import re
import math
import random
import urllib
import urllib2
import json
from PIL import Image, ImageDraw, ImageFont, ImageChops
from BeautifulSoup import BeautifulStoneSoup

#This code will download a random image from Flickr, glitch and/or apply a tint to the image, crop it to be square, and then grab a random wiki page title and overlay it as the album title
#if called on it's own, will generate 10 album covers and save them in the local directory
#if imported, call generateAlbum which will return the local filename of the generated cover
#code to download and glitch images copied and modified from Chris Cuellar's tutorial
#which is available at http://blog.art21.org/2011/09/20/how-to-use-python-to-create-a-simple-flickr-photo-glitcher/#.VcgaF3UVhBc



def getTitle():
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    page = urllib2.urlopen("https://en.wikipedia.org/w/api.php?action=query&generator=random&grnnamespace=0&prop=extracts&exchars=500&format=json")
    js = json.load(page)
    key = js["query"]["pages"].keys()
    title = js['query']['pages'][key[0]]['title'].encode('ascii','ignore')
    title = re.sub('\(.*\)','',title)
    return title


def find_an_image(keyword):
    response = urllib.urlopen('http://api.flickr.com/services/feeds/photos_public.gne?tags=' + keyword + '&lang=en-us&format=rss_200')
    soup = BeautifulStoneSoup(response)
 
    image_list = []
 
    for image in soup.findAll('media:content'):
        image_url = dict(image.attrs)['url']
        image_list.append(image_url)
 
    return random.choice(image_list)
   
def download_an_image(image_url):
    filename = image_url.split('/')[-1]
    urllib.urlretrieve(image_url, filename)
   
    return filename
 
def get_random_start_and_end_points_in_file(file_data):
    start_point = random.randint(2500, len(file_data))
    end_point = start_point + random.randint(0, len(file_data) - start_point)
 
    return start_point, end_point
 
def splice_a_chunk_in_a_file(file_data):
    start_point, end_point = get_random_start_and_end_points_in_file(file_data)
    section = file_data[start_point:end_point]
    repeated = ''
 
    for i in range(1, random.randint(1,5)):
        repeated += section
 
    new_start_point, new_end_point = get_random_start_and_end_points_in_file(file_data)
    file_data = file_data[:new_start_point] + repeated + file_data[new_end_point:]
    return file_data
   
def glitch_an_image(local_image):
    file_handler = open(local_image, 'r')
    file_data = file_handler.read()
    file_handler.close()
 
    for i in range(1, random.randint(1,5)):
        file_data = splice_a_chunk_in_a_file(file_data)
 
    file_handler = open(local_image, 'w')
    file_handler.write(file_data)
    file_handler.close
 
    return local_image

def square_image(local_image):
	with Image.open(local_image) as im:
		s = im.size
		b = min(s)
		box = ((s[0]-b)/2,(s[1]-b)/2,(s[0]+b)/2,(s[1]+b)/2)
		square = im.crop(box)
	square.save(local_image)

	return local_image

def add_text(local_image,string):
	dn = os.path.dirname(os.path.realpath(__file__))
	fonts_dir = os.path.join(dn,"fonts")
	with Image.open(local_image).convert('RGBA') as im:
		txt = Image.new('RGBA',im.size,(255,255,255,0))
		fnt = ImageFont.truetype(os.path.join(fonts_dir,random.choice(os.listdir(fonts_dir))),random.randint(20,72))
		d = ImageDraw.Draw(txt)
		s = im.size
		loc = (random.randint(1,math.floor(0.55*s[0])),random.randint(1,s[1]))
		d.text(loc, string, font=fnt, fill=(255,255,255,255))
		out = Image.alpha_composite(im,txt)
	out.save(local_image)

	return local_image

def tint(local_image):
        colors = ('#D586E3','#FCAA3F','#2D2DC4','#00F731','#00F3F7','#999E11','#EDCECE','#523333')
        with Image.open(local_image) as im:
		out = ImageChops.multiply(im,Image.new('RGB',im.size,colors[random.randint(1,len(colors)-1)]))
	out.save(local_image)

	return local_image
	 
def generateAlbum():
        keywords = ['art','beach','house','landscape','punk','night','owl','portrait','music','fire','throwback','painting']
	key = keywords[random.randint(1,len(keywords))-1]
    	image_url = find_an_image(key)
    	image = download_an_image(image_url)
        r = random.randint(1,10)
        if r < 6:
    	    image = glitch_an_image(image)
        if r % 2 == 0:
	    image = tint(image)
        image = square_image(image)
        title = getTitle()
        image = add_text(image,title)
        return image

if __name__ == "__main__":
    for x in range(1,10):
        print generateAlbum()
