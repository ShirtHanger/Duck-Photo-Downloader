"""Functions for downloading duck photos and accessing API using requests package"""

import requests  # Web scraping/API access module
from duck_photo_downloader_lists import *

"""Function for bulk download, can also be used for single download"""


def collect_duck_links(request_amount, completed_links, link_list, url):

    """Collects links of duck photo(s) from random duck API"""

    # Loop collects unique URLs from api dictionary, then puts them all in a list
    for photo in range(request_amount):
        # response and each duck_link are defined in loop to create a new link
        response = requests.get(url)
        duck_link = response.json()['url']  # 'url' is key for the duck link in the API dictionary
        # Adds each new URL to list
        link_list.append(duck_link)
        # Updates user on progress
        completed_links += 1
        print("Collecting ducks... (" + str(completed_links) + "/" + str(request_amount) + ")")


def download_duck_files(link_list, item_tag, duplicate_names, file_location):

    """Downloads links that were collected into list, allows user to name each one"""

    for link in link_list:

        # Creates extension variable for .jpg or .gif photos
        extension = link_extension_fix(link)

        # User names duck file here
        item_tag += 1
        item_name = input("Give a name to duck #" + str(item_tag) + ": ")
        while item_name in duplicate_names:
            print("We already have a", item_name, "here!")
            item_name = input("Give this one a unique name, it's special: ")
        duplicate_names.append(item_name)

        # Takes input and tweaks to allow access to file explorer
        duck_filename = folder_path_fix(item_name, extension, file_location)

        # Downloads duck photo to computer using requests module
        pull_duck_file(link, duck_filename[1], duck_filename[0])
        # [1] is the pathway, [2] is the file.jpg name.


"""

Mini functions listed below

"""

# Creates extension variable for .jpg or .gif photos


def link_extension_fix(image_link):

    """Creates extension variable for proper file naming"""

    if image_link.endswith("jpg"):  # String method returns true if something ends with specified value
        extension = '.jpg'
    else:
        extension = '.gif'
    return extension


def folder_path_fix(item_name, extension, file_location):

    """Takes input and tweaks to allow access to file explorer"""

    duck_filename = item_name + extension
    duck_file_final = file_location + '/' + duck_filename
    # Return both file.jpg and the path, as a tuple
    return duck_filename, duck_file_final


def pull_duck_file(link, duck_file_final, duck_filename):
    scraped_image = requests.get(link)

    with open(duck_file_final, 'wb') as f:
        f.write(scraped_image.content)
    print(duck_filename, "downloaded!")
