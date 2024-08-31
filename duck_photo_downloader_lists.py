"""All variables and lists here used for input validation and storing duck photo links"""

import requests  # Web scraping/API access module
from duck_photo_downloader_funcs import *

# API links

URL = 'https://random-d.uk/api/random'  # API link for random-d-uk, returns a dictionary containing link:

# Example of dictionary pulled from link. This is not used at all.
api_pull_example = {"message": "Powered by random-d.uk",
                    "url": 'https://random-d.uk/api/142.jpg'}

# Personal note. random and quack do the same thing
usable_api = ('random-d.uk/api/random', 'random-d.uk/api/quack')

# Lists

duplicate_names = []  # Stores every duck name to prevent user from making duplicate filenames
duck_links = []  # Contains all links scrapped from website

# Counter variable for loops in functions and/or main

duck_tag = 0  # Tracks the file # the user is naming during file naming/download loop
completed_links = 0  # Tracks number of links successfully acquired during link collection loop
