from googleapiclient.discovery import build
import random

# YouTube API constants
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
YOUTUBE_API_KEY = "AIzaSyAmXIZ2vp7-hspVf9cAB1OHRBxF5jkyb7I"

# Common prefixes and postfixes for YouTube video titles
PREFIXES = ['VIDEO', 'VIDEO ', 'VIDEO-', 'VIDEO_', 'IMG ', 'IMG_', 'IMG-', 'DSC ', 'VID']
POSTFIXES = [' MOV', '.MOV', 'MOV', 'AVI', ' AVI', '.AVI', ' MP4', '.MP4', 'MP4']

def youtube_search():
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=YOUTUBE_API_KEY)
    
    # Build a random query string using one of the common prefixes and postfixes
    query = random.choice(PREFIXES) + str(random.randint(999, 9999)) + random.choice(POSTFIXES)
    
    search_response = youtube.search().list(
        q=query,
        part='snippet',
        maxResults=5
    ).execute()
    
    videos = []
    
    # Get a list of video IDs from the search results
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append('%s' % (search_result['id']['videoId']))
    
    # If no videos were found, try again with a new random query
    if not videos:
        return youtube_search()
    
    # Return a random video from the list of found videos
    return "https://www.youtube.com/watch?v=" + videos[random.randint(0, len(videos)-1)]

# Print a random YouTube video URL
print(youtube_search())
