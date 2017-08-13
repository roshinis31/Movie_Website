import fresh_tomatoes
import media
thupaki = "https://upload.wikimedia.org/wikipedia/en/b/be/Thuppakki_poster.jpg"
magadhera = "http://photos.filmibeat.com/ph-big/2012/01/1325845008613892.jpg"
viveegam = "https://upload.wikimedia.org/wikipedia/en/b/be/Vivegam_poster.jpg"
Mr = "https://upload.wikimedia.org/wikipedia/en/9/92/Mr._Perfect_poster.jpg"
brindhavan = "http://www.southmp3.co/wp-content/uploads/2010/09/00frontd.jpg",
Magadheera = media.Movie("Magadheera",
                         "Past life",
                         magadhera,
                         "https://www.youtube.com/watch?v=C1pLJJqKmMM")
Thupakki = media.Movie("Thupaaki",
                       "Army man",
                       thupaki,
                       "https://www.youtube.com/watch?v=2S0Fk2Dh9Mk")
Vivegam = media.Movie("Vivegam",
                      "Hard working",
                      viveegam,
                      "https://www.youtube.com/watch?v=uM7zTAMFRxc")
Mr_perfect = media.Movie("Mr.perfect",
                         "Romance",
                         Mr,
                         "https://www.youtube.com/watch?v=41Lbd7nZJAI")
Brindhavanam = media.Movie("Brindavanam",
                           "Romance",
                           brindhavan,
                           "https://www.youtube.com/watch?v=J9ZhAtJClsE")
films = [Magadheera, Thupakki, Vivegam, Mr_perfect, Brindhavanam]
fresh_tomatoes.open_movies_page(films)
