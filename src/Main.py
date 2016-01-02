import Song_Info
import Browser_Actions
import argparse


def get_file_name():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    return args.filename

file_name = get_file_name()
si = Song_Info.Song(file_name)
si.rename_file_to_artist_song_name(file_name)
query = si.return_query()
ba = Browser_Actions.GoogleImage()
ba.search_google_images(query)
ba.save_image()
si.change_album_art()
ba.del_image()
ba.closeup()
