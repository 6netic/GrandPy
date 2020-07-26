import requests
from grandpy import googleapi
import json

def test_googleapi(monkeypatch):
	
	#result = ["7 Cité Paradis, 75010 Paris, France", 48.8748465, 2.3504873]
	result = ["7 Cité Paradis, 75010 Paris, France", "Cité Paradis", 48.8748465, 2.3504873]
	

	class MockRequestGet:
		""" Making a mock for requests.get() """
		
		def __init__(self, url, params):
			self.url = "http://www.internet.com"
			self.params = {"address": result[0], "key": "dRt0tuyiG1"}
			#self.status_code = status_code
		
		
		def json(self):
	
			response = {
				'results': [{
								'formatted_address': result[0],
								'address_components': [{},{'long_name': result[1]}],
								'geometry': {'location': {'lat': result[2], 'lng': result[3]}}, 
							}]
			}
			
			return response
			
	monkeypatch.setattr("requests.get", MockRequestGet)
	instance = googleapi.AddressGps()
	coord = instance.calculation("openclassrooms")
	assert result == coord


'''
def test_googleapi(monkeypatch):
	""" Patching function for Google Api method """
	result = ['7 Cité Paradis, 75010 Paris, France', 'Cité Paradis', 48.8748465, 2.3504873]

	class MockResponse:
		
		def __init__(self):
			self.url = "https://googlemaps"
			#self.google_key = "dRt0tuyiG1"
			self.params = {"address" : "3 rue Monceault", "key" : "dRt0tuyiG1"}
			#self.sentence = sentence
			#self.status_code = 200
			

		def get_google(self, sentence):
			
			response_string = json.dumps(result) #Renvoie un type 'str'
			response_bytes = response_string.encode() #Renvoie un type 'bytes'
			return response_bytes


	def mock_get_infos():
			return MockResponse()

	monkeypatch.setattr("requests.get", mock_get_infos())
	#monkeypatch.setattr("grandpy.googleapi.AddressGps.calculation", mock_get_infos())
	g_result = googleapi.AddressGps()
	g_result.calculation("openclassrooms")
	#assert google_result == ['7 Cité Paradis, 75010 Paris, France', 'Cité Paradis', 48.8748465, 2.3504873]
'''
















