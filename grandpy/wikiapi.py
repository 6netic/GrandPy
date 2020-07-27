#!/usr/bin/python3
# -*- coding: Utf-8 -*

import requests, json

class PlaceInfo:
	""" This class deals with requesting MediaWiki api """

	def __init__(self):
		""" Initializing """
		
		self.url = "https://fr.wikipedia.org/w/api.php"


	def search_pageid(self, latitude, longitude):
		""" this function picks up a page related to the place """
		
		params = {
			"format" : "json", # format de la réponse
			"action" : "query",
			"list" 	 : "geosearch",
			"gsradius" : 1000,
			"gscoord" : "{}|{}".format(latitude, longitude)
		}
		
		response = requests.get(self.url, params=params)
		
		if response.status_code != 200:
			return False
		else:
			content = response.json()
			pageid = content["query"]["geosearch"][0]["pageid"]
			return pageid
		


	def search_description(self, page):
		""" method that looks nearby our place """
		
		param = {
			"format" : "json",
			"action" : "query",
			"prop" : "extracts",
			"exsectionformat" : "plain",
			"exlimit" : 1,
			"exchars" : 400,
			"explaintext" : True,
			"pageids" : page
		}

		response = requests.get(self.url, params=param)
		
		if response.status_code != 200:
			return False
		else:
			content = response.json()
			description = content["query"]["pages"][str(page)]["extract"]
			return description
		




