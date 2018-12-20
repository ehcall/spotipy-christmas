import requests
import json
import csv

#read in API Key
key_file = open('lastfm-api')
lines = key_file.readlines()
key = lines[0]
API_KEY = key.split(" = ")
API_KEY = API_KEY[1]


def fetchtrackresults(song, page_number):
    seed_search = requests.get("http://ws.audioscrobbler.com/2.0/?method=track.search&track=" + song + "&api_key=" + API_KEY + "&page=" + str(page_number) + "&format=json")
    #print("http://ws.audioscrobbler.com/2.0/?method=track.search&track=" + song + "&api_key=" + API_KEY + "&startPage=" + str(page_number) + "&format=json")
    search_data = seed_search.json()
    return search_data['results']

songs = ["jingle bells"]
'''
with open("lastfm.csv",'w',encoding="utf-8",newline='') as writefile:
    csvwriter = csv.writer(writefile)
    for song in songs:
        results = fetchtrackresults(song, 1)
        total_results = int(results['opensearch:totalResults'])
        items_per_page = int(results['opensearch:itemsPerPage'])
        results_left = 0
        page_number = 0
        while results_left < total_results:
            page_number += 1
            results_left += items_per_page
            page_results = fetchtrackresults(song,page_number)
            matches = page_results['trackmatches']
            for track in matches['track']:
                csvwriter.writerow([track['name'],track['artist']])



#matches = results['trackmatches']
#item_num = 0
#while item_num < items_per_page:
    #track = matches['track'][item_num]
    #track_name = track['name']
    #track_artist = track['artist']
    #item_num += 1
'''

track = "Let It Snow! Let It Snow! Let It Snow!"
artist = "dean martin"
#get_track = requests.get("http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key=" + API_KEY + "&artist=" + artist + "&track=" + track.lower() + "&format=json")
#track_info = get_track.json()
#print(track_info['track'])
#track

##name
##artist
###name

##album
###artist
###title

##toptags (multiple tags)
###tag
####name

#album = "christmas+with+dino"
#artist = "dean+martin"
#get_album = requests.get("http://ws.audioscrobbler.com/2.0/?method=album.getInfo&api_key=" + API_KEY + "&artist=" + artist + "&album=" + album + "&format=json")
#print(get_album.json())

#album

##name
##artist
##tracks (multiple tracks)
###track
####name
####artist
#####name
