class Song:
    all = []
    genres = []
    artists = []
    count = 0
    genre_count = {}
    artist_count = {}

    def __init__( self, name, artist, genre ):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_new_song( self )

    @classmethod
    def add_new_song( cls, new_song ):
        cls.all.append( new_song )
        if new_song.genre not in cls.genres:
            cls.genres.append(new_song.genre)
            cls.genre_count[new_song.genre] = 0
        if new_song.artist not in cls.artists:
            cls.artists.append(new_song.artist)
            cls.artist_count[new_song.artist] = 0
        cls.count += 1
        cls.genre_count[new_song.genre] += 1
        cls.artist_count[new_song.artist] += 1