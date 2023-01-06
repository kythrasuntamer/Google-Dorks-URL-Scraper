import requests
from bs4 import BeautifulSoup

# Set the base URL for the Google search
base_url = "https://www.google.com/search?q="

# Set the Google dork that you want to search for
dork = "ext:inc \"pwd=\" \"UID=\""


# Set the number of pages of results that you want to scrape
num_pages = 20

# Initialize a list to store the results
results = []

# Iterate over the pages of results
for page in range(num_pages):
    # Send an HTTP request to the Google search URL
    response = requests.get(base_url + dork + "&start=" + str(page * 10))

    # Parse the HTML of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all of the search result links on the page
    links = soup.find_all("a")

    # Iterate over the links and store the result URLs
    for link in links:
        href = link.get("href")
        if href.startswith("/url?q="):
            results.append(href7:)

# Write the results to a file
with open("results.txt", "w") as f:
    for result in results:
        f.write(result + "\n")
