""" News Engine: Script for scrapping world and science news."""

import requests
from bs4 import BeautifulSoup
from voice_engine import speak


def get_news_world():
    """
    Fetch and speak world news headlines.
    This function fetches world news headlines from 'https://globalnews.ca/world/' and speaks them using text-to-speech.
    """

    news_list = []
    try:
        # Make a GET request to the specified URL
        url = 'https://globalnews.ca/world/'
        response = requests.get(url)

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all news headlines using BeautifulSoup
        headlines = soup.find('body').find_all("span", attrs={'class': 'c-posts__headlineText'})
        print(len(headlines))

        # Iterate through headlines and speak them
        for x in headlines[10:len(headlines)]:
            txt = x.text.strip()

            # Check if the headline is already in the list to avoid repetition
            if txt in news_list:
                continue
            news_list.append(txt)
            print(txt)
            speak(txt)

    except requests.RequestException as e:
        # Handle request-related exceptions
        print(f"Error fetching world news: {e}")
        speak("Error fetching world news. Please check your internet connection.")

    except Exception as e:
        # Handle unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        speak("An unexpected error occurred while fetching world news.")


def get_news_science():
    """
    Fetch and speak science news headlines.
    This function fetches science news headlines from 'https://www.sciencenews.org/topic/space' and speaks them using text-to-speech.
    """

    try:
        # Make a GET request to the specified URL
        url = 'https://www.sciencenews.org/topic/space'
        response = requests.get(url)

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find science news headlines using BeautifulSoup
        headlines = soup.find('body').find_all("p", attrs={'class': 'post-item-river__excerpt___SWLb7'})
        print(len(headlines))

        # Iterate through headlines and speak the first two
        for x in headlines[0:2]:
            txt = x.text.strip()
            print(txt)
            speak(txt)

    except requests.RequestException as e:
        # Handle request-related exceptions
        print(f"Error fetching science news: {e}")
        speak("Error fetching science news. Please check your internet connection.")

    except Exception as e:
        # Handle unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        speak("An unexpected error occurred while fetching science news.")
