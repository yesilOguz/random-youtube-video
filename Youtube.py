from googleapiclient.discovery import build
import random

youtubeApi = "AIzaSyAmXIZ2vp7-hspVf9cAB1OHRBxF5jkyb7I"
apiServiceName = 'youtube'
apiVersion = 'v3'

prefix = ['VIDEO', 'VIDEO ','VIDEO-', 'VIDEO_', 'IMG ', 'IMG_', 'IMG-', 'DSC ', 'VID']
postfix = [' MOV', '.MOV', 'MOV', 'AVI', ' AVI', '.AVI', ' MP4', '.MP4', 'MP4']

def youtube_search():
    youtube = build(apiServiceName, apiVersion, developerKey=youtubeApi)
    
    search_response = youtube.search().list(
        q=random.choice(prefix) + str(random.randint(999, 9999)) + random.choice(postfix),
        part='snippet',
        maxResults=5
          ).execute()

    videos = []
    video = ""

    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append('%s' % (search_result['id']['videoId']))
    
    if(len(videos) != 0):
        
        return "https://www.youtube.com/watch?v=" + videos[random.randint(0, len(videos)-1)]
        
    else:
        return youtube_search()

print(youtube_search())



