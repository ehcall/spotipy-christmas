[INSERT CREDENTIALS HERE]
import spotipy
import re
import spotipy.oauth2 as oauth2
import csv
import string

# # # Import client id and client secret (and username). I know there's a better way to set ENV variables, but I'm not gonna learn how right now.
#with open('../spotify-christmas-keysecret.txt', encoding="ascii") as txtfile:
#    lines = txtfile.readlines()
#    client_id = re.sub("client_id = ", "", lines[0])
#    client_id = re.sub("\n","",client_id)

#    client_secret = re.sub("client_secret = ", "", lines[1])
#    client_secret = re.sub("\n", "", client_secret)

#    print(client_id + "\n" + client_secret)

# # # Spotify authentication
#credentials = oauth2.SpotifyClientCredentials(
#        client_id=client_id,
#        client_secret=client_secret)

#token = credentials.get_access_token()
#sp = spotipy.Spotify(auth=token)


### read in file of foreign christmas songs? or just add directly into program?
### for now we'll just do the one song
songs = ["jingle+bells","alina+masina","astro+del+ciel","belle+nuit","bianco+natal","cicha+noc","clara+notg","csendes+éj","cëchô+noc","douce+nuit","glade+jul","gleðilig+jól","heims+um+bol","hljóða+nótt","jouluyö,+juhlayö","kiyoshi+kono+yoru","klusa+nakts","la+sankta+nokto","malam+kudus","malam+sunyi,+malam+suci","natë+e+shenjtë","nocte+seren","noite+feliz","noite+de+paz","nokto+pacoz","notte+lunar","nuit+de+paix","nuit+de+silence","o+noapte+preasfintita","oidhche+shamhach","oíche+chiúin","püha+öö","sainte+nuit","sancta+nox","santo+natal","kutsal+gece","stilla+natt","stille+nacht","stille+nag","stille+nat","sveta+noč","talang+patnubay","tichá+noc","tiha+noć","tykha+nich","tyli+naktis","usiku+mtakatifu","voici+noël","đêm+thánh+vô+cùng"]
### Need to open a file to write the info to ###


album_ids = []
for song in songs:
	offset_num = 0
	while offset_num <= 30000:
		results = sp.search(q=song,limit=50,type='track',offset=offset_num)
			#idk if this one goes here?
			if len(results) == 0:
				break
			### save the results in a file (track name, track id, album name, album id, artist name, artist id), but also save just album uris in program
		for track in results['items']:
			# track_name = track['name']
			# track_id = track['id']
			# artist_name = track['artists']['name']
			# artist_id = track['artists']['id']
			# album_name = track['album']['name']
			album_id = track['album']['id']
			album_id.append(album_id)
		
		offset_num += 50

	for album_id in album_ids:
		results = album_tracks(album_id)
		for track in results['items']:
			track_name = track['name']
			track_name.replace(" ", "+")
			# and right here is where we need to see if a version of the track name is in the songs list
			for song in songs:
				if track_name not in song:
					songs.append(track_name)

