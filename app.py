from flask import Flask, request, jsonify
from settings import Config
from youtube_api import youtube_search
from supabase_client import init_supabase 

app = Flask(__name__)
app.config.from_object(Config)

init_supabase(app.config['SUPABASE_URL'], app.config['SUPABASE_KEY'])

@app.route('/')
def hello_world():
    # Accessing configuration variables through the app's config dictionary
    # return f'Your API Key is: {app.config["YOUTUBE_API_KEY"]}'
    return "this is the youtube content scraper backend."


@app.route('/api/search')
def search():
    query = request.args.get('query', '')
    exclude = request.args.get('exclude', '')

    if not query:
        return jsonify({'error': 'Missing query parameter'}), 400

    # Split the exclude string into a list, if provided
    excluded_channels = exclude.split(',') if exclude else []

    results = youtube_search(app.config['YOUTUBE_API_KEY'], query, excluded_channels)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
