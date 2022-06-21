import os
import requests as r
from urllib import request


API_KEY = 'ARAoAEvrlNOw3OpFXEH54FczEw4LRlrC9qBlFhDn'
ENDPOINT_URL = 'https://api.nasa.gov/planetary/apod?api_key='+API_KEY
LOG_FOLDER = '/var/api-logs/nasa.log'
OUTPUT_FOLDER = '/var/api-logs/nasa_wallpapers/'  


response_output = {
	"copyright": "Meiying Lee",
	"date": "2022-06-21",
	"explanation": "Does the Sun return to the same spot on the sky every day? No.  A better and more visual answer to that question is an analemma, a composite of images taken at the same time and from the same place over the course of a year. The featured analemma was compiled at 4:30 pm many afternoons from Taiwan during 2021, with the city skyline of Taipei in the foreground, including tall Taipei 101. The Sun's location in December -- at the December solstice -- is shown on the far left, while its location at the June solstice is captured on the far right. Also shown are the positions of the Sun throughout the rest of the day on the solstices and equinoxes.  Today is the June solstice of 2022, the day in Earth's northern hemisphere when the Sun spends the longest time in the sky.  In many countries, today marks the official beginning of a new season, for example winter in Earth's southern hemisphere.",
	"hdurl": "https://apod.nasa.gov/apod/image/2206/AnalemmaTaipei_Lee_1080.jpg",
	"media_type": "image",
	"service_version": "v1",
	"title": "Analemma over Taipei",
	"url": "https://apod.nasa.gov/apod/image/2206/AnalemmaTaipei_Lee_1080.jpg"
}

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
    