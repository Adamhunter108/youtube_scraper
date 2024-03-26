# youtube_scraper

endpoint:
`localhost:5000/api/search?query=<YOUR_SEARCH_QUERY>`
or optionally exclude specific channels by name:
`localhost:5000/api/search?query=<YOUR_SEARCH_QUERY>&exclude=ChannelNameToExclude,AnotherChannelToExclude`

so to search for "Lil Wayne" but exclude his official channel with channelID:
`/api/search?query=lil%20wayne&exclude=LilWayneVEVO`

returns array of objects of first 10 results, data included: - videoId - channelId - channelTitle - description - thumbnailUrl - publishTime
