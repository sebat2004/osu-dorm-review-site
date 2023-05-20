from flask import Blueprint, render_template
import requests as requests

ratings = Blueprint("ratings", __name__) 

url = "https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJl-61hrlAwFQRSsuaxoMTm7I&fields=reviews%2Crating&key=AIzaSyBYII-GqPLWO7JRqsOpCd6Z7JwvFQq9g54"

payload= {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

reviews = response.json().get('result').get('reviews')
rating = response.json().get('result').get('rating')
for review in reviews:
    currRating = review.get('rating')
    reviewMessage = review.get('text')

@ratings.route('/dorms')
def dorms():
    return render_template('dorms.html', rating=rating, reviews=reviews, currRating=currRating, reviewMessage=reviewMessage)