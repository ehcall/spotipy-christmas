from Gracenote import pygn

#store this later

clientID = '404121395-982A638E654509B14B7938FDB0B35778' # Enter your Client ID here
userID = pygn.register(clientID)

metadata = pygn.search(clientID=clientID, userID=userID, track='"jingle bells"')

print(type(metadata))