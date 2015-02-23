import webbrowser

class Movie():
	""" This class provides a way to store movie information.

		Attributes:
			movie_title: A string indicating a movie's title.
			movie_storyline: A string of a movie's plot and storyline.
			poster_image: A string including a URL to the image of a movie's poster.
			trailer_youtube: A string indicating the URL of a movie's YouTube trailer.
			movie_cast: A string indicating a movie's main starring actors.
	"""

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_cast):
		""" Inits Movie with information about each film """
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.cast = movie_cast
