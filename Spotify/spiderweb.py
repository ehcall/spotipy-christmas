import spotipy
import re
import jellyfish
import spotipy.oauth2 as oauth2
import csv
from collections import Counter
import time

# # # Import client id and client secret (and username). I know there's a better way to set ENV variables, but I'm not gonna learn how right now.
with open('../spotify-christmas-keysecret.txt', encoding="ascii") as txtfile:
    lines = txtfile.readlines()
    client_id = re.sub("client_id = ", "", lines[0])
    client_id = re.sub("\n","",client_id)

    client_secret = re.sub("client_secret = ", "", lines[1])
    client_secret = re.sub("\n", "", client_secret)

    #print(client_id + "\n" + client_secret)

# # # Spotify authentication
credentials = oauth2.SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret)

token = credentials.get_access_token()
sp = spotipy.Spotify(auth=token)


### read in file of foreign christmas songs? or just add directly into program?
### for now we'll just do the one song
seeds = ["\"jingle+bells\"","\"santa+claus+is+coming+to+town\"","\"alina+masina\"","\"astro+del+ciel\"","\"belle+nuit\"","\"bianco+natal\"","\"cicha+noc\"","\"clara+notg\"","\"csendes+éj\"","\"cëchô+noc\"","\"douce+nuit\"","\"glade+jul\"","\"gleðilig+jól\"","\"heims+um+bol\"","\"hljóða+nótt\"","\"jouluyö,+juhlayö\"","\"kiyoshi+kono+yoru\"","\"klusa+nakts\"","\"la+sankta+nokto\"","\"malam+kudus\"","\"malam+sunyi,+malam+suci\"","\"natë+e+shenjtë\"","\"nocte+seren\"","\"noite+feliz\"","\"noite+de+paz\"","\"nokto+pacoz\"","\"notte+lunar\"","\"nuit+de+paix\"","\"nuit+de+silence\"","\"o+noapte+preasfintita\"","\"oidhche+shamhach\"","\"oíche+chiúin\"","\"püha+öö\"","\"sainte+nuit\"","\"sancta+nox\"","\"santo+natal\"","\"kutsal+gece\"","\"stilla+natt\"","\"stille+nacht\"","\"stille+nag\"","\"stille+nat\"","\"sveta+noč\"","\"talang+patnubay\"","\"tichá+noc\"","\"tiha+noć\"","\"tykha+nich\"","\"tyli+naktis\"","\"usiku+mtakatifu\"","\"voici+noël\"","\"đêm+thánh+vô+cùng\""]
#seeds = ["\"jingle+bells\""]
collect = []
### Need to open a file to write the info to ###


album_ids = {}
collected_tracks_ids = []
with open("spiderweb.csv",'a+',encoding="utf-8",newline='') as writefile:
    csvwriter = csv.writer(writefile)
    for song in seeds:
        print("song being seeded: ",song)
        ### search and gather tracks on spotify for seeded song
        offset_num = 0
        while offset_num <= 100000:
            try:

                results = sp.search(q=song, limit=50, type='track', offset=offset_num)
                tracks = results['tracks']['items']
                if len(results) == 0:
                    print("there aren't any results")
                    break
                    ### save the results in a file (track name, track id, album name, album id, artist name, artist id), but also save just album uris in program
                for track in tracks:
                    track_id = track['id']
                    if track_id not in collected_tracks_ids:
                        collected_tracks_ids.append(track_id)
                        track_name = track["name"]
                        artist_names = []
                        artist_ids = []
                        for artist in track["artists"]:
                            artist_names.append(artist["name"])
                            artist_ids.append(artist['id'])
                        album_name = track['album']['name']
                        album_id = track['album']['id']
                        if album_id not in album_ids:
                            album_ids[album_id] = album_name
                        csvwriter.writerow([track_name,track_id,artist_names,artist_ids,album_name,album_id])

                offset_num += 50
                print(offset_num)
                time.sleep(60)
            except spotipy.client.SpotifyException as e:
                print(str(e))
                url = "https://api.spotify.com/v1/search?" + song + "&type=track"

                print("done searching for ",song)
                print(offset_num)
                #offset_num += 50
        print("gathering tracks...")
        all_album_tracks = []
        all_album_tracks_info = []
        for album_id in album_ids:
            try:
                album_tracks = sp.album_tracks(album_id)
                for track in album_tracks['items']:

                    track_name = track['name']
                    track_name = track_name.replace(" ", "+").lower()
                    track_name = "\"" + track_name + "\""

                    artist_names = []
                    artist_ids = []
                    for artist in track["artists"]:
                        artist_names.append(artist["name"])
                        artist_ids.append(artist['id'])
                    all_album_tracks_info.append([track["name"], track_id, artist_names, artist_ids, album_ids[album_id], album_id])
                    all_album_tracks.append(track_name)
            except:
                print(album_ids[album_id] + " might be a broken album")
        #album_track_set = set()

        ### need to find similarities
        counted = Counter(all_album_tracks)

        top_recurring_songs = []
        for count in counted:
            #print(count,counted[count])
            if counted[count] >= 20:
                print(count)
                top_recurring_songs.append(count)
                if count not in seeds:
                    seeds.append(count)

        for track in all_album_tracks_info:
            track_name = track[0].replace(" ", "+").lower()
            track_name = "\"" + track_name + "\""
            if counted[track_name] < 20 and track_name not in seeds:
                skip = False
                for song in top_recurring_songs:
                    if jellyfish.jaro_winkler(track_name, song) >= .8:
                        skip = True
                        break
                if not skip:
                    user_input = input("seed? y/n:"+ track[0] + track[2][0])
                    if user_input is "y":

                        seeds.append(track_name)
                        #print(seeds)
                    else:
                        user_input2 = input("save track info? Y/N:")
                        if user_input2 is "y":
                            csvwriter.writerow(track)
                            collected_tracks_ids.append(track[1])
