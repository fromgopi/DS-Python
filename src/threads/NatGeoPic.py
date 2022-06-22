import os
import requests as r
from urllib import request


API_KEY = 'ARAoAEvrlNOw3OpFXEH54FczEw4LRlrC9qBlFhDn'
ENDPOINT_URL = 'https://api.nasa.gov/planetary/apod?api_key='+API_KEY
LOG_FOLDER = '/var/api-logs/nasa.log'
OUTPUT_FOLDER = '/var/api-logs/nasa_wallpapers/'  

def get_apod_data():
    response = r.get(ENDPOINT_URL).json()
    return response
    

def download_pic():
    response_output = get_apod_data()
    date = response_output['date']
    title = response_output['title'].replace(" ", "_")
    media_type = response_output['media_type']
    apod_link = f'https://apod.nasa.gov/apod/ap{date.replace("-", "")[2:]}.html'
    hdurl = response_output['hdurl']
    image_name = title+'.jpg'
    file_path = OUTPUT_FOLDER + image_name
    if not os.path.exists(file_path):
        request.urlretrieve(hdurl, file_path)

if __name__ == '__main__':
    # get_apod_data()
    download_pic()
