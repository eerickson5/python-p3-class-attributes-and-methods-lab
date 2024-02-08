class Song:
    count = 0
    artists = []
    artist_count = {}
    genres = []
    genre_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_artists(artist)
        self.add_to_genres(genre)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    
    def add_to_genres(self, genre):
        if genre not in Song.genres:
            Song.genres.append(genre)
            Song.genre_count[genre] = 1
        else:
            Song.genre_count[genre] += 1

    @classmethod
    def add_to_artists(self, artist):
        if artist not in Song.artists:
            Song.artists.append(artist)
            Song.artist_count[artist] = 1
        else:
            Song.artist_count[artist] += 1
