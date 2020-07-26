#!/usr/bin/python3
# -*- coding: Utf-8 -*

import requests
from grandpy import parsewords
from grandpy import googleapi
from grandpy import wikiapi


def make_new_sentence(sentence):
	""" This function will remove all unnecessary words """
	
	parser = parsewords.Parse()
	cleaned_sentence = parser.transform_sentence_to_lower_without_apostrophes(sentence)
	cleaned_sentence = parser.remove_special_characters_from_list(cleaned_sentence)
	cleaned_sentence = parser.transform_sentence_to_list(cleaned_sentence)
	cleaned_sentence = parser.create_new_sentence(cleaned_sentence)
	return cleaned_sentence


def find_place(cleaned_sentence):
	""" This function looks for the address of the place you're looking for """
	
	address_gps = googleapi.AddressGps()
	coord = address_gps.calculation(cleaned_sentence)
	return coord


def show_page(latitude, longitude):
	""" This function shows a description of the place """
	
	place = wikiapi.PlaceInfo()
	page_id = place.search_pageid(latitude, longitude)
	return page_id


def show_description(page):
	""" This function shows a description of the place """
	
	place = wikiapi.PlaceInfo()
	description = place.search_description(page)
	return description

