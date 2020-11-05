import json
import os
from os.path import isfile
from urllib import request
from urllib.error import HTTPError

from requests import RequestException, get
from logging import getLogger, Formatter, DEBUG

BASE_URL = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
IMAGE_OUTPUT_FOLDER = '/var/api-logs/bing_wallpapers/'
LOG_FOLDER='/var/api-logs'
BING_URL = 'http://www.bing.com'
DEFAULT = '%(asctime)s - %(thread)d - %(name)s - %(module)s - %(threadName)s - %(levelname)s - %(message)s'

# Apple Script to set wallpaper
SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""


def log_module(file_name='bing'):
    from logging.handlers import RotatingFileHandler
    try:
        log_file = LOG_FOLDER + '/' + file_name + '.log'
        log = getLogger(log_file)
        handler = RotatingFileHandler(log_file, maxBytes=100000000, backupCount=3)
        formatter = Formatter(DEFAULT)
        handler.setFormatter(formatter)
        log.addHandler(handler)
        log.setLevel(DEBUG)
        return log
    except Exception as ex:
        print(ex)


# LOG = log_module()

def set_mac_screen_background(file):
    """
    Sets the wallpaper in mac home screen.

    :param file:
    :return: None:
    """
    if isfile(file):
        import subprocess
        subprocess.Popen(SCRIPT % file, shell=True)
        print('Wallpaper set to ' + file)


def main_method():
    LOG = log_module()	
    try:
        # Check if the folder in the path exists.
        # os.mkdir(path=IMAGE_OUTPUT_FOLDER, mode=0o777)
        image_data = json.loads(get(BASE_URL).text)
        LOG.info("image")
        # This URL is for high Definition.
        sd_image_url = BING_URL + image_data.get('images')[0].get('url')
        hd_image_url = BING_URL + '/hpwp' + image_data.get('images')[0].get('hsh')
        image_title = image_data.get('images')[0].get('title')
        # image_title = "Nursing the world to health"

        image_title = image_title.replace(" ", "_").replace(",", "_") + '.jpg'
        file_path = IMAGE_OUTPUT_FOLDER + image_title
        if not os.path.exists(file_path):
            request.urlretrieve(hd_image_url, filename=file_path)
        else:
            LOG.debug('Nothing can be done')
            print("nothing can be done")
        set_mac_screen_background(file_path)
    except HTTPError as httpError:
        LOG.error("HttpError")
        print("HttpError")
        LOG.debug('HTTP ERROR')
        print(httpError)
        request.urlretrieve(sd_image_url, filename=file_path)
        set_mac_screen_background(file_path)

    except AttributeError as ae:
        LOG.error("Attribute Error")
        print("Attribute Error")
        print(ae)
    except (FileExistsError, FileNotFoundError) as fe:
        LOG.error('File Error')
        print("File Error")
        print(fe)
    except RequestException as re:
        LOG.error("Request Exception")
        print("Request Exception")
        print(re)


if __name__ == '__main__':
    # LOG.info("Inside Main Method main method func is been called for the first time.")
    main_method()
    # log_module()
