from __future__ import unicode_literals
from lxml.html import parse
from urllib2 import urlopen
import youtube_dl

parsed = parse(urlopen('https://www.youtube.com/watch?v=6jf5qm21FPM&list=PLnxdvka2GM3AQrpR8iTf3fTkuRjjTw3hl'))
doc = parsed.getroot()

links = doc.findall('.//a')
videos = []

for i in links:
	if '&index=' in i.get('href'):
		videos.append(i.get('href')[9:20])

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	for video in videos:
		ydl.download(['http://www.youtube.com/watch?v={}'.format(video)])