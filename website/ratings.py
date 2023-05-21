from flask import Blueprint, render_template, request, redirect, url_for
import requests as requests
from thefuzz import process

ratings = Blueprint("ratings", __name__)

# Each hall key has the place_id, image, and rating (?/5) of the hall as the value.
hallIDs = {"Buxton": ["ChIJl-61hrlAwFQRSsuaxoMTm7I", "buxton.jpg"],
           "Finley": ["ChIJ_3mYZLhAwFQR7XyBRBJgcxw", "finley.jpg"], 
            "Hawley": ["ChIJgeovJ7pAwFQRNO3tCp1EiVg", "hawley.jpg"],
            "Sackett": ["ChIJnUd4OLpAwFQRSqnwlInD_CI", "sackett.jpg"],
            "Bloss": ["ChIJhYCPksdAwFQRwiByLE24TQc", "bloss.jpg"],
            "Cauthorn": ["ChIJqct4rLtAwFQRuwPGTH0atWk", "cauthorn.jpg"],
            "Weatherford": ["ChIJrdHJd7lAwFQR5PrQRWqJZps", "weatherford.jpg"],
            "Callahan": ["ChIJtaNhF79AwFQRUhBeSyyMOwg", "callahan.jpg"],
            "Poling": ["ChIJ_bgYkblAwFQRyiczeStGLuI", "poling.jpg"],
            "McNary": ["ChIJ0Rh2p79AwFQRTuzrVy45L-U", "mcnary.jpg"],
            "Tebeau": ["ChIJjX4nXL9AwFQR-BUdk4lWhVI", "tebeau.jpg"],
            "West": ["ChIJ9R3p_rlAwFQRSkObm7RtdwM", "west.jpg"],
            "Dixon": ["ChIJv8Ibwb9AwFQRIwDV2rxfI4U", "dixon-lodge.jpg"],
            "ILLC": ["ChIJR_dGmcdAwFQRwdunNu8qmAE", "illc.jpg"],
            "Halsell": ["ChIJ6_8dgLhAwFQRYclL1p0Ms8A", "halsell.jpg"]}
allReviews = []

# Takes each hall and feeds Google Places API the ID of the hall to get the reviews and rating of the hall
for hall, hallInfo in hallIDs.items():
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={hallInfo[0]}&fields=reviews%2Crating&key=CONFIDENTIAL"
    response = requests.request("GET", url, headers={}, data={})
    reviews = response.json().get('result').get('reviews')
    for review in reviews:
        allReviews.append([review.get('rating'), review.get('text'), hall])
    hallInfo.append(response.json().get('result').get('rating'))

# Sets a route for the dorms page and passes in the necessary information collected from the API to the html file
@ratings.route('/dorms', methods=["GET", "POST"])
def dorms():
    # Only the dorms page with the hall names that are similar to the search query
    if request.method == "POST":
        search = request.form["search"]
        searchResults = process.extract(search, hallIDs.keys()) # [(hall, score), (hall, score), ...]
        searchResults = [result[0] for result in searchResults if result[1] > 60] # only saves scores above 60
        return render_template('dorms.html', allReviews=allReviews, hallIDs=hallIDs, search=search, searchResults=searchResults)
    return render_template('dorms.html', allReviews=allReviews, hallIDs=hallIDs, hall=None)

# Route for the individual hall pages, passes in the hall name and the information collected from the API
@ratings.route('/dorms/<hall>')
def hall(hall):
    return render_template('halls.html', hall=hall, allReviews=allReviews, hallIDs=hallIDs)
