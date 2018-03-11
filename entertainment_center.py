import fresh_tomatoes
import media
creation = media.Movie("allah", "who is allah","https://upload.wikimedia.org/wikipedia/commons/7/79/Allah.svg","https://www.youtube.com/watch?v=m_tjxz4yS_U" )
wild_russia = media.Movie("National Geographic", "National Geographic - Wild Russia: Siberia - BBC Planet Earth HD 1080p","https://upload.wikimedia.org/wikipedia/commons/4/4f/A_Russian_Bear.jpg","https://www.youtube.com/watch?v=PfxOhEN8Cr4" )
Rare_Exotic_Animals = media.Movie("Rare_Exotic_Animals", "The Rare and Exotic Animals - National Geographic Documentary","https://upload.wikimedia.org/wikipedia/commons/c/cd/Oryx_gazella_PICT1415.JPG","https://www.youtube.com/watch?v=JZf9TUDYmME" )
africas_wild_west = media.Movie("africas_wild_west", "africas_wild_west","https://upload.wikimedia.org/wikipedia/commons/4/4f/NgoroNgoro_Crater%2C_Tanzania%2C_Africa.jpg","https://www.youtube.com/watch?v=zRt70jyj6tE" )
paradise_found = media.Movie("paradise_found", "paradise_found","https://upload.wikimedia.org/wikipedia/commons/a/a1/Evening%2C_Nile_River%2C_Uganda.jpg","https://www.youtube.com/watch?v=GTlQcfYx8JQ" )
great_white_shark = media.Movie("great_white_shark", "great_white_shark","https://upload.wikimedia.org/wikipedia/commons/3/31/Great_white_shark_south_africa.jpg","https://www.youtube.com/watch?v=zhSeXppv0jY" )
# instances object from class movie with attribute definition
movies = [creation, wild_russia, Rare_Exotic_Animals, africas_wild_west, paradise_found, great_white_shark]
# this array of movies to display on website
fresh_tomatoes.open_movies_page(movies)
# this function from class fresh_tomatoes to open this movie as awebsite