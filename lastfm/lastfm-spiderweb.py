import requests
import json
import csv

#read in API Key
key_file = open('./lastfm/lastfm-api')
lines = key_file.readlines()
key = lines[0]
API_KEY = key.split(" = ")
API_KEY = API_KEY[1]


def fetchtrackresults(song, page_number):
    seed_search = requests.get("http://ws.audioscrobbler.com/2.0/?method=track.search&track=" + song + "&api_key=" + API_KEY + "&page=" + str(page_number) + "&format=json")
    #print("http://ws.audioscrobbler.com/2.0/?method=track.search&track=" + song + "&api_key=" + API_KEY + "&startPage=" + str(page_number) + "&format=json")
    search_data = seed_search.json()
    return search_data['results']

def search_one_track(track_name,artist,mbid):
    if mbid != '0':
        get_track = requests.get("http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key=" + API_KEY + "&mbid=" + mbid + "&format=json")
        try:
            return get_track.json()
        except json.decoder.JSONDecodeError:
            print("idk JSON problem")
            return False
    else:
        get_track = requests.get("http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key=" + API_KEY + "&artist=" + artist + "&track=" + track_name + "&format=json")
        try:
            results = get_track.json()
            try:
                if results['error']:
                    return False
            except:
                return results
        except json.decoder.JSONDecodeError:
            print("idk JSON problem")
            return False






songs = ["jingle bells"]
for song in songs:
    results = fetchtrackresults(song, 1)
    total_results = int(results['opensearch:totalResults'])
    items_per_page = int(results['opensearch:itemsPerPage'])
    results_left = 0
    page_number = 0
    simple_track_data = []
    while results_left < total_results:
        page_number += 1
        results_left += items_per_page
        page_results = fetchtrackresults(song,page_number)
        matches = page_results['trackmatches']
        for track in matches['track']:
            mbid = track['mbid']
            if len(mbid) < 1:
                mbid = 0
            simple_track_data.append([track['name'],track['artist'],mbid])
    full_track_data = []
    for simple_track in simple_track_data:
        track_name = simple_track[0].lower()
        artist = simple_track[1].lower()
        if '&' not in artist:
            mbid = simple_track[2]
            track_info = search_one_track(track_name, artist, mbid)
            if track_info is False:
                print(track_name, artist, " FAILED")
                full_track_data.append([track_name, artist, "NO ALBUM", "NO ALBUM", 0, '[]'])
            else:
                track_data = track_info['track']
                try:
                    artist_mbid = track_data['artist']['mbid']
                    if len(artist_mbid) < 1:
                        artist_mbid = 0
                except:
                    artist_mbid = 0
                try:
                    album_name = track_data['album']['title']
                    album_artist = track_data['album']['artist']
                    album_mbid = track_data['album']['mbid']
                    if len(album_mbid) < 1:
                        album_mbid = 0
                except:
                    album_name = "NO ALBUM"
                    album_artist = "NO ALBUM"
                    album_mbid = 0
                tags = track_data['toptags']['tag']
                print_tags = []
                for tag in tags:
                    print_tags.append(tag['name'])
                full_track_data.append([track_name, mbid, artist,artist_mbid, album_name, album_artist, album_mbid, print_tags])

    albums = []
    for full_track in full_track_data:
        ### gather album titles/mbid here
        print("")

    for album in albums:
        print("")
        ### collect all songs
        ### decide whether or not to seed
### Collect tracks for all songs in "songs"
'''
with open("./Data Files/lastfm.csv",'w',encoding="utf-8",newline='') as writefile:
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
                mbid = track['mbid']
                if len(mbid) < 1:
                    mbid = 0
                csvwriter.writerow([track['name'],track['artist'],mbid])
'''
'''
tracks = []
with open('./Data Files/lastfm.csv', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        tracks.append(row)
'''
### collect track data
'''
with open('./Data Files/lastfm-trackdata.csv', 'w', newline='', encoding='utf-8') as csv_write_file:
    csv_writer = csv.writer(csv_write_file)
    for track in tracks:
        track_name = track[0].lower()
        artist = track[1].lower()
        if '&' not in artist:
            mbid = track[2]
            track_info = search_one_track(track_name,artist,mbid)
            if track_info is False:
                print(track_name,artist," FAILED")
                csv_writer.writerow([track_name, artist, "NO ALBUM", "NO ALBUM",0,'[]'])
            else:
                track_data = track_info['track']
                try:
                    artist_mbid = track_data['artist']['mbid']
                    if len(artist_mbid) < 1:
                        artist_mbid = 0
                except:
                    artist_mbid = 0
                try:
                    album_name = track_data['album']['title']
                    album_artist = track_data['album']['artist']
                    album_mbid = track_data['album']['mbid']
                    if len(album_mbid) < 1:
                        album_mbid = 0
                except:
                    album_name = "NO ALBUM"
                    album_artist = "NO ALBUM"
                    album_mbid = 0
                tags = track_data['toptags']['tag']
                print_tags = []
                for tag in tags:
                    print_tags.append(tag['name'])
                csv_writer.writerow([track_name, mbid, artist,artist_mbid, album_name, album_artist, album_mbid, print_tags])
'''

tracks = []
with open('./Data Files/lastfm-trackdata.csv', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        tracks.append(row)

### collect album data

#track


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
