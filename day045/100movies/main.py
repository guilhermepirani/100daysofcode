from bs4 import BeautifulSoup

# Using file instead of request.get because of javascript random class name on render
# check https://pypi.org/project/requests-html/
with open('C:/100daysofcode/day045/100movies/website.html') as file:
    website_html = file.read()

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="jsx-2692754980")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("C:/100daysofcode/day045/100movies/movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")