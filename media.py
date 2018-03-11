import webbrowser
# import webbrowser to make my program to connect with browser easy
class Movie():
    # define anew class called movie to use it to make list of movies
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        # initial function define attribute for movie class
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        # this function allow class to open movie with youtube url

    