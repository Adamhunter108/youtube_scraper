# youtube_scraper

## About ℹ️

- A Flask application that can search YouTube, exclude specific channels and saves data to a live PosgreSQL database.

- The data includes:
  > Channel Title, Channel ID, Video ID, Description, Thumbnail URL, and Publish Time

## Endpoint

- `localhost:5000/api/search?query=<YOUR_SEARCH_QUERY>`

- or optionally exclude specific channels by name:

  - `localhost:5000/api/search?query=<YOUR_SEARCH_QUERY>&exclude=ChannelNameToExclude,AnotherChannelToExclude`

- _for example_: to search for "Lil Wayne" but exclude his official channel with channelID:
  - `/api/search?query=lil%20wayne&exclude=LilWayneVEVO`

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
