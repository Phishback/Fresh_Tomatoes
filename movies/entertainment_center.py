import media
import fresh_tomatoes

gangs_of_new_york = media.Movie("Gangs of New york",
                        "In 1860 New York, Gangs rule the street",
                        "https://upload.wikimedia.org/wikipedia/en/a/ae/Gangs_of_New_York_Poster.jpg",
                        "https://www.youtube.com/watch?v=qHVUPri5tjA")
print(gangs_of_new_york.storyline)
#gangs_of_new_york.show_trailer()

deadpool = media.Movie("Deadpool",
                     "Wade Wilson is a former Special Forces operative who now works as a mercenary.",
                     "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
                     "https://www.youtube.com/watch?v=Xithigfg7dA")
print(deadpool.storyline)
#deadpool.show_trailer()

spirited_away = media.Movie("Spirited Away",
                            "A little girl gets trapped in a spirit world and must find her way home.",
                            "https://upload.wikimedia.org/wikipedia/en/3/30/Spirited_Away_poster.JPG",
                            "https://www.youtube.com/watch?v=ByXuk9QqQkk&t=4s")
print(spirited_away.storyline)
#spirited_away.show_trailer()

doctor_strange = media.Movie("Doctor Strange",
                             "When traditional medicine fails Steven Strange, he looks for healing, and hope, in a mysterious enclave.",
                             "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",
                             "https://www.youtube.com/watch?v=Lt-U_t2pUHI")
print(doctor_strange.storyline)

grandmas_boy = media.Movie("Grandma's Boy",
                           "When he and his roommate can't pay rent, video game creator, Alex finds himself homeless and moves in with his wacky grandmother.",
                           "https://upload.wikimedia.org/wikipedia/en/2/26/Grandma%27s_Boy_poster.jpg",
                           "https://www.youtube.com/watch?v=vsEuOw3ihbs")
print(grandmas_boy.storyline)

up_movie = media.Movie("Up",
                       "Tying thousands of balloons to his house, 78-year-old Carl Fredricksen flies away to the South American wilderness",
                       "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
                       "https://www.youtube.com/watch?v=qas5lWp7_R0")
print(up_movie.storyline)


movies = [gangs_of_new_york, deadpool, spirited_away, doctor_strange, grandmas_boy, up_movie]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.valid_ratings)


                             

                            


