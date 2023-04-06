import logging
import logging.handlers
import os
import time
import requests as r
from urllib import request
from BingWallpaper import set_mac_screen_background

API_KEY = 'ARAoAEvrlNOw3OpFXEH54FczEw4LRlrC9qBlFhDn'
ENDPOINT_URL = 'https://api.nasa.gov/planetary/apod?api_key='+API_KEY
LOG_FOLDER = '/var/api-logs/nasa.log'
OUTPUT_FOLDER = '/var/api-logs/nasa_wallpapers/'
PIC_FOLDER = OUTPUT_FOLDER + 'Supernova_Remnant:_The_Veil_Nebula.jpg'
DEFAULT = '%(asctime)s - %(thread)d - %(name)s - %(module)s - %(threadName)s - %(levelname)s => %(message)s'
DEFAULT_LOG_LEVEL = 'DEBUG'

def get_apod_data():
    response = r.get(ENDPOINT_URL).json()
    return response

def setup_logger():
    handler = logging.handlers.WatchedFileHandler(LOG_FOLDER)
    formatter = logging.Formatter(DEFAULT)
    handler.setFormatter(formatter)
    log = logging.getLogger()
    log.addHandler(handler)
    log.setLevel(DEFAULT_LOG_LEVEL)
    return log
    

def download_pic():
    st = time.time()
    response_output = get_apod_data()
    date = response_output['date']
    title = response_output['title'].replace(" ", "_")
    media_type = response_output['media_type']
    apod_link = f'https://apod.nasa.gov/apod/ap{date.replace("-", "")[2:]}.html'
    hdurl = response_output['hdurl']
    image_name = title+'.jpg'
    file_path = OUTPUT_FOLDER + image_name
    lapsed_time = time.time() - st
    print("Lapsed time ")
    print(lapsed_time)
    if not os.path.exists(file_path):
        request.urlretrieve(hdurl, file_path)
    et = time.time()
    print("Time take to download the nasa pic ")
    print(et-st)

if __name__ == '__main__':
    logger = setup_logger()
    logger.info("This is info log")
    logger.fatal("This is fatal log")
    logger.debug("This is debug log")
    download_pic()