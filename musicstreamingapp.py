"""
You are part of a team developing a new music streaming app called "MFun." Your task is to design the core functionality that manages the user's music library and playlist creation. Consider the following requirements:

Music library:
Needs to store a collection of songs and their associated metadata (title, artist, album, genre, length).
Must efficiently retrieve songs by various criteria (artist, album, genre, title).
Must prevent duplicate song entries.

Playlists:
Users can create unlimited playlists.
Each playlist can contain any number of songs, but a song cannot be added multiple times to the same playlist.
Songs can be added, removed, or reordered within playlists.
The app should display songs in the order they were added to the playlist.

Which data structure model(s) would you choose to implement the music library and playlist features? Explain your choices, considering the characteristics of each data structure and the specific requirements of the application.

Data structures to consider:
       Tuples, Sets, Lists, Dictionaries, Trees, Graphs, Stacks, Queues
"""
# Prototype code, you can follow different implementation process

class Song:
    def __init__(self, title, artist, album, genre, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.length = length

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.album}, {self.genre}, {self.length})"

class MusicLibrary:
    def __init__(self):
        self.songs = {}

    def add_song(self, song):
        key = (song.title, song.artist)
        if key not in self.songs:
            self.songs[key] = song
      
    def get_songs_by_artist(self, artist):
        return [song for song in self.songs.values() if song.artist == artist]

    def get_songs_by_album(self, album):
        return [song for song in self.songs.values() if song.album == album]
        
    def get_songs_by_genre(self, genre):
        return [song for song in self.songs.values() if song.genre == genre]
      
    def get_songs_by_title(self, title):
        return self.songs.get((title, None))

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)

    def reorder_songs(self, new_order):
        self.songs = [self.songs[i] for i in new_order if 0 <= i < len(self.songs)]

    def display_playlist(self):
        print(f"Playlist: {self.name}")
        for idx, song in enumerate(self.songs, start=1):
            print(f"{idx}. {song}")
# Create songs
song1 = Song("Song1", "Artist1", "Album1", "Rock", "3:45")
song2 = Song("Song2", "Artist2", "Album2", "Pop", "4:20")
song3 = Song("Song3", "Artist1", "Album3", "Jazz", "5:10")

# Create music library and add songs
music_library = MusicLibrary()
music_library.add_song(song1)
music_library.add_song(song2)
music_library.add_song(song3)

# Retrieve songs by various criteria
print("\nSongs by Artist 1:")
songs_by_artist1 = music_library.get_songs_by_artist("Artist1")
for song in songs_by_artist1:
    print(f"{song.title} - {song.album}")
print("-------------------------------")
print("\nSongs in Album2:")
song_in_album1 = music_library.get_songs_by_album("Album2")
for song in song_in_album1:
    print(f"{song.title} - {song.artist}")
print("-------------------------------")
print("\nSongs in Jazz Genre:")
song_in_jazz = music_library.get_songs_by_genre("Jazz")
for song in song_in_jazz:
    print(f"{song.title} - {song.artist} - {song.album}")
print("-------------------------------")

# Create playlists and add songs
playlist1 = Playlist("MyPlaylist")
playlist1.add_song(song1)
playlist1.add_song(song2)
playlist1.add_song(song3)

# Display playlist
playlist1.display_playlist()

# Remove a song from the playlist
playlist1.remove_song(song2)
print("-------------------------------")
print("\nPlaylist after removing 'Song2':")
playlist1.display_playlist()

# Reorder songs in the playlist
playlist1.reorder_songs([2, 0, 1])
print("-------------------------------")
print("\nPlaylist reordering after remove 'Song2' :")
playlist1.display_playlist()


# Main Requirement:
# Create song example
# Create a music library
# Add songs to the music library
# Get songs by artist
# Create playlists
# Add songs to playlists
# Display playlists
# Searching for songs by artist

# Sample Output:
# Playlist: My Playlist 1
# 1. Song 1 - Artist 1
# 2. Song 2 - Artist 2

# Songs by Artist 1:
# Song 1 - Album 1
