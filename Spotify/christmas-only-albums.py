import spotipy
import re
import spotipy.oauth2 as oauth2
import csv

# # # Import client id and client secret (and username). I know there's a better way to set ENV variables, but I'm not gonna learn how right now.
with open('../spotify-christmas-keysecret.txt', encoding="ascii") as txtfile:
    lines = txtfile.readlines()
    client_id = re.sub("client_id = ", "", lines[0])
    client_id = re.sub("\n","",client_id)

    client_secret = re.sub("client_secret = ", "", lines[1])
    client_secret = re.sub("\n", "", client_secret)

    print(client_id + "\n" + client_secret)

# # # Spotify authentication
credentials = oauth2.SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret)

token = credentials.get_access_token()
sp = spotipy.Spotify(auth=token)

# # # Import uri list
album_uris = []
with open("album-uri-edit.csv",encoding='utf-8') as urifile:
    csvreader = csv.reader(urifile)
    for line in csvreader:
        album_uris.append(line[1])


albums = []
#with open('christmas-uris.csv', 'w+', encoding='utf-8', newline='') as writefile:
#    csvwriter = csv.writer(writefile)
with open('christmas-albums.csv', 'a', encoding='utf-8',newline='') as writefile:
    writing = csv.writer(writefile)
    for uri in album_uris:
        #print("Working on:",uri)
        try:
            try:
                to_check = sp.album(uri)
            except:
                token = credentials.get_access_token()
                sp = spotipy.Spotify(auth=token)
                to_check = sp.album(uri)
            #print(len(albums))
            if 'US' in to_check['available_markets']:
                if len(to_check["genres"]) == 0:
                    if re.match("christmas", to_check["name"].lower()):
                        writing.writerow([to_check["name"], uri, "KNOWN"])
                        print([to_check["name"], uri, "KNOWN"])
                    else:
                        print([to_check["name"], uri, "UNKNOWN"])
                        writing.writerow([to_check["name"], uri, "UNKNOWN"])
                else:
                    if 'christmas' in to_check["genres"] or 'holiday' in to_check["genres"] or 'carols' in to_check["genres"] or 'chanukah' in to_check["genres"]:
                        print([to_check["name"], uri, "KNOWN"])
                        writing.writerow([to_check["name"], uri, "KNOWN"])
        except:
            print("something broke")