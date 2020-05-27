import requests
import sys
f = open('program.133517.MP4.M20.m3u8')
arr = []
for line in f.readlines():
    if line[0] == '/':
        arr.append(line)
baseur = "https://iphone.c-spanvideo.org"
f = open('C:/Users/Carter Szukala/Documents/Advent/video_files/'+sys.argv[1]+'.mp4', 'wb')
for files in arr:
    print(baseur+files)
    header = {'Host': 'iphone.c-spanvideo.org',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
'Accept': '*/*',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Origin': 'https://www.c-span.org',
'Connection': 'keep-alive',
'Referer': 'https://www.c-span.org/video/?159295-1/2000-presidential-candidates-debate&event=159295&playEvent&auto',
'TE': 'Trailers'
    }
    r = requests.get(url = baseur + files.rstrip(), headers= header)
    
    f.write(r.content)
    print(r)


