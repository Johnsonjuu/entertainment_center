import webbrowser

class Movie():
	""" This class provides a way to store movie information """

	VALID_RATINGS = ["G", "PG", "PG-13", "R", "NC-17"]

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_cast):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.cast = movie_cast

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
