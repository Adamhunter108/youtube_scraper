from flask import Flask, request, jsonify
from settings import Config
from youtube_api import youtube_search

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def hello_world():
    # Accessing configuration variables through the app's config dictionary
    return f'Your API Key is: {app.config["YOUTUBE_API_KEY"]}'


@app.route('/search')
def search():
    query = request.args.get('query', '')
    if not query:
        return jsonify({'error': 'Missing query parameter'}), 400
    
    # exclude videos from a specific channel
    excluded_channels = ['LilWayneVEVO']
    results = youtube_search(app.config['YOUTUBE_API_KEY'], query, excluded_channels)
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
