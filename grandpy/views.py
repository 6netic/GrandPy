
from flask import Flask, render_template, jsonify, request
import requests, os
import json
from grandpy import control


app = Flask(__name__)
google_api_key = os.getenv("GOOGLE_API_KEY")


@app.route('/')
def index():
	""" Homepage when accessing the application """
	
	data = { 'google_api_key' : os.getenv('GOOGLE_API_KEY') }
	return render_template('index.html', data = data)


@app.route('/processing/', methods=["POST"])
def processing():
	""" That function is treating the request sent by the user """
	
	search_sentence = request.form.get('mySearch')
	cleaned_sentence = control.make_new_sentence(search_sentence)	
	coord = control.find_place(cleaned_sentence)
	address = coord[0]
	street_name = coord[1]
	latitude = coord[2]
	longitude = coord[3]
	
	page_id = control.show_page(latitude, longitude)
	description = control.show_description(page_id)
	
	return jsonify({
		"data"			: {
		"address" 		: address,
		"street_name" 	: street_name,
		"latitude" 		: latitude,
		"longitude" 	: longitude,
		"pageid"		: page_id,
		"description" : description
		}
	})



if __name__ == "__main__":
	app.run()

