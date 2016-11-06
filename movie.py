import webbrowser


class Movie():
    """ This class provides information  for the movies being displayed """
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, year, rating, release_date, runtime, genre, director, 
                 writer, actors, plot, language, country, awards, poster_image_url,
                 imdb_rating, trailer_youtube_id):
        self.title = title
        self.year = year
        self.rating = rating
        self.release_date = release_date
        self.runtime = runtime
        self.genre = genre
        self.director = director
        self.writer = writer
        self.actors = actors
        self.plot = plot
        self.language = language
        self.country = country
        self.awards = awards
        self.poster_image_url = poster_image_url
        self.imdb_rating = imdb_rating
        self.trailer_youtube_id = trailer_youtube_id

    # Check whether or not a movie rating is valid. I'm not forcing the use of it 
    def is_valid_rating(self):
        return self.rating in VALID_RATINGS
