# -*- coding: utf-8 -*-
#mr-Ucar2023

#On purpose, the output is detailed for further analysis. 
#But you can import some libraries and save and categorize the output
#or just minimize the output for the simple definition if it is what you need.

"""
Very simple python script to look up a word and its synonym & antonym

"""
import requests
import json

base_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
word2lookup = input("Write the word that you want to look up :  ")
nihai = base_url + word2lookup


response = requests.get(nihai)


print(json.dumps(response.json(), indent = 2))


data = response.json()


print(data)


response = requests.get(nihai).json()
print(response)
