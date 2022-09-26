import pandas as pd
import json
import sys
import os


def convert(trakt_file):
    invalid_keys = ['"slug":', '"trakt":', '"tvdb":', '"tvrage":',
                    '"plays":', '"last_updated_at":', '"reset_at":',
                    '"movie":', '"ids":', '"show":']

    with open(trakt_file, encoding='utf-8') as f:
        print("Opening the file...")
        input_json = json.load(f)

        # Clean JSON
        print("Cleaning JSON...")
        pf = json.dumps(input_json, indent=0)

        with open('cleaned.json', 'w') as cj:
            cj.write(pf)

        # Parse JSON
        print("Parsing JSON...")
        with open('cleaned.json', 'r') as cj, open('parsed.json', 'w') as pj:
            for line in cj:
                if not any(key in line for key in invalid_keys):
                    if "}" in line and not "," in line:
                        line = ""
                    if '"last_watched_at"' in line:
                        line = line.replace('last_watched_at', 'WatchedDate')
                    if '"imdb"' in line:
                        line = line.replace('imdb', 'imdbID')
                    if '"tmdb"' in line:
                        line = line.replace('tmdb', 'tmdbID')
                    if '"year"' in line:
                        line = line.replace('year', 'Year')
                    if '"title"' in line:
                        line = line.replace('title', 'Title')
                    if ']' in line:
                        line = "}\n]"

                    pj.write(line)

        # Convert to CSV
        print("Converting JSON...")
        with open('parsed.json', encoding='utf-8') as inputfile:
            df = pd.read_json(inputfile)

            df = df[['Title', 'Year', 'imdbID', 'tmdbID', 'WatchedDate']]
            df.to_csv("Trakt2Letterboxd.csv", index=False)
            # df = pd.read_csv('csvfile.csv')
            # df.to_csv("csvfile.csv", index=False)

        # Cleanup temp files
        print("Cleaning up...")
        os.remove("cleaned.json")
        os.remove("parsed.json")

    print("Converted.")


if len(sys.argv) == 1:
    print("Please drop a file onto Trakt2Letterbox.py")
else:
    trakt_file = sys.argv[1]
    try:
        print("Trying to convert...")
        convert(trakt_file)
    except:
        print("An error occurred. Please ensure you're using a valid file.")
