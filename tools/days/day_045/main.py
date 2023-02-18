from days.day_045.files.helpers import *


def day_045():
    title("MUST WATCH LIST")
    # ------------ ORIGINAL -------------
    # response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
    # response.encoding="utf-8"
    # contents = response.text

    # EMPIRE MAG HAS BLOCKED LIVE SCRAPING WITH JS, SO SAVED RENDERED HTML TO FILE
    # Open file containing html
    with open("./tools/days/day_045/files/top100.html", encoding="utf-8") as website:
        contents = website.read()

    # Use bs4 to parse contents
    soup = BeautifulSoup(contents, "html.parser")

    # scrape html for all titles and use list comprehension to save them in variable
    titles_html = soup.find_all(name="h3", class_="jsx-4245974604")
    titles = [eachtitle.getText() for eachtitle in titles_html]

    # Order the titles and print them
    ordered_titles = titles[::-1]
    nls(ordered_titles)

    # Save each movie in a text file as a list
    with open("./tools/days/day_045/files/movies.txt", mode="w") as file:
        for movie in ordered_titles:
            file.write(f"{movie}\n")

    nls("Top 100 Movies saved to file 'movies.txt'.")
