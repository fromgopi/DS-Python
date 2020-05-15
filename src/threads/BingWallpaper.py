import json
import os
from os.path import isfile
from urllib import request
from urllib.error import HTTPError

from requests import RequestException, get

BASE_URL = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
IMAGE_OUTPUT_FOLDER = '/var/api-logs/bing_wallpapers/'
BING_URL = 'http://www.bing.com'

# Apple Script to set wallpaper
SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""


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
    try:
        # Check if the folder in the path exists.
        # os.mkdir(path=IMAGE_OUTPUT_FOLDER, mode=0o777)
        image_data = json.loads(get(BASE_URL).text)
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
            print("nothing can be done")
        set_mac_screen_background(file_path)
    except HTTPError as httpError:
        print("HttpError")
        print(httpError)
        request.urlretrieve(sd_image_url, filename=file_path)

    except AttributeError as ae:
        print("Attribute Error")
        print(ae)
    except (FileExistsError, FileNotFoundError) as fe:
        print("File Error")
        print(fe)
    except RequestException as re:
        print("Request Exception")
        print(re)


if __name__ == '__main__':
    main_method()
