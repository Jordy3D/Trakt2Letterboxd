import pandas as pd
import json
import sys
import os


def rename_dict_keys(dict, pairs):
    for pair in pairs:
        dict[pair[1]] = dict[pair[0]]
        del dict[pair[0]]
    return dict


def convert(trakt_file):
    with open(trakt_file, encoding='utf-8') as f:
        print("Opening the file...")
        input_json = json.load(f)

        # Clean JSON
        print("Cleaning JSON...")
        pf = json.dumps(input_json, indent=4)

        with open('cleaned.json', 'w') as cj:
            cj.write(pf)

        # Parse JSON
        print("Parsing JSON...")
        empty_json = []
        with open('cleaned.json', 'r') as cj, open('parsed.json', 'w') as pj:
            lj = json.load(cj)

            for item in lj:
                # Create empty Dict for shoving shit into
                empty = {}

                # Keys we care about
                raw_keys = ["last_watched_at"]
                sub_keys = ["title", "year"]
                id_keys = ["imdb", "tmdb"]

                for index, key in enumerate(sub_keys):
                    if 'movie' in item:
                        empty[sub_keys[index]] = item['movie'][sub_keys[index]]
                    else:
                        empty[sub_keys[index]] = item['show'][sub_keys[index]]

                for index, key in enumerate(sub_keys):
                    if 'movie' in item:
                        empty[id_keys[index]] = item['movie']['ids'][id_keys[index]]
                    else:
                        empty[id_keys[index]] = item['show']['ids'][id_keys[index]]

                for index, key in enumerate(raw_keys):
                    empty[raw_keys[index]] = item[raw_keys[index]]

                # Re-assign Dict values to themselves, effectively renaming them
                pairs = [["title", "Title"], ["year", "Year"], ["imdb", "imdbID"], ["tmdb", "tmdbID"],
                         ["last_watched_at", "WatchedDate"]]
                empty = rename_dict_keys(empty, pairs)

                empty_json.append(empty)

            pj.write(json.dumps(empty_json, indent=4))

        # Convert to CSV
        print("Converting JSON...")
        with open('parsed.json', encoding='utf-8') as inputfile:
            df = pd.read_json(inputfile)
            df.to_csv("Trakt2Letterboxd.csv", index=False)

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
