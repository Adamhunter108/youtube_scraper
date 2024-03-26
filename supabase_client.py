from supabase import create_client, Client

supabase: Client = None

def init_supabase(url: str, key: str):
    global supabase
    supabase = create_client(url, key)