import requests as requests
import urllib.request as url
from urllib import parse
import os
from random import randint
import FileFolder
from PIL import Image

class Images:
    apikey = 'nEDQP2rR1NAGYJX81c4yhkeLw0UKvvBM'
    urltrans = "http://api.giphy.com/v1/gifs/search"
    filename = "gif"
    dir = "C:/Users/thewi/Desktop/Nodes2/Images"

    def __init__(self, search_word, num_of_images, i):
        self.List = [search_word]
        s = " "
        self.SearchWord = s.join(self.List)
        self.nImages = num_of_images
        self.dir_loop = self.dir + str(i) + '/'

        # Delete and remake directory
        FileFolder.delete_folder(self.dir_loop)
        FileFolder.make_folder(self.dir_loop)

        # Get images
        self.get_images()

        # Do the renaming because the API returns 1.<filename>.gif, 2.<filename>.gif etc...
        # self.rename_images()


    def get_images(self):
        for number in range(self.nImages):
            arguments = parse.urlencode({
                "q": self.SearchWord,
                "api_key": self.apikey,
                "limit": self.nImages + 1,
                "offset": 0
            })

            apirequest = self.urltrans + "?" + arguments
            r_search = requests.get(apirequest)
            data_search = r_search.json()
            img_url_search = data_search['data'][number]['images']['original']['url']
            savepath = os.path.join(self.dir_loop + self.filename + str(number) + '.gif')
            with open(savepath, 'wb') as f:
                f.write(requests.get(img_url_search).content)
                Image.open(savepath).save(savepath)



    # def get_images(self):
    #     response = google_images_download.googleimagesdownload()
    #     arguments = {"keywords": self.SearchWord,
    #                  "format": self.extension,
    #                  "limit": self.nImages,
    #                  "output_directory": self.download_path,
    #                  "no_directory": True
    #                  }
    #     response.download(arguments)

    # def rename_images(self):
    #     for i in range(1, self.nImages + 1):
    #         for filename in os.listdir(self.download_path):
    #             if filename.startswith(str(i) + "."):
    #                 os.rename(os.path.join(self.download_path, filename),
    #                           os.path.join(self.download_path, "image" + str(i) + ".gif"))
    #             else:
    #                 continue