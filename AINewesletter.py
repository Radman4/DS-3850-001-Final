import tkinter
import openai
import newsapi
import os
#sample of the newsapi 
import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=API_KEY')
response = requests.get(url)
print(response.json())

class NewsApp: 
    def __init__(self):
        pass
