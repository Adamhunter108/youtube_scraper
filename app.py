from flask import Flask, request, jsonify, abort
from settings import Config
from youtube_api import youtube_search
from supabase_client import init_supabase, insert_videos 

app = Flask(__name__)
app.config.from_object(Config)

init_supabase(app.config['SUPABASE_URL'], app.config['SUPABASE_KEY'])

# @app.route('/')
# def hello_world():
#     return "this is the youtube content scraper backend."

def check_auth_token():
    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
        if token == app.config['AUTH_TOKEN']:
            return True
    abort(403)

@app.route('/api/search')
def search():
    check_auth_token()
    
    query = request.args.get('query', '')
    exclude = request.args.get('exclude', '')

    if not query:
        return jsonify({'error': 'Missing query parameter'}), 400

    excluded_channels = exclude.split(',') if exclude else []
    results = youtube_search(app.config['YOUTUBE_API_KEY'], query, excluded_channels)

    insert_response = insert_videos(results)
    
    if insert_response.get('error'):
        return jsonify({'error': 'Failed to insert videos into database', 'details': insert_response['error']}), 500

    return jsonify(results)

    
if __name__ == '__main__':
    app.run(debug=True)
