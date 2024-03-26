import requests

def parse_youtube_response(response, excluded_channel_titles=None):
    """
    Parses the YouTube API response and extracts videoId, channelId, channelTitle, description, thumbnailUrl, publishTime
    Can exclude videos from specific channels.

    :param response: The JSON response from the YouTube API.
    :param excluded_channel_titles: A list of channel titles to exclude.
    :return: A list of dictionaries (array of objects) with video details.
    """
    videos = []
    for item in response.get('items', []):
        # Skip videos from excluded channels
        if excluded_channel_titles and item['snippet']['channelTitle'] in excluded_channel_titles:
            continue

        video_details = {
            'videoId': item['id']['videoId'],
            'channelId': item['snippet']['channelId'],
            'channelTitle': item['snippet']['channelTitle'],
            'description': item['snippet']['description'],
            'thumbnailUrl': item['snippet']['thumbnails']['default']['url'],
            'publishTime': item['snippet']['publishTime'],
        }
        videos.append(video_details)
    return videos

def youtube_search(api_key, query, excluded_channel_titles=None):
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'part': 'snippet',
        'q': query,
        'key': api_key,
        'maxResults': 10,
        'type': 'video',
    }
    
    response = requests.get(search_url, params=params).json()  # Get JSON response directly
    # Parse the response to extract video details
    return parse_youtube_response(response, excluded_channel_titles)
