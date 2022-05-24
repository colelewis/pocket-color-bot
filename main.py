import argparse
from random import randint
from datetime import datetime
from twitter_secrets import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_KEY_SECRET, twitter_secrets as ts
from PIL import Image
import tweepy, webcolors, os, sys

consumer_key = ts.API_KEY
consumer_secret = ts.API_KEY_SECRET
access_token = ts.ACCESS_TOKEN
access_secret = ts.ACCESS_TOKEN_SECRET

def write_to_history(data, image, date_to_write):
    with open('data/tweet_history/' + date_to_write + '_tweet.txt', 'w') as file:
        file.write(data)
    image.save('data/color_images/' + date_to_write + ".png")

def main():

    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    # api.update_status('tweet')  
      
    rred = randint(0, 255)
    rgreen = randint(0, 255)
    rblue = randint(0, 255)
    
    text_content = 'RGB: ' + '('+ str(rred) + ', ' + str(rgreen) + ', ' + str(rblue) + ')' + '\n' + 'Hex: ' + webcolors.rgb_to_hex((rred, rgreen, rblue)) + '\n' + 'RGB Percentages: ' + '('+ str(round(((rred/255)*100), 3)) + '%, ' + str(round(((rblue/255)*100), 3)) + '%, ' + str(round(((rgreen/255)*100), 3)) + '%)'
    color_image = Image.new('RGB', (32, 32), color=(rred, rgreen, rblue))
    color_image.save('data/color_images/temp.png')

    api.update_status_with_media(text_content, 'data/color_images/temp.png')

    os.remove("data/color_images/temp.png") # immediately cleans up temporarily generated file
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--save', help='Saves color images and information in /data', action='store_true')
    args = parser.parse_args()
    if args.save:
        write_to_history(text_content, color_image, str(datetime.now()))
    

if __name__=="__main__":
    main()