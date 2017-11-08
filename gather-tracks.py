from musixmatch import Musixmatch
with open('../musixmatch-api.txt', encoding="ascii") as txtfile:
    API_KEY = txtfile.readline()

musixmatch = Musixmatch(API_KEY)
