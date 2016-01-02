import eyed3
import os


class Song:
    def __init__(self, file_name):
        self.audiofile = eyed3.load(file_name)

    def rename_file_to_artist_song_name(self, file_name):
        self.new_file_name = os.path.dirname(os.path.abspath('__file__')) + \
                        '\%s - %s' % (self.audiofile.tag.artist, self.audiofile.tag.title) + \
                        os.path.splitext(file_name)[1]
        os.rename(file_name, self.new_file_name)

    def return_query(self):
        return self.audiofile.tag.artist + '-' + self.audiofile.tag.title

    def change_album_art(self):
        self.audiofile = eyed3.load(self.new_file_name)
        imagedata = open('Album Art.jpg', 'rb').read()
        self.audiofile.tag.images.set(3, imagedata, "image/jpeg", u"")
        self.audiofile.tag.save()



