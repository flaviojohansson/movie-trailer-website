import json
import urllib
import os
import movie
import fresh_tomatoes


JSON_FILE_NAME = "movies.json"
DEFAULT_PAGE_TITLE = "Movie Trailer Website"

# Return JSON from the omdb Free webapi.
def get_omdb_data(imdb_id):
    # Any error will throw an exception and funcion exits with no error 
    try:
        url = "http://www.omdbapi.com/?plot=short&r=json&i="
        connection = urllib.urlopen(url + imdb_id)
        output = connection.read()
        connection.close
    except e:
        output = "{}"  # On exception, create an empty JSON string

    return output

# Return a new Movie object if the data was sucessfully retrieved from omdb API
def create_movie_object (imdb_id, youtube_trailer_id):
    omdb_data = get_omdb_data(imdb_id)

    # By default this is the returning value
    new_movie = None

    if omdb_data:  # Was data returned from omdb ?
        # Avoid malformed JSON
        try:
            movies_json = json.loads(omdb_data)
        except ValueError, e:
            movies_json = json.loads("{}")  # On exception, create an empty JSON

        # Please Udacity's code reviewers: is this a correct approach
        # on breaking lines in IF's ? 
        if "True" in movies_json["Response"] and \
           "movie" in movies_json["Type"]:  # Must be a movie
            new_movie = movie.Movie(
                title = movies_json["Title"],
                year = movies_json["Year"],
                rating = movies_json["Rated"],
                runtime = movies_json["Runtime"],
                genre = movies_json["Genre"],
                director = movies_json["Director"],
                actors = movies_json["Actors"],
                plot = movies_json["Plot"],
                poster_image_url = movies_json["Poster"],
                imdb_rating = movies_json["imdbRating"],
                trailer_youtube_id = youtube_trailer_id            
        )

    return new_movie

# Main function just to keep 'movie' names concerns separated 
def main():
    # Create an empty movies list
    movies = []

    # Default page title in case none is supplied in the JSON file
    page_title = DEFAULT_PAGE_TITLE

    # Build full path for JSON file
    dir_path = os.path.dirname(os.path.realpath(__file__))  # Directory of this py file
    full_path = "\\".join([dir_path, JSON_FILE_NAME])

    if os.path.isfile(full_path):  # Check if file exists
        # Open JSON file and parse the data to a JSON object
        movies_json_data = open(full_path).read()

        # Avoid malformed JSON
        try:
            movies_json = json.loads(movies_json_data)
        except ValueError, e:
            movies_json = json.loads("{}")  # On exception, create an empty JSON

        # Set page name if key exists in JSON file
        if ("page_title" in movies_json):
            page_title = movies_json["page_title"]

        if ("movies" in movies_json):  # Check if key 'movies' exists in JSON file
            # For each movie, try to create a Movie() object and add to movies List
            for movie in movies_json["movies"]:
                # Create an instance of Movie() on success, or None
                movie_instance = create_movie_object(movie["imdb_id"],
                                                     movie["youtube_trailer_id"])
                # Add the new Movie() object to movies List
                if movie_instance:
                    movies.append(movie_instance)

    # Finally render the webpage an open it in webbrowser
    fresh_tomatoes.open_movies_page(page_title, movies)

if __name__ == "__main__":
    main()
