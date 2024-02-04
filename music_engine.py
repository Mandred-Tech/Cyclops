""" Music Engine: Script for playing music and searching YouTube videos."""

import webbrowser
import urllib.request
import re

# Define YouTube playlist URLs for different music types
pop_url = "https://www.youtube.com/watch?v=PIh2xe4jnpk&list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj&pp=iAQB8AUB"
classical_url = "https://www.youtube.com/watch?v=nj2GILDFiE8&list=PL2788304DC59DBEB4&pp=iAQB8AUB"
techno_url = "https://www.youtube.com/watch?v=3yreIYeiKHw&list=PLWcttt0SQjI_r_lyii1pJvDQ-2R94DBV2&pp=iAQB8AUB"
rock_url = "https://www.youtube.com/watch?v=kPBzTxZQG5Q&list=PLyORnIW1xT6wFALM5dZlkFhOULbToFok3&pp=iAQB8AUB"

# Specify the path where your web browser is
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

# Register the 'brave' browser
webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))

# Get the 'brave' browser
browser = webbrowser.get('brave')


def play_music(music_type):
    # Open the 'brave' web browser to play the specified music type
    match music_type:
        case "pop":
            browser.open(pop_url, new=0)
        case "classical":
            browser.open(classical_url, new=0)
        case "techno":
            browser.open(techno_url, new=0)
        case "rock":
            browser.open(rock_url, new=0)
        case _:
            # Default to pop music if the specified type is not recognized
            browser.open(pop_url, new=0)


def play_youtube_video(what_to_play):
    # Search for YouTube videos based on the specified keyword
    search_keyword = what_to_play.split()
    search_url = "https://www.youtube.com/results?search_query=" + "+".join(search_keyword)
    html = urllib.request.urlopen(search_url)

    # Extract video IDs from the search results
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

    # Open the 'brave' web browser to play the second video from the search results
    link = "https://www.youtube.com/watch?v=" + video_ids[1]
    browser.open_new(link)

play_youtube_video("marmot")