from flask import Blueprint, render_template
import requests as requests

ratings = Blueprint("ratings", __name__)

# Initializes the hallIDs dictionary with the hall name as the key and the ID of the hall as the value. Later we append the rating of the hall to the list of values
hallIDs = {"Buxton Hall": ["ChIJl-61hrlAwFQRSsuaxoMTm7I", "buxton.jpg"],
           "Finley Hall": ["ChIJ_3mYZLhAwFQR7XyBRBJgcxw", "finley.jpg"], 
            "Hawley Hall": ["ChIJgeovJ7pAwFQRNO3tCp1EiVg", "hawley.jpg"],
            "Sackett Hall": ["ChIJnUd4OLpAwFQRSqnwlInD_CI", "sackett.jpg"],
            "Bloss Hall": ["ChIJhYCPksdAwFQRwiByLE24TQc", "bloss.jpg"],
            "Cauthorn Hall": ["ChIJqct4rLtAwFQRuwPGTH0atWk", "cauthorn.jpg"]}
reviewInfo = []

# Takes each hall and feeds Google Places API the ID of the hall to get the reviews and rating of the hall
for hall, hallInfo in hallIDs.items():
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={hallInfo[0]}&fields=reviews%2Crating&key=AIzaSyA-RLVYrsBL8C-8AzLT17CfKFjI31MLsko"
    response = requests.request("GET", url, headers={}, data={})
    hallInfo.append(response.json().get('result').get('rating'))
    reviews = response.json().get('result').get('reviews')
    for review in reviews:
        reviewInfo.append([review.get('rating'), review.get('text'), hall])

# Sets a route for the dorms page and passes in the necessary information collected from the API to the html file
@ratings.route('/dorms')
def dorms():
    return render_template('dorms.html', reviewInfo=reviewInfo, hallIDs=hallIDs)
