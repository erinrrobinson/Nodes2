import freesound
import os
import pydub
import FileFolder
import re

class Sounds:
    TOKEN = "a87mbH7WEcDNbf1JBE60r8vKItn5GQmONfozVBIA"
    AUTH_TYPE = "OAuth2"
    dir = "C:/Users/thewi/Desktop/Nodes2/Sounds"
    Sounds = None


    def __init__(self, search_word, num_of_sounds, i):
        self.SearchWord = search_word
        self.nSounds = num_of_sounds
        self.i = i
        self.dir_loop = self.dir + str(i) + '/'

        #Delete and remake directory
        FileFolder.delete_folder(self.dir_loop)
        FileFolder.make_folder(self.dir_loop)

        # Download sounds
        self.sound_download()

        # Rename sounds
        self.rename_sounds()


        # Convert sounds - Not needed for meantime
        # self.convert_sounds()

        # Remove mp3s - Deletes mp3s if not converted
        # FileFolder.remove_files(self.dir, "mp3")

    def sound_download(self):
        client = freesound.FreesoundClient()
        client.set_token(self.TOKEN, self.AUTH_TYPE)
        self.Sounds = client.text_search(query=self.SearchWord, page_size=self.nSounds,
                                         fields="id,name,previews", duration=(1, 5))
        for sound in self.Sounds:
            print("downloading sound" + sound.name)
            sound_name = re.sub(r'[^\w\s]', '', sound.name)
            sound.retrieve_preview("", self.dir_loop + sound_name + ".mp3")
            print('Generated file: ' + sound_name)


    def rename_sounds(self):
        filenum = 1
        for filename in os.listdir(self.dir_loop):
            dst = "sound" + str(filenum) + ".mp3"
            src = self.dir_loop + filename
            dst = self.dir_loop + dst

            # rename() function will rename all the files
            os.rename(src, dst)

            filenum += 1

    # def convert_sounds(self):
    #     sound_count = 0
    #     for i in range(1, self.nSounds + 1):
    #         if FileFolder.does_file_exist(self.dir_loop + 'haiku' + str(i) + '.mp3'):
    #             original_file = self.dir_loop + 'haiku' + str(i) + '.mp3'
    #             converted_file = self.dir_loop + 'haiku' + str(i) + '.wav'
    #             sound = pydub.AudioSegment.from_mp3(original_file)
    #             sound.export(converted_file, format="wav")
    #             sound_count += 1
    #     print('Number of sounds generated: ' + str(sound_count))
