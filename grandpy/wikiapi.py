#!/usr/bin/python3
# -*- coding: Utf-8 -*

import requests, json

class PlaceInfo():
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
		if response.status_code == 200:
			content = json.loads(response.content.decode('utf-8'))
			self.pageid = content["query"]["geosearch"][0]["pageid"]
			return self.pageid
		else:
			print("La requete a donné une erreur")


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
		if response.status_code == 200:
			#info_search = response.json()
			content = json.loads(response.content.decode('utf-8'))
			description = content["query"]["pages"][str(page)]["extract"]
			#self.extract = info_search["query"]["pages"][str(self.pageid)]["fullurl"]
			print("Mais t'ai-je déjà raconté l'histoire de ce lieu ?")
			#self.dictionary_search.append(self.extract)
			#self.dictionary_search.append(self.fullurl)
			#print(description)
			return description
		else:
			print("Une erreur est survenue lors de la recherche de la page")




def main():
	page_search = PlaceInfo()
	latitude = 48.8748465
	longitude = 2.3504873
	pageid = page_search.search_pageid(latitude, longitude)
	page_search.search_description(pageid)


if __name__ == '__main__':
	main()







