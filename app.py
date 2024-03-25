from flask import Flask
from settings import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def hello_world():
    # Accessing configuration variables through the app's config dictionary
    return f'Your API Key is: {app.config["YOUTUBE_API_KEY"]}'


if __name__ == '__main__':
    app.run(debug=True)
