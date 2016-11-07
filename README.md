# movie-trailer-website

* Udacity Full Stack Web Developer Nanodegree Project #1
* This project creates a HTML page based on a given list of movies

## Getting started
* You must have Python 2.7 installed.
* Clone this repository into your computer. `git clone https://github.com/flaviojohansson/movie-trailer-website.git`
* In the root directory of the project, just type: `python entertainment_center.py`

## Configuring movies.json

This project comes with a file named movies.json, which contains the list of movies to be rendered in a page. Here's an example:

```
{
    "page_title": "Movies I've watched with my daughter",
    "movies": [
        {
            "__title": "The Goonies",
            "imdb_id": "tt0089218",
            "youtube_trailer_id": "hJ2j4oWdQtU"
        },
        {
            "__title": "Ghostbusters",
            "imdb_id": "tt0087332",
            "youtube_trailer_id": "8qXjho3E15k"
        }
    ]
}
```

You can change the page title by changing the value of the key `page_title`.
The `movies` array contains the movies you want to show. There are only two mandatory keys:
* imdb_id: The ID from imdb website. eg: http://www.imdb.com/title/tt0451279/ the ID is `tt0451279`
* youtube_trailer_id: The ID from youtube video. eg: https://www.youtube.com/watch?v=yI2oS2hoL0k the ID is `yI2oS2hoL0k`

## Troubleshooting

* Depending on the size of the movie plot, bootstrap will not render 3 movies in a single row, putting one column in a new row

