# Trakt2Letterboxd
 
This little Python tool can convert Trakt movie backups (at least, those from [this site](https://darekkay.com/blog/trakt-tv-backup/)) into a format that Letterboxd is happy with. 

The Letterboxd import page can be found [here](https://letterboxd.com/import/).

Some sample files can be found at [this path](https://github.com/Jordy3D/Trakt2Letterboxd/tree/main/Examples) showing an actual backup file, as well as the final .csv output ready for Letterboxd.

## Requirements
`python3`
`pandas`
`flatten-json`

## A few notes: 
It will NOT work for TV shows.
This is for a number of reasons:
- Letterboxd's support for TV shows is kinda spotty as it is
- The format is annoyingly different with TV shows and I am too tired as of the writing of this program to support it
- Even when things are successfully converted, Letterboxd rarely accurately connects what you submit with something on their system. This can be understandable (Black Butler the anime being picked up as the live-action film), but many others are outright incorrect.

The Trakt backup doesn't seem to list the first time a movie was watched, just the most recent. If you don't rewatch things often, this shouldn't be an issue, but it's something to consider if the Watch Dates being accurate is something you care about.

If someone is willing to use this work to make it some webtool, they're more than free to do so. Just let me know in a GitHub issue or something and I'll link to it here.
