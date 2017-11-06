import spotipy
import re


# # # Import client id and client secret
with open('../spotify-christmas-keysecret.txt') as txtfile:
    lines = txtfile.readlines()
    client_id = re.sub("client_id = \"", "", lines[0])
    client_id = re.sub(r"\"\n","",client_id)

    client_secret = re.sub("client_secret = \"", "", lines[1])
    client_secret = re.sub("\"", "", client_secret)

