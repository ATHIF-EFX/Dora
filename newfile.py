import youtube_dl

video = {}
url = "https://youtu.be/_42iByu2OxI"
with youtube_dl.YoutubeDL(video) as ydl:
	ydl.download([url])