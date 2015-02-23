import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>CmL's Top 8</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <!-- added jquery ui for creating mouseover tooltip -->
    <script src="http://code.jquery.com/ui/1.11.2/jquery-ui.js"></script>
    <link rel="stylesheet" href="http://code.jquery.com/ui/1.11.2/themes/smoothness/jquery-ui.css">
    <!-- added font awesome for social media buttons -->
    <link href="http://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            background-color: #FFCC66;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #FFC;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
        // Tooltip integration for jQuery UI and allowing of HTML in tooltip
        $(function() {
            $(document).tooltip({
                content: function() {
                return $(this).attr('title');
                }
            });
        });
        // Poistioning for jQuery UI tooltip
        $(document).tooltip({
            position: { my: "left top", at: "right top", collision: "flipfit" }
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#" style="color: #BFFC44">CmL's Top 8 Movies</a>
          </div>
            <!-- Social media icons in nav bar -->
              <ul class="nav navbar-nav navbar-right nav-pills">
                <li>
                    <a href="http://facebook.com/" class="btn btn-social-icon btn-facebook">
                        <i class="fa fa-facebook"></i>
                    </a>
                </li>
                <li>
                    <a href="http://twitter.com/" class="btn btn-social-icon btn-twitter">
                        <i class="fa fa-twitter"></i>
                    </a>
                </li>
                <li>
                    <a href="http://www.linkedin.com/in/" class="btn btn-social-icon btn-linkedin">
                        <i class="fa fa-linkedin"></i>
                    </a>
                </li>
                <li>
                    <a href="https://github.com/carlmlane" class="btn btn-social-icon btn-github">
                        <i class="fa fa-github"></i>
                    </a>
                </li>
              </ul>
        </div>
      </div>
    </div>
    <!-- container for movie tiles section -->
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry's html template
# Includes a mouseover tooltip for showing movie's plot & starring actors
movie_tile_content = '''

<div class="col-md-3 col-lg-3 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
<!-- HTML in title will display in the mouseover tooltip -->
<div title="<div style='background-color: #CCC; border: dashed; border-width: 1px'><em>Starring:</em> <b>{movie_cast}</b></div><br/><em>Plot:</em> {movie_storyline}">
<!-- Poster image and title that will display on front of tile -->
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
</div>
'''

def create_movie_tiles_content(movies):
    """ Generates the HTML content for the movie tiles container.

        Generates an appropriate YouTube URL for each movie and initializes
        the movies' information from the input array.

        Args:
            movies: An array of movies to create tiles on HTML template.

        Returns:
            A string of all movie's information.
    """
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        # Added movie storyline and cast to be accessable by page template
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_storyline=movie.storyline,
            movie_cast=movie.cast
        )
    return content

def open_movies_page(movies):
    """ Writes the HTML file from base template and movies array.

        Creates an HTML file named fresh_tomatoes.html inside the same
        directory as entertainment_center.py. If a previous version of
        fresh_tomatoes.html exists, it will be overwritten. Upon creating
        the HTML file, it will be automatically be openened by your default
        web broswer.

    Args:
        movies: An array of movies to be displayed in HTML template.

    Returns:
        An HTML file named fresh_tomatoes.html to the programs's directory.
        Opens the computer's default web browser to display the file.

    """
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)  # open in a new tab, if possible
