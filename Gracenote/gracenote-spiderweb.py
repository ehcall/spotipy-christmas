import requests
query_auth_xml = '<QUERIES><LANG>eng</LANG><AUTH><CLIENT>404121395-982A638E654509B14B7938FDB0B35778</CLIENT><USER>30500557063908317-6F587B65D18D0D688153EB5DD44274A8</USER></AUTH>'
search_query_xml = '<QUERY CMD="TRACK_SEARCH"><TEXT TYPE="TRACK_TITLE">jingle bells</TEXT></QUERY></QUERIES>'

xml = query_auth_xml + search_query_xml

r = requests.post('https://c404121395.web.cddbp.net/webapi/xml/1.0/', data=xml)
print(r.content)

