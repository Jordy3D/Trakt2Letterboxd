# Trakt2Letterboxd
 
This little Python tool can convert Trakt movie backups (at least, those from [this site](https://darekkay.com/blog/trakt-tv-backup/)) into a format that Letterboxd is happy with. 

The Letterboxd import page can be found [here](https://letterboxd.com/import/).

Some sample files can be found at [this path](https://github.com/Jordy3D/Trakt2Letterboxd/tree/main/Examples) showing an actual backup file, as well as the final .csv output ready for Letterboxd.

## Requirements
`python3`
`pandas`

## Usage
Drop a valid backup file from the above link (only known-working ones being watched_movies.txt and watched_shows.txt) onto Trakt2Letterboxd.py

## A few notes: 
It may not work well for TV shows.
This is because TV shows are far from Letterboxd's focus. An early version of this tool would fail spectacularly every time it tried to do TV things, but now it's at least somewhat capable. Mileage may vary.

The Trakt backup doesn't seem to list the first time a movie was watched, just the most recent. If you don't rewatch things often, this shouldn't be an issue, but it's something to consider if the Watch Dates being accurate is something you care about.

If someone is willing to use this work to make it some webtool, they're more than free to do so. Just let me know in a GitHub issue or something and I'll link to it here.
