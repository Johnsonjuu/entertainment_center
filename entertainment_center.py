import media
import fresh_tomatoes

full_metal_jacket = media.Movie("Full Metal Jacket",
								"A pragmatic U.S. Marine observes the dehumanizing effects the U.S.-Vietnam War has on his fellow recruits from their brutal boot camp training to the bloody street fighting in Hue.",
								"http://upload.wikimedia.org/wikipedia/en/9/99/Full_Metal_Jacket_poster.jpg",
								"https://www.youtube.com/watch?v=x9f6JaaX7Wg")

pulp_fiction = media.Movie("Pulp Fiction",
						   "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
						   "http://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg",
						   "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					 "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

empire_strikes_back = media.Movie("Star Wars: The Empire Strikes Back",
								  "After the rebels have been brutally overpowered by the Empire on their newly established base, Luke Skywalker takes advanced Jedi training with Master Yoda, while his friends are pursued by Darth Vader as part of his plan to capture Luke.",
								  "http://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
								  "https://www.youtube.com/watch?v=mz_YWNhKOkM")

big_lebowski = media.Movie("The Big Lebowski",
							"'The Dude' Lebowski, mistaken for a millionaire Lebowski, seeks restitution for his ruined rug and enlists his bowling buddies to help get it.",
							"http://upload.wikimedia.org/wikipedia/en/thumb/3/35/Biglebowskiposter.jpg/220px-Biglebowskiposter.jpg",
							"https://www.youtube.com/watch?v=cd-go0oBF4Y")

ace_ventura = media.Movie("Ace Ventura: Pet Detective",
					      "A goofy detective specializing in animals goes in search of a missing dolphin mascot of a football team.",
						  "http://upload.wikimedia.org/wikipedia/en/thumb/8/84/Ace_ventura_pet_detective.jpg/220px-Ace_ventura_pet_detective.jpg",
						  "https://www.youtube.com/watch?v=QzxDlS6QY1s")

a_space_odyssey = media.Movie("2001: A Space Odyssey",
						      "Humanity finds a mysterious, obviously artificial, object buried beneath the Lunar surface and, with the intelligent computer H.A.L. 9000, sets off on a quest.",
						      "http://upload.wikimedia.org/wikipedia/en/thumb/e/ef/2001_A_Space_Odyssey_Style_B.jpg/220px-2001_A_Space_Odyssey_Style_B.jpg",
						      "https://www.youtube.com/watch?v=E8TABIFAN4o")

v_for_vendetta = media.Movie("V for Vendetta",
						      "In a future British tyranny, a shadowy freedom fighter, known only by the alias of 'V', plots to overthrow it with the help of a young woman.",
						      "http://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Vforvendettamov.jpg/220px-Vforvendettamov.jpg",
						      "https://www.youtube.com/watch?v=k_13fFIrhPk")


movies = [full_metal_jacket, pulp_fiction, avatar, empire_strikes_back, big_lebowski, ace_ventura, a_space_odyssey, v_for_vendetta]
fresh_tomatoes.open_movies_page(movies)
