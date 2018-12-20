import csv

albums = []
with open("album-uris.csv",encoding='utf-8') as urifile:
    csvreader = csv.reader(urifile)
    for line in csvreader:
        if len(line) > 1:
            albums.append(line)
        else:
            print("blankline")

with open("album-uri-edit.csv", 'w+', encoding='utf-8', newline='') as urifile:
    csvwriter = csv.writer(urifile)
    for album in albums:
        csvwriter.writerow(album)