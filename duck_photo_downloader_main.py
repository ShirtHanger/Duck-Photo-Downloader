"""Main file for project, all user input here"""

import requests  # Web scraping/API access module
from duck_photo_downloader_lists import *
from duck_photo_downloader_funcs import *

duck_number = int(input("How many duck photos: "))

print("-----")

# Loop collects unique URLs from api dictionary, then puts them all in a list

collect_duck_links(duck_number, completed_links, duck_links, URL)

print("-----")

print("Your ducks are here!")
print("Now give them a place to stay!")

print("You must paste your desired destination path in your file explorer")
print("Example below: ")
print("-----")
print("C:/Users/newci/OneDrive/Downloads/duck_file_home")
print("Folder(s) must already exist): ")
print("-----")
file_location = input("Paste it here: ")

print("-----")

print("Time to name all", duck_number, "of your ducks!")


# Asks user to name each file successively
download_duck_files(duck_links, duck_tag, duplicate_names, file_location)

print("-----")
print("-----")
print("All the ducks are here! They're happy!")
print("-----")
print("Enjoy")
