import webbrowser


class Movie():
    def __init__(self, movie, movie_storyline, poster, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_id

        def show_trailer(self):
            webbrowser.open(self.trailer_youtube_url)
