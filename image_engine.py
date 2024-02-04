""" Image Engine: Script for scraping images."""

import requests
from bs4 import BeautifulSoup
import urllib
import os


def scrape_images(keyword, num_images=6):
    # Define the URL for Google Images search
    search_url = f"https://www.google.com/search?q={keyword}&tbm=isch"

    # Send a GET request to the search page
    response = requests.get(search_url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find image elements
    image_tags = soup.find_all('img')

    # Create a directory to store images
    if not os.path.exists("images_temp"):
        os.makedirs("images_temp")

    # Download images
    count = 0
    for img in image_tags:
        if count < num_images:
            img_url = img['src']
            img_name = os.path.join("images_temp", f"{keyword}_{count + 1}.jpg")

            try:
                # Download image using urllib
                urllib.request.urlretrieve(img_url, img_name)
                count += 1
                print(f"Downloaded {count} image(s)")
            except Exception as e:
                # Handle exceptions during image download
                print(f"Error downloading image: {str(e)}")
