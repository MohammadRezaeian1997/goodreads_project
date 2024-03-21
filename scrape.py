import requests
from bs4 import BeautifulSoup


def scrape_goodreads(pages=5):
    base_url = "https://www.goodreads.com"
    books_data = []

    for page_num in range(1, pages + 1):
        url = f"{base_url}/shelf/show/best_books_of_all_time?page={page_num}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        books = soup.find_all("tr", {"itemtype": "http://schema.org/Book"})

        for book in books:
            title = book.find("a", {"class": "bookTitle"}).text.strip()
            author = book.find("span", {"itemprop": "name"}).text.strip()
            rating = float(book.find("span", {"class": "minirating"}).text.strip().split()[1])

            books_data.append({"title": title, "author": author, "rating": rating})

    return books_data
