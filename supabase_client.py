from supabase import create_client, Client

supabase: Client = None

def init_supabase(url: str, key: str):
    global supabase
    supabase = create_client(url, key)


def insert_videos(videos):
    if not videos:
        return {'data': None, 'error': 'No videos to insert'}
    
    response = supabase.table("videos").upsert(videos, on_conflict="videoId").execute()

    if hasattr(response, 'error') and response.error:
        error_message = response.error.message if response.error.message else "Unknown error"
        return {'data': None, 'error': error_message}
    else:
        return {'data': response.data, 'error': None}
