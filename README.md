# youtube_scraper

## About

- The backend for a proof-of-concept internal tool to help find and monitor copyrighted content.

- A Flask application that searches the YouTube Data API, can exclude specific channels from the search and saves data to a live PosgreSQL database.

- The data includes:

  > Channel Title, Channel ID, Video ID, Description, Thumbnail URL, and Publish Time

- The app is deployed continuously to Heroku and the PostgreSQL database is hosted on Supabase.

## Endpoint

**_⚠️ note_**: this endpoint is protected with an authorization Bearer token.

- The live base URL:

```
https://flask-youtube-scraper-a55f990bea9f.herokuapp.com/
```

- Local development URL:

```
localhost:5000/
```

### Search

```python
{{URL}}/api/search?query=<YOUR_SEARCH_QUERY>
```

Optionally exclude specific channels by name:

```python
{{URL}}/api/search?query=<YOUR_SEARCH_QUERY>&exclude=ChannelNameToExclude,AnotherChannelToExclude
```

**_for example_**: to search for "Lil Wayne" but exclude his official channel with his channel ID:

```python
{{URL}}/api/search?query=lil%20wayne&exclude=LilWayneVEVO
```

## Run Locally

### ‼️ Requirements:

- rename `.env.example` to just `.env` and add your environment variables

```bash
$ # Create virtual environment
$ venv venv
$ # Activate virtual environment
$ # If on Mac or Linux
$  source venv/bin/activate
$ # If on Windows
$ c:\>c:\Python35\python -m venv c:\path\to\venv
$ # Install dependencies
$ pip install -r requirements.txt
$ # Export Flask app
$ export FLASK_APP=app.py
$ # Run the development server
$ flask run
```
