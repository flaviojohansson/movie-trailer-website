import json
import urllib
import movie
import fresh_tomatoes


# Free webapi. For more information, check it out omdbapi.com
def get_omdb_data(imdb_id):
    connection = urllib.urlopen("http://www.omdbapi.com/?plot=short&r=json&i=" + imdb_id)
    output = connection.read()
    connection.close
    return output


# Returns a new Movie object if the data was sucessfully retrieved from omdb API
def create_movie_object (imdb_id, youtube_trailer_id):
    omdb_data = get_omdb_data(imdb_id)
    if omdb_data:
        movies_json = json.loads(omdb_data)
        new_movie = movie.Movie(
            title = movies_json["Title"],
            year = movies_json["Year"],
            rating = movies_json["Rated"],
            release_date = movies_json["Released"],
            runtime = movies_json["Runtime"],
            genre = movies_json["Genre"],
            director = movies_json["Director"],
            writer = movies_json["Writer"],
            actors = movies_json["Actors"],
            plot = movies_json["Plot"],
            language = movies_json["Language"],
            country = movies_json["Country"],
            awards = movies_json["Awards"],
            poster_image_url = movies_json["Poster"],
            imdb_rating = movies_json["imdbRating"],
            trailer_youtube_id = youtube_trailer_id            
        )
        return new_movie

    # When no data is get from omdb site, returns None
    return None


# Main function just to keep 'movie' concerns separated 
def main():
    # Creates an empty movies list
    movies = []
    # Opens the json file and reads it
    movies_json_data = open("movies.json").read()
    # Parse the data to a JSON object
    movies_json = json.loads(movies_json_data)
    # For each movie, retrieve information from omdbAPI  
    for movie in movies_json["movies"]:
        movie_instance = create_movie_object(movie["imdb_id"], movie["youtube_trailer_id"])
        if movie_instance:
            movies.append(movie_instance)

    fresh_tomatoes.open_movies_page(movies)

if __name__ == "__main__":
    main()
