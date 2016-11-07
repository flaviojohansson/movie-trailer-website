import webbrowser


class Movie():
    """This class provides information for the movies being displayed
    
    Attributes:
        title (str): Title of the movie
        year (str): Release Year
        rating (str): One of the VALID_RATINGS
        runtime (str): Duration of the movie
        genre (str): Free text describing the genre
        director (str): Name of director
        actors (str): Name of actors 
        plot (str): Short description of the movie plot 
        poster_image_url (str): Full URL to the movie poster image
        imdb_rating (str): Grade of the movie
        trailer_youtube_id (str): Youtube's movie traiiler id 

    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, year, rating, runtime, genre, director, 
                 actors, plot, poster_image_url, imdb_rating,
                 trailer_youtube_id):
        self.title = title
        self.year = year
        self.rating = rating
        self.runtime = runtime
        self.genre = genre
        self.director = director
        self.actors = actors
        self.plot = plot
        self.poster_image_url = poster_image_url
        self.imdb_rating = imdb_rating
        self.trailer_youtube_id = trailer_youtube_id

    # Check whether or not a movie rating is valid. I'm not forcing the use of it 
    def is_valid_rating(self):
        return self.rating in VALID_RATINGS
