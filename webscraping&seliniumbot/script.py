import requests
import requests.exceptions
from collections import deque
import re
import xlsxwriter
import os, io
import webbrowser
import urllib.request


path="playlist.xlsx"
workbook=xlsxwriter.Workbook(path)
worksheet=workbook.add_worksheet()
playlist=set()
final_list=deque()
max=0
for i in range(1, 10):
    url="https://www.insomnia.gr/forums/topic/695707-%CF%80%CE%BF%CE%B9o-%CF%84%CF%81%CE%B1%CE%B3%CE%BF%CF%8D%CE%B4%CE%B9-%CE%B1%CE%BA%CE%BF%CF%8D%CF%84%CE%B5-%CF%84%CF%8E%CF%81%CE%B1/page/"+str(i)
    print("have done"+ str(i) +" of 492 \n" )
    try:
        response=requests.get(url)
    except (requests.exceptions.ConnectionError,requests.exceptions.MissingSchema):
        continue
    
    
    new_songs=set(re.findall(r'https:\/\/www\.youtube\.com\/embed\/([\w\-\_]*)',response.text ))
  
    playlist.update(new_songs)
print(playlist)
worksheet.write(0,0,"youtube_links")
counter=1

for song in playlist:
    if not song in final_list:
        final_list.append(song)

for song in final_list:    
    song="https://www.youtube.com/watch?v="+song
    print(song)
    row=counter
    counter+=1
    worksheet.write(row,0,song)
    max+=1

##Gia liges selides doulevei san unlisted selida. gia ola skalwnei giati einai terastio to string.
#listOfVideos="http://www.youtube.com/watch_videos?video_ids=" + ','.join(final_list)
#print(listOfVideos)
#file=open("list.txt", "r+")
#file.write(listOfVideos)
#file.close()




workbook.close()