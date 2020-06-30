
# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify
import json
import requests
import googlemaps
#from functions import extract_keywords

app = Flask(__name__)

#gmaps = googlemaps.Client(key='AIzaSyBFwyV7Ne-QtBvFXAgiuI2RjqgcSVBGWaA')
GOOGLE_API_KEY = "AIzaSyBFwyV7Ne-QtBvFXAgiuI2RjqgcSVBGWaA"
GOOGLEMAPS_API_URL = "https://maps.googleapis.com/maps/api/geocode/json?address=Openclassrooms&key=" + GOOGLE_API_KEY



@app.route("/")
def hello():
	return "Hello World!"

@app.route("/google/")
def google():
	#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
	response = requests.get(GOOGLEMAPS_API_URL)
	content = json.loads(response.content.decode('utf-8'))

	if response.status_code != 200:
		return jsonify({
						"status": "error",
						"message": "Your request failed. Here's the error message : {}".format(content["message"])
						}), 500

	results = content["results"]
	street_number = results[0]["address_components"][0]["long_name"]
	street_name = results[0]["address_components"][1]["long_name"]
	return jsonify({
		"status"	: "ok",
		"data"		:{
			"street_number" : street_name,
			"street_name" : street_number
			}
		})








if __name__ == "__main__":
	app.run(debug=True)








'''
@app.route('/api/news/')
def get_news():
 
    response = requests.get(NEWS_API_URL)

    content = json.loads(response.content.decode('utf-8'))

    if response.status_code != 200:
        return jsonify({
            'status': 'error',
            'message': 'La requête à l\'API des articles d\'actualité n\'a pas fonctionné. Voici le message renvoyé par l\'API : {}'.format(content['message'])
        }), 500


    keywords, articles = extract_keywords(content["articles"])

    return jsonify({
        'status'   : 'ok',
        'data'     :{
            'keywords' : keywords[:100], # On retourne uniquement les 100 premiers mots
            'articles' : articles
        }
    })
-------------------------------
@responses.activate
    def test_simple_geocode(self):
        responses.add(
            responses.GET,
            "https://maps.googleapis.com/maps/api/geocode/json",
            body='{"status":"OK","results":[]}',
            status=200,
            content_type="application/json",
        )

        results = self.client.geocode("Sydney")

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual(
            "https://maps.googleapis.com/maps/api/geocode/json?"
            "key=%s&address=Sydney" % self.key,
            responses.calls[0].request.url,
        )

'''








