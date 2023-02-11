# from Images import Images
from Sounds import Sounds
from Images import Images
from datetime import datetime, timedelta


class Project:
    Haiku = None
    Images = None
    Sounds = None

    def __init__(self, search_word, num_files, timeout, i):
        self.SearchWord = search_word
        self.Num_Files = num_files
        self.Timeout = timeout
        self.iteration = i
        self.generate_images()
        print("!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!")

        print("!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!")
        self.generate_sounds()


    def generate_sounds(self):
        start = datetime.now()
        print('***Generating Sounds...***')
        self.Sounds = Sounds(self.SearchWord, self.Num_Files, self.iteration)
        print('***Finished generating Sounds in ' + str(datetime.now() - start) + ' seconds***')

    def generate_images(self):
        start = datetime.now()
        print('***Generating Images...***')
        self.Images = Images(self.SearchWord, self.Num_Files, self.iteration)
        print('***Finished generating Images in ' + str(datetime.now() - start) + ' seconds***')